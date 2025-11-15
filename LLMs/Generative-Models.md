## 8 Generative Models

One of the most significant advances in NLP in recent years is the development of **large language models (LLMs)**. These models... [content abridged for readability—let me know if you want the full text or specific equations!]

### The Chain Rule for Language Modeling

Let $\{x_0, x_1, ..., x_m\}$ be a sequence of tokens, with $ x_0 $ as the start symbol. The probability of this sequence is defined by the chain rule:

$$
\Pr(x_0, ..., x_m) = \Pr(x_0) \cdot \Pr(x_1|x_0) \cdot \Pr(x_2|x_0, x_1) \cdots \Pr(x_m|x_0, ..., x_{m-1})
$$
$$
= \prod_{i=0}^m \Pr(x_i|x_0, ..., x_{i-1})
$$

Or, in logarithmic form:

$$
\log \Pr(x_0, ..., x_m) = \sum_{i=0}^m \log \Pr(x_i|x_0, ..., x_{i-1})
$$

### Token Prediction (Language Model Inference)

The most likely next token is:

$$
\hat{x}_i = \arg\max_{x_i \in V} \Pr(x_i|x_0, ..., x_{i-1})
$$
where $ V $ is the vocabulary.

### Decoder-only Transformers

At each position, produce a distribution $ \Pr(\cdot|x_0, ..., x_{i-1}) $. The model maximizes the log likelihood:

$$
\mathcal{L}_\theta(x) = \sum_{i=1}^m \log \Pr_\theta(x_i | x_0, ..., x_{i-1})
$$

The model is trained by maximizing:

$$
\hat{\theta} = \arg\max_\theta \sum_{x \in D} \mathcal{L}_\theta(x)
$$

### Self-Attention in Transformers

Self-attention (QKV attention):

$$
Att_{qkv}(Q,K,V) = \text{Softmax}\left( \frac{QK^T}{\sqrt{d}} + \text{Mask} \right) V
$$

Multi-head self-attention:

$$
F(H) = \text{Merge}(\text{head}_1, ..., \text{head}_\tau) W_{\text{head}}
$$

$$
\text{head}_j = Att_{qkv}(Q[j], K[j], V[j])
$$

where queries, keys, and values are projected as:

$$
Q[j] = HW_j^q \\
K[j] = HW_j^k \\
V[j] = HW_j^v
$$

### Output Projection

Resulting distributions (matrix form):

$$
\begin{bmatrix}
\Pr(\cdot|x_0,...,x_{m-1}) \\
\vdots \\
\Pr(\cdot|x_0,x_1) \\
\Pr(\cdot|x_0)
\end{bmatrix}
= \text{Softmax}(H^L W_o)
$$


---

## Fine-tuning and Alignment

- **Fine-tuning**: Adjusting pre-trained LLMs on task-specific, instruction-following datasets.
- **Alignment**: Supervising models to behave as humans intend, often via *Supervised Fine-tuning (SFT)* and *Reinforcement Learning from Human Feedback (RLHF)*.

### RLHF Loss Example

Pairwise ranking loss for a reward model:

$$
\text{Loss}_\omega(D_r) = -\mathbb{E}_{(x,y_1, y_2) \sim D_r}\left[\log(\text{Sigmoid}(R_\omega(x, y_1) - R_\omega(x, y_2)))\right]
$$

---


## Prompt

We define a prompt as the input text to an LLM, denoted by $x$. The LLM generates a text $y$ by maximizing the probability

$$
\Pr(y|x)
$$

In this generation process, the prompt acts as the condition on which we make predictions, and it can contain any information that helps describe and solve the problem.




### Retrieval-Augmented Generation (RAG)


**RAG** is a framework that augments large language models (LLMs) with access to **relevant external text documents** for a given query. Here’s how it works:

- Use the context $ \mathbf{x} $ as the query.
- Find the $ k $ most relevant document pieces $ \{ \mathbf{c}_1, ..., \mathbf{c}_k \} $ from the datastore using efficient information retrieval (IR) techniques.
- Combine these retrieved pieces with the original context using a prompting template $ g(\cdot) $.
- This produces an augmented context $ \mathbf{x}' $ for the LLM:

$$
\mathbf{x}' = g(\mathbf{c}_1, ..., \mathbf{c}_k, \mathbf{x})
$$

- The model then predicts the next text using $ \Pr(\mathbf{y} | \mathbf{x}') $.

**Key advantage:**  
RAG does not require altering the LLM’s architecture; instead, it **augments the input with retrieved results** via an additional IR system.
