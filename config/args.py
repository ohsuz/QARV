import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--config_file", type=str, default="./config/config.yml", help="Path to the configuration YAML file")
parser.add_argument("--prompts_file", type=str, default="./config/prompt.yml", help="Path to the prompts YAML file")
parser.add_argument("--exp_report_file", type=str, default="./exp/report.csv", help="Path to the experimental results file")
parser.add_argument("--num_gpus", type=str, default="auto", help = "Number of GPUs for distributed inference")
parser.add_argument("--exp", type=str, default=None, help = "Experiment Options (current options: sc, ...)")


def get_args():
    return parser.parse_args()