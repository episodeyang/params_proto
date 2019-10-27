#!/Users/geyang/anaconda3/bin/python
from params_proto import cli_parse, Proto


@cli_parse
class Config:
    """
    Your ICLR best paper project

    -- Ge
    """
    seed = Proto(10, help="random seed for the environment")


if __name__ == "__main__":
    print(f"seed is {Config.seed}")
