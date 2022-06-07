import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', dest='config', type=str,
                        help="指定使用的config.ini", required=True)
    return parser


def get_config():
    parser = get_parser()
    args = parser.parse_args()
    return args.config
