import pynini
from pynini.lib import pynutil

from nemo_text_processing.text_normalization.zh.graph_utils import (  # MIN_NEG_WEIGHT,
    NEMO_ALPHA,
    NEMO_CHAR,
    NEMO_NOT_SPACE,
    NEMO_SIGMA,
    NEMO_SPACE,
    NEMO_SPACE_CHAR,
    delete_space,
    generator_main,
)
from nemo_text_processing.text_normalization.zh.taggers.punctuation import PunctuationFst
from nemo_text_processing.utils.logging import logger


def apply_fst(text, fst):
    """ Given a string input, returns the output string
  produced by traversing the path with lowest weight.
  If no valid path accepts input string, returns an
  error.
  """
    try:
        print(pynini.shortestpath(text @ fst).string())
    except pynini.FstOpError:
        print(f"Error: No valid output with given input: '{text}'")


remove_space_around_single_quote = pynini.cdrewrite(delete_space, NEMO_NOT_SPACE, NEMO_NOT_SPACE, NEMO_SIGMA)

text = input(str('inputs: '))
apply_fst(text, remove_space_around_single_quote)