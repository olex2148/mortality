# mortality

Understanding the genetic and causal relationship between common health outcomes and
mortality.

The aim of this project is to understand what causes mortality by performing causal inference analysis (e.g. Mendelian
randomisation) using summary statistics from genome-wide association studies of mortality and other diseases and
outcomes. To examine this question, we will identify a list of outcomes of interest, and examine the genetic correlation
between these and mortality. We will then further perform causal inference using Mendelian randomization to distinguish
between correlation and causation among outcomes correlated with mortality. Additionally, gaining understanding of
machine learning methods required to do these analyses is also a goal of this project. The data will consist of GWAS
summary statistics from a mortality GWAS which used data from the UK biobank. The reason for using summary statistics
is that obtaining individual level genotype data from the UK biobank is infeasible for this project. Since we have GWAS
summary statistics, LD score regression is likely the method that will be used to do correlation analysis. For causal
inference a variety of tools and methods are available e.g., LCV and GSMR. Relevant theory and literature will be
discussed in assessing causality of mortality, yielding a statistical as well as a biologically reasonable basis for the
conclusion of the study to be drawn.

- The student should be able to describe some basics of statistical learning, such as linear regression, cross-validation, and measurements of prediction accuracies.
- The student should be able to describe fundamental genetics concepts such as heritability and genetic correlation.
- The student should be able to describe basics of causal inference and Mendelian randomization.
- The student should be able to estimate heritability and genetic correlations from GWAS summary statistics.
- The student should be able to perform Mendelian randomization using GWAS summary statistics.
- The student should be able to interpret the results and discuss their limitations.
