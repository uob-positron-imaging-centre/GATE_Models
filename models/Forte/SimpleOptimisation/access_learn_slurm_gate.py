import coexist
from coexist.schedulers import SlurmScheduler

with open("bluebear_modules.sh") as f:
    commands = f.readlines()

scheduler = SlurmScheduler(
    "4:0:0",           # Time allocated for a single simulation
    commands = commands,        # Commands you'd add in the sbatch script, after `#`
    qos = "bbdefault",
    mem = "8G",
    account = "mangers-positron-imaging-centre",
    constraint = "icelake",     # Any other #SBATCH -- <CMD> = "VAL" pair
)

# Use ACCESS to learn the simulation parameters
access = coexist.Access("simulation_script_gate.py", scheduler)
access.learn(num_solutions = 100, target_sigma = 0.1, random_seed = 12349)




