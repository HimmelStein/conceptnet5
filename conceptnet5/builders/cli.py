import click
from .combine_assertions import combine_assertions
from .reduce_assoc import reduce_assoc
from .morphology import prepare_vocab_for_morphology, subwords_to_edges


@click.group()
def cli():
    pass


@cli.command(name='combine')
@click.argument('input', type=click.Path(readable=True, dir_okay=False))
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
def run_combine(input, output):
    """
    Combine edges that have the same relation, start, and end, into
    higher-level assertions that add their weights and sources.

    `input` is a tab-separated CSV file to be grouped into assertions.
    `output` is the combined assertions, as a Msgpack stream.
    """
    combine_assertions(input, output)


@cli.command(name='reduce_assoc')
@click.argument('input_filenames', nargs=-1, type=click.Path(readable=True, dir_okay=False))
@click.argument('output', type=click.Path(writable=True, dir_okay=False))
def run_reduce_assoc(input_filenames, output):
    """
    Takes in a file of tab-separated simple associations, one or more 
    hdf5 files defining vector embeddings, and removes from the associations 
    low-frequency terms and associations that are judged unlikely to be
    useful by various filters.
    """
    reduce_assoc(input_filenames[0], input_filenames[1:], output)


@cli.command('prepare_morphology')
@click.argument('language')
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def run_prepare_morphology(language, input, output):
    prepare_vocab_for_morphology(language, input, output)


@cli.command('subwords')
@click.argument('language')
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('wb'))
def run_subwords(language, input, output):
    subwords_to_edges(language, input, output)
