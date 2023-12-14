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

**Setup Cost**

Also referred to as Ordering Cost. It is a fixed cost incurred with each batch production or lot purchase. Its defining characteristic in modeling is that it remains constant, irrespective of the lot size Q. Accordingly, the total setup cost is solely based on the number of replenishments throughout the year.

If the demand for the year is D and we order lots of size Q, then we will have D over Q orders across the year.
Once we multiply this number by the setup cost factor, we get the total setup cost.

Total Setup Cost $= c_t\frac{D}{Q}$

But what are the fixed costs of ordering inventory?

Consider the resources invested in a purchase process: the buyer's time, communication expenses, the use of procurement software. There may also be potential paperwork and invoicing.

The transportation of the items might require fixed delivery rates, independent of the lot size.

Later, upon arrival, inventory incurs costs before it even hits the shelves. We're talking about material handling, preparation for storage, inspection, and the task of updating inventory records.

In practical situations, however, both receiving and transportation costs are influenced by the size of the lot. For instance, handling and transporting large quantities requires more labor than smaller lots. This implies that the ordering cost may have both a fixed and a variable element that escalates with Q.

$c_t = c_{t_v}*Q + c_{t_f}$

Notice that the Q in the variable component would be cancelled out. This is why per-unit costs like transportation and material handling were already included in the unit cost. However, this approach assumes that the variable factor does not benefit from economies of scale and remains constant for any lot size.

Now, in the context of manufacturing, fixed setup costs can also be multifaceted. For instance, the labor required for machine setup is a critical factor in the early stages of production runs. Reduced efficiency and quality often characterize the learning period for new production setups, representing another significant cost component. Furthermore, when a fully operational factory pauses the production of revenue-generating items for a new setup, substantial opportunity costs arise, highlighting the financial weight of these decisions.

**Holding Cost = $c_{e}\frac{Q}{2}$**

Holding Cost. Also known as carrying cost. Unlike the setup cost, the holding cost is determined based on the quantity or level of inventory ordered or produced in each lot, leading to different holding costs for varying lot sizes.

This difference is due to the cost concepts involved here. 

For instance: The money tied up in inventory or cost of capital. Capital is allocated to either purchase or produce inventory units, so less inventory means more available capital for alternative investments, each with their respective rates of return. Given that capital can be sourced from either equity or debt, the Weighted Average Cost of Capital is often used here, as it’s a blended measure for both sources of inventory financing.

Costs of Storage. Warehouse space often represents a significant expenditure, especially in prime locations. Handling and organizing within the storage space adds to the costs. Some inventory items might also necessitate special storage conditions, such as refrigeration or specific humidity levels, leading to additional expenses.

Sometimes, concepts such as perishability, shrinkage, insurance, or even taxation expenses are also included as part of the holding cost.

Given the complexity of these factors, the EOQ model attempts to amalgamate all these cost concepts into a single value, C sub E, which can be expressed, for instance, as a percentage of the unit value, C. This percentage is known as the 'holding rate.' Accordingly, the total holding cost is proportional to C sub E multiplied by the amount of inventory held during the year. So how much inventory is held during the year?

Recall that previously we stated that demand in the EOQ model is assumed to be constant throughout the year. This can also be interpreted as a steady rate of consumption or usage per unit time. Given this steady rate of consumption, when ordering or producing inventory in lots of size Q, the inventory level will naturally oscillate between the maximum of Q and a minimum of zero over the course of the year. Which means that items are not necessarily held for a whole year. So, to streamline calculations, the average inventory level over the year is typically used, which is taken as Q over 2.

**Closer look at the EOQ assumptions**

We are now closer to deriving the square root formula for the EOQ. But first, let's take a closer look at the EOQ model's assumptions. We have already established that demand should be known and constant, rather than random and variable; continuous, not occurring in discrete events. It should be accompanied by instantaneous or nearly instantaneous replenishment, not finite and variable. Items should be unaffected by quantity-based discounts and not specifically consider item perishability. The planning horizon is assumed to be infinite, as opposed to finite. This means that, despite using annual costs, the model assumes a perpetual policy, with no defined time limit. The review time for inventory should be continuous, as opposed to periodic. This implies that we can check the inventory level at any point in time. What kind of inventory tracking technology do you think this requires? There should not be explicit restrictions on order size or warehouse capacity, nor should planned backorders be allowed.

Note that we are not considering the potential costs of stockouts or shortages, as the model theoretically mitigates this risk. By operating under the premise of constant and known demand, ensuring timely replenishments, and disallowing backorders, we effectively negate the possibility of sudden stockouts.

It’s important to realize that the EOQ model is most effective when these conditions are met, but such scenarios are rare in real-world applications. Fortunately, the model can be modified to accommodate deviations from these assumptions, or we can leverage its insights to develop more advanced models better suited to those complexities.

## Total Cost Expression 

So let's continue with the Total Inventory Cost expression.

$TC = cD + c_t\frac{D}{Q} + c_e\frac{Q}{2}$

If we consider the individual costs and the demand as known parameters, and the order quantity Q as a variable, then the total cost of inventory is a function of Q.

$TC(Q) = cD + c_t\frac{D}{Q} + c_e\frac{Q}{2}$

Note that the material cost remains unaffected by changes in Q, and can be seen as a fixed cost in this regard. So, for the purpose of our analysis, we can exclude the material cost and focus solely on the costs that are relevant and influenced by Q. This leads us to the formulation of the Total Relevant Cost expression.

$TRC(Q) = c_t\frac{D}{Q} + c_e\frac{Q}{2}$

Let's plot the function to observe its behavior. As Q increases, the ordering or setup cost decreases, which is logical since larger lots result in fewer orders. Conversely, the holding cost increases with larger Q, leading to a higher average cost for the year, and therefore more capital and storage costs, as previously discussed.

We can visually observe that the total relevant cost appears to be the least when both cost components are roughly equal. To precisely understand this aspect and confirm our visual intuition, a basic understanding of calculus, specifically derivatives, is necessary. An in-depth exploration of derivatives could fill an entire video, so we won't delve into it here. For those unfamiliar with the concept, I recommend Three Blue One Brown's concise and intuitive series on the Essence of Calculus.

In a nutshell, derivatives help us determine the slope of tangent lines to a function. To minimize the total relevant cost, our focus is on identifying the specific tangent line with a slope of zero, as this indicates the function's minimum point.

## Formula derivation

So, by taking the derivative of the total relevant cost function and setting it equal to zero, we can find the specific Q that...

$TRC'(Q) = \frac{d}{dQ}\big(c_t\frac{D}{Q} + c_e\frac{Q}{2}\big)$

$0 = - c_t\frac{D}{Q^2} + \frac{c_e}{2}$

$\frac{c_e}{2} = c_t\frac{D}{Q^2}$ (This is the mathematical explanation of why the optimal or minimum cost is found when the ordering cost and the holding cost are the same.)

$Q^2 = \frac{2c_{t}D}{c_e}$

$Q = \sqrt{\frac{2c_{t}D}{c_e}}$

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