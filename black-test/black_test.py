l = [1, 2, 3]

ImportantClass.important_method(
    exc, limit, lookup_lines, capture_locals, extra_argument
)


def very_important_function(
    template: str,
    *variables,
    file: os.PathLike,
    engine: str,
    header: bool = True,
    debug: bool = False
):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, 'w') as f:
        pass
