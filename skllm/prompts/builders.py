from typing import Union

from skllm.prompts.templates import (
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM1,
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM2,
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM3,
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM4,
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM1,
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM2,
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM3,
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM4,
)

# TODO add validators


def build_zero_shot_prompt_slc_mu_dim1(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM1
) -> str:
    """Builds a prompt for zero-shot single-label classification (MU Dimension 1).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM1

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)

def build_zero_shot_prompt_slc_mu_dim2(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM2
) -> str:
    """Builds a prompt for zero-shot single-label classification (MU Dimension 2).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM2

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)

def build_zero_shot_prompt_slc_mu_dim3(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM3
) -> str:
    """Builds a prompt for zero-shot single-label classification (MU Dimension 3).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM3

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)

def build_zero_shot_prompt_slc_mu_dim4(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM4
) -> str:
    """Builds a prompt for zero-shot single-label classification (MU Dimension 4).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM4

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)

def build_few_shot_prompt_slc(
    x: str,
    labels: str,
    training_data: str,
    template: str = FEW_SHOT_CLF_PROMPT_TEMPLATE,
) -> str:
    """Builds a prompt for zero-shot single-label classification.

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    training_data : str
        training data to be used for few-shot learning
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels, training_data=training_data)


def build_zero_shot_prompt_mlc(
    x: str,
    labels: str,
    max_cats: Union[int, str],
    template: str = ZERO_SHOT_MLCLF_PROMPT_TEMPLATE,
) -> str:
    """Builds a prompt for zero-shot multi-label classification.

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    max_cats : Union[int,str]
        maximum number of categories to assign
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_MLCLF_PROMPT_TEMPLATE

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels, max_cats=max_cats)


def build_summary_prompt(
    x: str, max_words: Union[int, str], template: str = SUMMARY_PROMPT_TEMPLATE
) -> str:
    """Builds a prompt for text summarization.

    Parameters
    ----------
    x : str
        sample to summarize
    max_words : Union[int,str]
        maximum number of words to use in the summary
    template : str
        prompt template to use, must contain placeholders for all variables, by default SUMMARY_PROMPT_TEMPLATE

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, max_words=max_words)


def build_focused_summary_prompt(
    x: str,
    max_words: Union[int, str],
    focus: Union[int, str],
    template: str = FOCUSED_SUMMARY_PROMPT_TEMPLATE,
) -> str:
    """Builds a prompt for focused text summarization.

    Parameters
    ----------
    x : str
        sample to summarize
    max_words : Union[int,str]
        maximum number of words to use in the summary
    focus : Union[int,str]
        the topic(s) to focus on
    template : str
        prompt template to use, must contain placeholders for all variables, by default FOCUSED_SUMMARY_PROMPT_TEMPLATE

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, max_words=max_words, focus=focus)


def build_translation_prompt(
    x: str, output_language: str, template: str = TRANSLATION_PROMPT_TEMPLATE
) -> str:
    """Builds a prompt for text translation.

    Parameters
    ----------
    x : str
        sample to translate
    output_language : str
        language to translate to
    template : str
        prompt template to use, must contain placeholders for all variables, by default TRANSLATION_PROMPT_TEMPLATE

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, output_language=output_language)
