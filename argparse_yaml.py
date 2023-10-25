import argparse
import yaml

EXEC_ARGS = ["prog", "description"]

COMMAND_ARGS = ["title", "description", "parser_class", "action", "option_string", "dest", "required", "help"]

SUBCOMMAND_ARGS = ["help", "description"]


def default_command(ctx):
    return {
        "dest": ctx + "_command" if ctx else "command",
        "required": True
    }


ARGUMENT_ARGS = ["help", "action"]

FLAG_ARGS = ["help"]


def default_flag(flag_name):
    return {
        "action": "store_true",
        "dest": flag_name
    }


OPTION_ARGS = ["help"]


def default_option(option_name):
    return {
        "dest": option_name
    }


def argparser_from_dict(curr_parser, config, ctx=""):
    if "commands" in config:
        commands = curr_parser.add_subparsers(**get_kwargs(
            config["commands"], COMMAND_ARGS, default_command(ctx), consume=True))
        for (cmd, cmd_config) in config["commands"].items():
            cmd_parser = commands.add_parser(cmd, **get_kwargs(cmd_config, SUBCOMMAND_ARGS))
            argparser_from_dict(cmd_parser, cmd_config, ctx + "_" + cmd if ctx else cmd)
    if "arguments" in config:
        arguments = config["arguments"]
        for argument in arguments:
            (arg_name, arg_config) = list(argument.items())[0]
            curr_parser.add_argument(arg_name, **get_kwargs(arg_config, ARGUMENT_ARGS))
    if "flags" in config:
        flags = config["flags"]
        for (flag_name, flag_config) in flags.items():
            short = flag_config.get("short", None)
            if short is not None:
                short = "-" + short
            long = flag_config.get("long", None)
            if long is not None:
                long = "--" + long

            kwargs = get_kwargs(flag_config, FLAG_ARGS, default_flag(flag_name))

            if short is not None and long is not None:
                curr_parser.add_argument(short, long, **kwargs)
            elif long is None:
                curr_parser.add_argument(short, **kwargs)
            elif short is None:
                curr_parser.add_argument(long, **kwargs)
            else:
                curr_parser.add_argument(short, long, **kwargs)
    if "options" in config:
        options = config["options"]
        for (option_name, option_config) in options.items():
            short = option_config.get("short", None)
            if short is not None:
                short = "-" + short
            long = option_config.get("long", None)
            if long is not None:
                long = "--" + long

            kwargs = get_kwargs(option_config, OPTION_ARGS, default_option(option_name))

            if short is not None and long is not None:
                curr_parser.add_argument(short, long, **kwargs)
            elif long is None:
                curr_parser.add_argument(short, **kwargs)
            elif short is None:
                curr_parser.add_argument(long, **kwargs)
            else:
                curr_parser.add_argument(short, long, **kwargs)
    return curr_parser


def argparser_from_config(path):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
        return argparser_from_dict(
            argparse.ArgumentParser(**get_kwargs(config, EXEC_ARGS)),
            config
        )

def get_kwargs(dict, args, default=None, consume=False):
    kwargs = {}
    if default is not None:
        kwargs = default
    for arg in args:
        if arg in dict:
            kwargs[arg] = dict[arg]
            if consume:
                del dict[arg]
    return kwargs