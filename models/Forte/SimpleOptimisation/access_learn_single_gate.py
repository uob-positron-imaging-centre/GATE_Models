import coexist

# Use ACCESS to learn the simulation parameters
access = coexist.Access("simulation_script_gate.py")
access.learn(num_solutions = 100, target_sigma = 0.1, random_seed = 12349)




