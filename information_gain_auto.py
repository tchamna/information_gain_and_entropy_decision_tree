def information_gain_auto(Total_left,Nclass_left,Total_right,Nclass_right,Nclass_parent):

  # Total_left = int(input("Total Number of instances in the left branch: "))
  # Nclass_left = int(input("Number of instances in the minimum class of the left branch: "))

  # print("*"*60)

  # Total_right= int(input("Total Number of instances in the right branch: "))
  # Nclass_right = int(input("Number of instances in the minimum class of the right branch: "))

  # print("*"*60)

  # Nclass_parent = int(input("Number of instances in the minimum class of the parent: "))

  import numpy as np

  def entro(Nclass_parent_,Nclass_left_,Total_left_):
    p0 = Nclass_left_/Total_left_
    p0_parent = Nclass_parent_/Total_instances
    # p1 =  1-p0
    p1 = 1e-9 if 1-p0 == 0 else 1-p0
    p1_parent = 1e-9 if 1-p0_parent == 0 else 1-p0_parent


    # print("p0",p0)
    print("p0_parent",p0_parent)
    print("p1_parent",p1_parent)


    e = 0 if -p0*np.log2(p0)-p1*np.log2(p1) < 1e-6 else -p0*np.log2(p0)-p1*np.log2(p1)

    ep = 0 if -p0_parent*np.log2(p0_parent)-p1_parent*np.log2(p1_parent) < 1e-6 else -p0_parent*np.log2(p0_parent)-p1_parent*np.log2(p1_parent)
    # e = -p0*np.log2(p0)-p1*np.log2(p1)

    

    return e, ep


  def ig(ep,e,Node_instances_, Total_instances_):
    w0 = Node_instances_/Total_instances_
    w1 = 1 -w0
    weight_average_enthropy = w0*e[0]+w1*e[1]

    print("*"*60)

    print("weight_average_enthropy: ",weight_average_enthropy)
    gain = ep-weight_average_enthropy

    print("*"*60)

    print("Information Gain: ",gain)

    return gain

  # Nclass_left,Total_left = 13,17
  # Nclass_right, Total_right = 1,13

  # Nclass = Total_left
  Total_instances = Total_left + Total_right

  e_left,ep = entro(Nclass_parent,Nclass_left,Total_left)
  e_right,ep = entro(Nclass_parent,Nclass_right,Total_right)


  e = [e_left,e_right]
  # ep = entro(Nclass_parent,Nclass_parent,Total_instances)

  print("*"*60)
  print("entopy left:", e[0])
  print("*"*60)
  print("entopy right:", e[1])

  print("*"*60)
  print("entopy parent:", ep)



  IG = ig(ep,e,Total_left,Total_instances)
  

#Inputs:

# 1. Total_left = Total Number of instances in the left branch

# 2. Nclass_left = Number of instances in the minimum class of the left branch. If we have only one class, then the minimum is the number of instances in that class. If we have two equal classes, then the minimum is the number of instances in either class.

# 3. Total_right = Total Number of instances in the right branch

# 4. Nclass_right = Number of instances in the minimum class of the right branch. If we have only one class, then the minimum is the number of instances in that class. If we have two equal classes, then the minimum is the number of instances in either class.

# 5. Nclass_parent = Number of instances in the minimum class of the parent

information_gain_auto(3,1,2,1,2)


