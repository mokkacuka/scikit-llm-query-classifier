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
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM1,
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM2,
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM3,
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM4,
    ZERO_SHOT_CLF_PROMPT_TEMPLATE_CATEGORY,
)

# TODO add validators

def build_zero_shot_prompt_slc_category(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_CATEGORY
) -> str:
    """Builds a prompt for zero-shot single-label classification (SC Category).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_CATEGORY

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)


def build_zero_shot_prompt_slc_sc_dim1(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM1
) -> str:
    """Builds a prompt for zero-shot single-label classification (SC Dimension 1).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM1

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)

def build_zero_shot_prompt_slc_sc_dim2(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM2
) -> str:
    """Builds a prompt for zero-shot single-label classification (SC Dimension 2).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM2

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)

def build_zero_shot_prompt_slc_sc_dim3(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM3
) -> str:
    """Builds a prompt for zero-shot single-label classification (SC Dimension 3).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM3

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)

def build_zero_shot_prompt_slc_sc_dim4(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM4
) -> str:
    """Builds a prompt for zero-shot single-label classification (SC Dimension 4).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM4

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)



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

def build_zero_shot_prompt_slc_ha_dim1(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM1
) -> str:
    """Builds a prompt for zero-shot single-label classification (HA Dimension 1).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM1

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)

def build_zero_shot_prompt_slc_ha_dim2(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM2
) -> str:
    """Builds a prompt for zero-shot single-label classification (HA Dimension 2).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM2

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)

def build_zero_shot_prompt_slc_ha_dim3(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM3
) -> str:
    """Builds a prompt for zero-shot single-label classification (HA Dimension 3).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM3

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)

def build_zero_shot_prompt_slc_ha_dim4(
    x: str, labels: str, template: str = ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM4
) -> str:
    """Builds a prompt for zero-shot single-label classification (HA Dimension 4).

    Parameters
    ----------
    x : str
        sample to classify
    labels : str
        candidate labels in a list-like representation
    template : str
        prompt template to use, must contain placeholders for all variables, by default ZERO_SHOT_CLF_PROMPT_TEMPLATE_HA_DIM4

    Returns
    -------
    str
        prepared prompt
    """
    return template.format(x=x, labels=labels)
