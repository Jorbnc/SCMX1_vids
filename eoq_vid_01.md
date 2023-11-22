- [Introduction to the Video](#introduction-to-the-video)
  - [Brief introduction of the EOQ](#brief-introduction-of-the-eoq)
  - [Explain the purpose of the video and what viewers will learn.](#explain-the-purpose-of-the-video-and-what-viewers-will-learn)
- [Brief History and Relevance](#brief-history-and-relevance)
- [The Economic Order Quantity](#the-economic-order-quantity)
  - [Inventory Costs](#inventory-costs)
  - [Total Cost Expression](#total-cost-expression)
  - [Formula derivation](#formula-derivation)
- [Practical Example](#practical-example)
  - [Provide a step-by-step example using real-life figures to calculate EOQ.](#provide-a-step-by-step-example-using-real-life-figures-to-calculate-eoq)
- [Applicability of EOQ](#applicability-of-eoq)
  - [Some comments](#some-comments)
  - [Scenarios where EOQ is particularly useful (e.g., stable demand).](#scenarios-where-eoq-is-particularly-useful-eg-stable-demand)
- [Limitations of the EOQ Model](#limitations-of-the-eoq-model)
  - [Costs and parameters are often estimations, because most accounting system don't report such concepts.](#costs-and-parameters-are-often-estimations-because-most-accounting-system-dont-report-such-concepts)
    - [Constant demand rate](#constant-demand-rate)
    - [Constant lead time](#constant-lead-time)
    - [No quantity discounts](#no-quantity-discounts)
    - [Only one product involved](#only-one-product-involved)
  - [Scenarios where EOQ may not be accurate (e.g., fluctuating demand).](#scenarios-where-eoq-may-not-be-accurate-eg-fluctuating-demand)
  - [Discuss how ignoring certain complexities can lead to suboptimal decisions.](#discuss-how-ignoring-certain-complexities-can-lead-to-suboptimal-decisions)
- [Sensitivity Analysis and Variations of the Model](#sensitivity-analysis-and-variations-of-the-model)
  - [What is sensitivity analysis and why it's important in the context of EOQ.](#what-is-sensitivity-analysis-and-why-its-important-in-the-context-of-eoq)
- [Explore variations of the EOQ model:](#explore-variations-of-the-eoq-model)
  - [Replenishment Lead Time \> 0](#replenishment-lead-time--0)
  - [Quantity Discounts](#quantity-discounts)
  - [EPQ](#epq)
  - [Allowance for backorders \& Planned backorders](#allowance-for-backorders--planned-backorders)
  - [Safety Stocks](#safety-stocks)
- [Advanced EOQ Models](#advanced-eoq-models)
  - [Briefly introduce more sophisticated inventory models that build on or modify the traditional EOQ formula.](#briefly-introduce-more-sophisticated-inventory-models-that-build-on-or-modify-the-traditional-eoq-formula)
- [Case Study](#case-study)
  - [Analyze a case study where EOQ has been successfully implemented.](#analyze-a-case-study-where-eoq-has-been-successfully-implemented)
  - [Discuss any adaptations made to the basic model in the case study.](#discuss-any-adaptations-made-to-the-basic-model-in-the-case-study)
- [Conclusion](#conclusion)
  - [Summarize the key points made in the video.](#summarize-the-key-points-made-in-the-video)
  - [Encourage the viewers to consider how EOQ could be relevant to their own business operations.](#encourage-the-viewers-to-consider-how-eoq-could-be-relevant-to-their-own-business-operations)
- [Call to Action](#call-to-action)
  - [Invite viewers to like, share, and subscribe.](#invite-viewers-to-like-share-and-subscribe)
  - [Prompt viewers to comment on how they might apply EOQ in their business or any questions they have.](#prompt-viewers-to-comment-on-how-they-might-apply-eoq-in-their-business-or-any-questions-they-have)
- [Additional Resources](#additional-resources)
  - [Provide links or references to further reading materials, tools, or software for EOQ calculation.](#provide-links-or-references-to-further-reading-materials-tools-or-software-for-eoq-calculation)
- [Credits](#credits)
  - [Acknowledge any contributions, references, or music used in the video.](#acknowledge-any-contributions-references-or-music-used-in-the-video)


# Introduction to the Video

## Brief introduction of the EOQ

The Economic Order Quantity (EOQ) stands as a cornerstone in Operations and Supply Chain Management. This analytical tool is designed to aid organizations in determining the optimal order size that minimizes the total costs associated with inventory, including both holding and ordering expenses. Due to its simplicity and effectiveness, the EOQ model is extensively taught as a core concept in introductory courses and widely featured in academic textbooks. It serves as a fundamental strategy for inventory optimization and a preliminary step towards developing more sophisticated inventory models and policies.

## Explain the purpose of the video and what viewers will learn.
<span style="color:green">Testing Color</span>

# Brief History and Relevance

In 1913, Ford Whitman Harris, an American Production Engineer, introduced the EOQ model through his paper *"How many parts to make at once?"*, published in *"Factory, The Magazine of Management"*.

His work emerged from his understanding of manufacturing processes and costs, emphasizing the need to balance the less visible inventory expenses, such as capital interest and depreciation, against the more apparent ordering or setup costs.

Following the initial publication, various adaptations of the EOQ formula were proposed.
However, Harris's fundamental approach remained the standard for order-quantity analysis for decades.

# The Economic Order Quantity

## Inventory Costs

Let's explore the cost concepts involved in the derivation of the basic EOQ model.

Whether in the form of raw materials, components, or final products, inventory will be required through a given period, for instance: one year. We will call this time frame the "unit time".

During this unit time, acquiring and maintaining inventory incurs specific costs essential for operational continuity. Accordingly, the Total Cost of inventory consists of:

**Material Cost = $cD$**

Represents the cumulative value of all required items, acquired either through procurement or production.

It's derived from the Unit Cost multiplied by the total demand over the unit time.

For merchants, the unit cost encompasses the purchase price from suppliers, plus any additional costs necessary for preparing the product for sale, such as packaging and labeling. It often also covers per-unit charges for freight transportation and material handling activities, like loading and unloading.

For producers, the unit cost extends beyond the mere calculation of raw materials. It encompasses the comprehensive unitary production cost, which includes direct labor and overheads.

Notice that there is a crucial assumption here: demand is represented by a single value, so it's said to be known and constant throughout the year. We will explore the ramifications of this assumption later.

**Total Setup Cost or Ordering Cost = $c_t\frac{D}{Q}$**

Foo

**Holding Cost = $c_{e}\frac{Q}{2}$**

Holding Costs, which include expenses for storing and managing inventory throughout the unit time.

Check SCMx1 PDF

## Total Cost Expression 
Introducing variable and fixed components in the ordering cost results a similar expression:

$TC = cD + (c_{t_v}Q + c_{t_{f}})\frac{D}{Q} + c_e\frac{Q}{2} = (c + c_{t_v})D + c_t\frac{D}{Q} + c_e\frac{Q}{2}$

that also includes variable transportation and material handling as "part of the $c$"

**Shortages:**

$TC = cD + c_e\frac{Q}{2} + c_t\frac{D}{Q} + c_sE[Units\;Short]$

but demand is deterministic, so we can get rid of the fourth component

## Formula derivation

$0 = \frac{c_e}{2} - c_t\frac{D}{Q^2} \implies Q=\sqrt{\frac{2c_{t}D}{c_e}}$

# Practical Example

## Provide a step-by-step example using real-life figures to calculate EOQ.
Foo

# Applicability of EOQ

## Some comments
<span style="color:green">(check the xlsx of eoq costs, there's a little eoq introduction and comments)</span> 

## Scenarios where EOQ is particularly useful (e.g., stable demand).
Foo

# Limitations of the EOQ Model

## Costs and parameters are often estimations, because most accounting system don't report such concepts.

So we have to update them. 

<span style="color:green">(parafrasis de Building Intuition. Insights... pag. 139)</span> 

<span style="color:green">(there must be AI solutions and so literature for this)</span> 

### Constant demand rate
Foo
### Constant lead time
Foo
### No quantity discounts
Foo
### Only one product involved
Foo
## Scenarios where EOQ may not be accurate (e.g., fluctuating demand).
## Discuss how ignoring certain complexities can lead to suboptimal decisions.

# Sensitivity Analysis and Variations of the Model

## What is sensitivity analysis and why it's important in the context of EOQ.
Sensitivity Analysis given the Square Root Formula:
$Q^{*} = \sqrt{\frac{2*D*c_s}{c_e}}$

- If warehousing costs $\uparrow \implies c_e  \implies Q^* \uparrow$
- If exogenous competitive products are introduced $\implies D \downarrow \implies Q^* \downarrow$

# Explore variations of the EOQ model:
## Replenishment Lead Time > 0
## Quantity Discounts
## EPQ
(introduces a rate of replenishment in $\frac{units}{time}$, i.e. production lead times)
## Allowance for backorders & Planned backorders
## Safety Stocks

# Advanced EOQ Models
## Briefly introduce more sophisticated inventory models that build on or modify the traditional EOQ formula.
Mention only:
- Wagner-Whitin Model
- Newsvendor
- Periodic Review
- Continuous Review
- Maybe a couple more
# Case Study

## Analyze a case study where EOQ has been successfully implemented.
## Discuss any adaptations made to the basic model in the case study.

# Conclusion

## Summarize the key points made in the video.
## Encourage the viewers to consider how EOQ could be relevant to their own business operations.

# Call to Action

## Invite viewers to like, share, and subscribe.
## Prompt viewers to comment on how they might apply EOQ in their business or any questions they have.

# Additional Resources

## Provide links or references to further reading materials, tools, or software for EOQ calculation.

# Credits

## Acknowledge any contributions, references, or music used in the video.