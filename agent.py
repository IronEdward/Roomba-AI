import numpy as np
from collections import defaultdict
from constants import *
from time import sleep
from keras.models import Sequential
from keras.layers import Dense
import pickle

class Agent_actor():
    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(2, input_shape=(1,), init='random_uniform'))
        self.model.add(Dense(4, init='random_uniform'))
        self.model.summary()
        self.model.compile(loss='categorical_crossentropy', optimizer='adam')

    def train(self, X, Y):
        X = np.array(X); Y = np.array(Y)
        self.model.fit(X, Y, epochs=1, verbose=0)
    
    def predict(self, X):
        X = np.array(X)
        return np.argmax(self.model.predict(X)[0])

class Agent_critic():
    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(3, input_shape=(1,), init='random_uniform'))
        self.model.add(Dense(1, init='random_uniform'))
        self.model.summary()
        self.model.compile(loss='mean_squared_error', optimizer='adam')

    def train(self, X, Y):
        X = np.array(X); Y = np.array(Y)
        self.model.fit(X, Y, epochs=1, verbose=0)
    
    def predict(self, X):
        X = X[np.newaxis]
        return self.model.predict(X)[0]

    #! Don't need this for now...
    #! No need to comment it out but whatevs 
    """
    def make_epsilon_greedy_policy(epsilon, nA):
        def policy_fn(observation):
            A = np.ones(nA, dtype=float) * epsilon / nA
            action_values = []
            for j in range(action_space):
                observation = list(observation[:3])
                action_values.append(nn.predict(np.array(observation + [j])))
            best_action = np.argmax(action_values)
            A[best_action] += (1.0 - epsilon)
            return A
        return policy_fn

    def mc_control_epsilon_greedy(num_episodes, discount_factor=1.0, epsilon=0.2):
        returns_sum = defaultdict(float)
        returns_count = defaultdict(float)
            
        policy = make_epsilon_greedy_policy(epsilon, action_space)
        for i_episode in range(1, num_episodes + 1):
            episode = []
            state = env.reset()
            accumulated_reward = 0
            if i_episode >= num_episodes - 10:
                input("\nWaiting for input...")
            for t in range(time):
                probs = policy(state)
                action = np.random.choice(np.arange(len(probs)), p=probs)
                next_state, reward = env.action(action, t)
                if reward >= 0:
                    accumulated_reward += reward
                episode.append((state, action, reward))
                state = next_state
                env.draw()
                if next_state[3] == True:
                    break
            if i_episode % 200 == 0:
                print("\rEpisode {}/{}.   ".format(i_episode, num_episodes), end="")        
                print("Accumulated Reward:", accumulated_reward)
                sys.stdout.flush()
            sa_in_episode = set([(tuple(x[0]), x[1]) for x in episode])
            epoch_x = []; epoch_y = []

            for state, action in sa_in_episode:
                sa_pair = (state, action)
                first_occurence_idx = next(i for i,x in enumerate(episode) if x[0] == state and x[1] == action)

                G = sum([x[2]*(discount_factor**i) for i,x in enumerate(episode[first_occurence_idx:])])

                returns_sum[sa_pair] += G
                returns_count[sa_pair] += 1.0
                state = list(state[:3])
                epoch_x.append(state + [action]); epoch_y.append([returns_sum[sa_pair] / returns_count[sa_pair]])
            # * Train the NN
            nn.train(epoch_x, epoch_y)
            epsilon *= 0.9
        return policy
        """