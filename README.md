# information_gain_and_entropy_decision_tree
Calculate the entropy and information of a decision tree for <b> binary classification</b>
Although Sophisticated machine learning Algorithm are able to calculate decision trees hyperparameters sucha as entropy and gain, knowing how to calculate that manually or programmatically helps understanding what is going on behind the black box machine learning libraries.

<b> Inputs of the code: </b>

<b> Total_left</b> = Total Number of instances in the left branch
<b> Nclass_left</b> = Number of instances in the <b>minimum class</b> of the left branch. If we have only one class, then the minimum is the number of instances in that class. If we have two equal classes, then the minimum is the number of instances in either class.

<b> Total_right</b> = Total Number of instances in the right branch
<b> Nclass_right</b> = Number of instances in the minimum class of the right branch.  If we have only one class, then the minimum is the number of instances in that class. If we have two equal classes, then the minimum is the number of instances in either class.

<b> Nclass_parent</b>= Number of instances in the <b>minimum class of the parent</b>

