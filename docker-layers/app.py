import json
from utils import helper_function

def main():
    with open('config.json') as f:
        config = json.load(f)
    result = helper_function(config)
    print(result)

if __name__ == "__main__":
    main()
