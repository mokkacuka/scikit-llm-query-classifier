ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_CATEGORY = """
Act like a professional in the beauty industry.
You will be provided with the following information:
1. Search queries related to beauty. The list of search queries is delimited with triple backticks.
2. List of product categories the search queries can be assigned to. The list is delimited with square brackets. The skin concerns in the list are enclosed in single quotes and comma separated.

Perform the following tasks:
1. Identify the product category the provided search queries belong to with the highest probability. If the classification is not obvious, rather classify the category as *Unknown*.
2. Assign the provided search query to that product category (e.g. "mascara": Makeup).
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned concern. Do not provide any additional information except the JSON.

List of classes: {labels}

Text sample: ```{x}```

Your JSON response:
"""


ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM1 = """
Act like a professional in the skincare industry.
You will be provided with the following information:
1. Search queries related to skincare. The list of search queries is delimited with triple backticks.
2. List of skin concerns the search queries can be assigned to. The list is delimited with square brackets. The skin concerns in the list are enclosed in single quotes and comma separated.

Perform the following tasks:
1. Identify the skin concern the provided search queries belong to with the highest probability. If the classification is not obvious, rather classify the beauty concern as *This query is not related to any skin concern known*.
2. Assign the provided search query to that skin concern (e.g. "face cream": Unknown).
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned concern. Do not provide any additional information except the JSON.

List of classes: {labels}

Text sample: ```{x}```

Your JSON response:
"""

ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM2 = """
Act like a professional in the skincare industry.
You will be provided with the following information:
1. Search queries related to skincare. The list of search queries is delimited with triple backticks.
2. List of skincare ingredients or features the search queries can be assigned to. The list is delimited with square brackets. The skincare ingredients and features in the list are enclosed in single quotes and comma separated.

Perform the following tasks:
1. Identify the skincare ingredient or feature the provided search queries belong to with the highest probability. If the ingredient or feature is not directly mentioned in the query, rather don't infer and classify the ingredient as *This query is not related to any skincare ingredient or feature known*.
2. Assign the provided search query to that skincare ingredient or feature (e.g. "best vitamin c serum": Vitamin C).
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned concern. Do not provide any additional information except the JSON.

List of classes: {labels}

Text sample: ```{x}```

Your JSON response:
"""

ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM3 = """
Act like a professional in the skincare industry.
You will be provided with the following information:
1. Search queries related to skincare. The list of search queries is delimited with triple backticks.
2. List of skincare products the search queries can be assigned to. The list is delimited with square brackets. The skincare products in the list are enclosed in single quotes and comma separated.

Perform the following tasks:
1. Identify the skincare product the provided search queries belong to with the highest probability. If the product is not directly mentioned in the query, rather don't infer and classify the ingredient as *This query is not related to any skincare product known*.
2. Assign the provided search query to that skincare product (e.g. "best vitamin c serum": Serum).
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned concern. Do not provide any additional information except the JSON.

List of classes: {labels}

Text sample: ```{x}```

Your JSON response:
"""

ZERO_SHOT_CLF_PROMPT_TEMPLATE_SC_DIM4 = """
Act like a professional in the skincare industry.
You will be provided with the following information:
1. Search queries related to skincare. The list of search queries is delimited with triple backticks.
2. List of skincare advices or inspirations the search queries can be assigned to. The list is delimited with square brackets. The skincare advices or inspirations in the list are enclosed in single quotes and comma separated.

Perform the following tasks:
1. Identify the skincare advice or inspiration the provided search queries belong to with the highest probability. If the classification is not obvious, rather classify the concern as *This query is not related to any beauty advice or inspiration*.
2. Assign the provided search query to that skincare advice or inspiration (e.g. "best vitamin c serum": Best).
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned concern. Do not provide any additional information except the JSON.

List of classes: {labels}

Text sample: ```{x}```

Your JSON response:
"""

ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM1 = """
Act like a professional in the makeup industry.
You will be provided with the following information:
1. Search queries related to makeup. The list of search queries is delimited with triple backticks.
2. List of beauty concerns the search queries can be assigned to. The list is delimited with square brackets. The makeup concerns in the list are enclosed in single quotes and comma separated.

Perform the following tasks:
1. Identify the beauty concern the provided search queries belong to with the highest probability. If the classification is not obvious, rather classify the beauty concern as *This query is not related to any beauty concern*.
2. Assign the provided search query to that concern (e.g. "lip gloss": Unknown).
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned concern. Do not provide any additional information except the JSON.

List of classes: {labels}

Text sample: ```{x}```

Your JSON response:
"""

ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM2 = """
Act like a professional in the makeup industry.
You will be provided with the following information:
1. Search queries related to makeup. The list of search queries is delimited with triple backticks.
2. List of makeup ingredients or features the search queries can be assigned to. The list is delimited with square brackets. The ingredients and features in the list are enclosed in single quotes and comma separated.

Perform the following tasks:
1. Identify the makeup ingredient or feature the provided search queries belong to with the highest probability. If the classification is not obvious, rather classify the makeup ingredient or feature as *This query is not related to any makeup ingredient or feature known*.
2. Assign the provided search query to that ingredient or feature (e.g. "cream with hyaluronic acid": Hyaluronic Acid).
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned concern. Do not provide any additional information except the JSON.

List of classes: {labels}

Text sample: ```{x}```

Your JSON response:
"""

ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM3 = """
Act like a professional in the makeup industry.
You will be provided with the following information:
1. Search queries related to makeup. The list of search queries is delimited with triple backticks.
2. List of makeup products the search queries can be assigned to. The list is delimited with square brackets. The products in the list are enclosed in single quotes and comma separated.

Perform the following tasks:
1. Identify the makeup product the provided search queries belong to with the highest probability. If the classification is not obvious, rather classify the makeup product as *This query is not related to any makeup product known*.
2. Assign the provided search query to that product (e.g. "plumper lips": Unknown).
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned concern. Do not provide any additional information except the JSON.

List of classes: {labels}

Text sample: ```{x}```

Your JSON response:
"""

ZERO_SHOT_CLF_PROMPT_TEMPLATE_MU_DIM4 = """
Act like a professional in the makeup industry.
You will be provided with the following information:
1. Search queries related to makeup. The list of search queries is delimited with triple backticks.
2. List of makeup advice or inspirations the search queries can be assigned to. The list is delimited with square brackets. The advice or inspirations in the list are enclosed in single quotes and comma separated.

Perform the following tasks:
1. Identify the makeup advice or inspiration the provided search queries belong to with the highest probability. If the classification is not obvious, rather classify the makeup advice or inspiration as *This query is not related to any makeup advice or inspiration known*.
2. Assign the provided search query to that makeup advice or inspiration (e.g. "blush": Unknown).
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned concern. Do not provide any additional information except the JSON.

List of classes: {labels}

Text sample: ```{x}```

Your JSON response:
"""
