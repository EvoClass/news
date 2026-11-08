---
title: When One Proposal Is Not Enough: From Generated Answers to Ongoing Experiments
slug: ai999-evox-evolution-research-en
date: 2026-11-08
category: course
language: en
translation_key: ai999-evox-evolution-research
source_language: zh_CN
author_name: EvoClass
tags: ["AI999", "EvoX", "Evolutionary computation", "AI Native research"]
excerpt: Explore AI999 through the trade-offs in airfoil design, and see how parallel computation, meta-evolution and research validation support ongoing experiments.
cover_url: https://raw.githubusercontent.com/EvoClass/news/main/assets/news/ai999-candidate-evolution-v1.webp
cover_alt: Conceptual illustration: a researcher compares airfoil candidates along a red feedback path. Not measured aerodynamic data.
draft: false
---

If you want to improve an airfoil, what exactly does “better” mean?

Cruise efficiency matters, design constraints must be met, and every high-fidelity evaluation consumes part of the computational budget. One candidate may excel on a particular metric, while another leaves more room elsewhere. Putting them in a ranked list and picking the first is less straightforward than it might seem.

AI can help propose designs and write experimental code. The next challenge is how to evaluate, compare and keep exploring.

EvoClass's AI999, *EvoX Intelligent Evolution Systems and AI Native Research Practice*, follows this thread: from evolutionary computation to multi-objective problems, then to modern computational infrastructure, meta-evolution and research practice in an AI Native environment. It asks how a proposal enters an experiment, and how feedback changes the next proposal.

## First, define which improvements are worth keeping

[Lesson 3, “Real-World Complexity and Multi-Objective Trade-offs”](https://evoclass.ai/student/NwpWfDKqROGyROhyMm1syg/Lesson%203?content_language=zh_CN), uses airfoil design and other scenarios to examine the relationship between objectives, constraints and evaluation costs.

Some metrics are to be improved as much as possible; other requirements must meet a threshold. Distinguishing the two provides a basis for comparison.

If one candidate performs worse across all the metrics of interest, there is a reason to discard it. When several candidates offer different benefits and costs, keeping those differences can make the eventual choice clearer. Domain experts can then consider operating conditions and preferences when deciding which directions deserve further work.

This also prompts researchers to examine their evaluation procedure. How is an overall score calculated? Why were those weights chosen? Could a constraint omitted from the evaluation make a high-scoring proposal unusable?

Experimental design needs to address these questions. Otherwise, a search can keep improving its score while drifting away from the task that actually matters.

## As candidates multiply, where should the evaluation budget go?

Keeping several possibilities brings new costs.

Lesson 3 also discusses surrogate models: learning relationships between candidate parameters and performance from existing samples, using lower-cost predictions to aid screening, sending candidates that warrant closer inspection for higher-fidelity evaluation, and using those results to inform subsequent updates.

Different kinds of evidence carry different weight. Surrogate predictions have errors, and checks become especially important as a search enters unfamiliar regions. A promising predicted score still needs further examination.

Another cost comes from how computation is organized. [Lesson 4, “Modern Computational Infrastructure and Tensorized Parallel Evolution”](https://evoclass.ai/student/NwpWfDKqROGyROhyMm1syg/Lesson%204?content_language=zh_CN), examines how populations, evaluation results and state can be organized as tensors and processed in batches.

One way to understand this is to arrange many candidates' parameters in a consistent structure so that operations supporting batch execution can process them together. EvoX's [custom problem development documentation](https://evox.readthedocs.io/en/latest/tutorial/tutorial_part5.html) illustrates this organization through an evaluation interface that receives a batch of candidates and returns their objective values.

The actual benefit still needs to be measured. Is time being spent generating candidates, executing the objective function, or moving data? Does a larger batch consume too much GPU memory? Recording these costs separately helps identify what to change next.

Surrogate-assisted evaluation and batch parallelism address evaluation costs and computational organization, respectively. Understanding their roles is more useful than simply expecting more runs to produce better results.

## When search stalls, examine how candidates are generated

If more iterations bring little improvement, the candidates themselves are not the only thing worth examining.

How does mutation work? How are parameters set? Is the current search strategy suitable for this problem?

[Lesson 5, “Meta-Evolution: From Optimizing Solutions to Optimizing Algorithms Themselves”](https://evoclass.ai/student/NwpWfDKqROGyROhyMm1syg/Lesson%205?content_language=zh_CN), uses materials on MetaDE, AutoPSO and related methods to bring candidate-generation methods into the discussion.

In [MetaDE](https://github.com/EMI-Group/metade), for example, an inner differential evolution process solves the target problem, while an outer process searches strategy and parameter configurations based on their solving performance. Alongside comparing the solutions obtained, researchers can compare the ways those solutions are sought.

This additional layer also costs resources. Evaluation counts and runtime at both levels belong in the budget when methods are compared. Conclusions also need to be interpreted within the problems and conditions tested.

One exercise for learners is to establish a clear baseline, change one strategy, preserve configurations and complete results, and conduct repeated runs. This creates a basis for explaining changes in performance and noticing which modifications look impressive only in a single run.

## Once the code is written, what should research leave behind?

As AI takes part in implementing more experiments, researchers still have judgments to make.

[Lesson 6's discussion of Genesis and ongoing software evolution](https://evoclass.ai/student/NwpWfDKqROGyROhyMm1syg/Lesson%206?content_language=zh_CN) moves the focus to projects: how tasks are decomposed, how code changes are validated, and how useful results become a foundation for subsequent work. The [official Genesis project description](https://github.com/EMI-Group/genesis) likewise brings building, validation and continued development into the same workflow.

The conclusions supported by compilation and tests need to be distinguished from research conclusions. They can show that a program satisfies the requirements that have been checked. Whether a method is more effective also depends on the problem setup, comparative experiments, evaluation metrics and analysis of results.

[Lesson 7, “The AI Native Research Paradigm and Getting Started with EvoX”](https://evoclass.ai/student/NwpWfDKqROGyROhyMm1syg/Lesson%207?content_language=zh_CN), returns these responsibilities to the researcher: asking questions, defining evaluation, judging direction and critically examining results.

“Research taste” can become concrete here. Was a problem chosen because it matters, or because it makes attractive results easy to obtain? Can the evaluation test the claim being made? Could another researcher use the code, environment description, parameters and run records to examine the experiment again?

If you have begun using AI to write experimental code, start with a small problem whose results you can check yourself: write down objectives and constraints, establish a budget and baseline, then run, compare, record and decide what to keep for the next round. The [AI999 course overview](https://evoclass.ai/courses/NwpWfDKqROGyROhyMm1syg?lang=zh_CN) provides an entry point for continuing along this path.

Returning to the original set of airfoil candidates, the immediate outcome of research may be a set of evidence-based trade-offs: which proposals deserve to be kept, which need more evaluation, and which directions no longer merit further exploration.

When those judgments and their evidence can be carried into the next experiment, a proposal that is not yet good enough has a starting point for further improvement.

---

This course introduction is based on current EvoClass AI999 materials, with technical background drawn from the official project resources linked above. The airfoil discussion illustrates relationships between objectives and constraints. The suggested experimental arrangements are learning exercises, not performance evaluations conducted for this article. Lesson links lead to Simplified Chinese learning materials.
