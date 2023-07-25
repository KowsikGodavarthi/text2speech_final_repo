import numpy as np
import tensorflow as tf
import random
# Define the game environment
class SnakeGame:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.snake = [(0, 0)]
        self.food = (random.randint(0, self.width-1), random.randint(0, self.height-1))
        self.direction = (1, 0)

    def move(self, action):
        if action == 0:
            self.direction = (-1, 0)  # left
        elif action == 1:
            self.direction = (1, 0)   # right
        elif action == 2:
            self.direction = (0, -1)  # up
        elif action == 3:
            self.direction = (0, 1)   # down

        new_head = tuple(map(lambda x, y: x + y, self.snake[0], self.direction))
        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.food = (random.randint(0, self.width-1), random.randint(0, self.height-1))
            return 1
        elif new_head in self.snake or \
             new_head[0] < 0 or new_head[0] >= self.width or \
             new_head[1] < 0 or new_head[1] >= self.height:
            return -1
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()
            return 0

    def get_state(self):
        state = np.zeros((self.width, self.height))
        for s in self.snake:
            state[s[0], s[1]] = 1
        state[self.food[0], self.food[1]] = 2
        return state

# Define the AI agent
class SnakeAgent:
    def __init__(self, input_size, output_size):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(input_size,)),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(output_size, activation='softmax')
        ])
        self.model.compile(optimizer=tf.keras.optimizers.Adam(),
                           loss=tf.keras.losses.CategoricalCrossentropy(),
                           metrics=[tf.keras.metrics.CategoricalAccuracy()])

    def get_action(self, state):
        q_values = self.model.predict(np.array([state]))
        action = np.argmax(q_values)
        return action

    def train(self, states, actions, rewards):
        actions_one_hot = tf.one_hot(actions, depth=self.model.output_shape[1])
        with tf.GradientTape() as tape:
            q_values = self.model(states)
            selected_q_values = tf.reduce_sum(tf.multiply(q_values, actions_one_hot), axis=1)
            loss = tf.keras.losses.mean_squared_error(rewards, selected_q_values)
        grads = tape.gradient(loss, self.model.trainable_variables)
        self.model.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))

# Define the main function for training the AI agent
def train_snake_agent(num_episodes=1000, max_steps=1000, batch_size=32, gamma=0.95):
    game = SnakeGame()
    agent = SnakeAgent(game.width * game.height,4)
    epsilon = 1.0
    epsilon_min = 0.01
    epsilon_decay = 0.001
    memory = []
    for i in range(num_episodes):
        state = game.get_state()
        done = False
        total_reward = 0
        for j in range(max_steps):
            # Choose an action using epsilon-greedy policy
            if np.random.rand() < epsilon:
                action = np.random.randint(0, 4)
            else:
                action = agent.get_action(state)
                # Take the action and observe the reward and new state
                reward = game.move(action)
                next_state = game.get_state()

                # Store the experience in memory
                memory.append((state, action, reward, next_state, done))

                # Update the state and total reward
                state = next_state
                total_reward += reward

                if reward == -1 or reward == 1:
                    done = True

                if done:
                    break

            # Train the agent using experience replay
            if len(memory) >= batch_size:
                # Sample a batch of experiences from memory
                batch = random.sample(memory, batch_size)

                # Extract the states, actions, rewards, and next states from the batch
                states, actions, rewards, next_states, dones = zip(*batch)

                # Convert the inputs to tensors
                states = tf.convert_to_tensor(states)
                next_states = tf.convert_to_tensor(next_states)

                # Compute the target Q-values using the Bellman equation
                next_q_values = agent.model.predict(next_states)
                max_next_q_values = np.max(next_q_values, axis=1)
                targets = np.array(rewards) + gamma * max_next_q_values * (1 - np.array(dones))

                # Compute the current Q-values and the loss
                current_q_values = agent.model.predict(states)
                actions_one_hot = tf.one_hot(actions, depth=agent.model.output_shape[1])
                selected_q_values = tf.reduce_sum(tf.multiply(current_q_values, actions_one_hot), axis=1)
                loss = tf.keras.losses.mean_squared_error(targets, selected_q_values)

                # Update the weights of the agent
                agent.model.train_on_batch(states, targets)

            # Decay the exploration rate
            if epsilon > epsilon_min:
                epsilon -= epsilon_decay

            # Print the results of the episode
            print(
                "Episode {}/{} - Total Reward: {} - Epsilon: {:.2f}".format(i + 1, num_episodes, total_reward, epsilon))

