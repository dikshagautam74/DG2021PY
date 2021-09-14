"""
    # CASE 1
    John expense in 1st Month
    Month 1   10000  -> spend
              10%    -> interest
              11000  -> amount with interest
    Month 2   3000   -> every month payment
    Month 3   3000
    Month 4   3000
    Month 5   2000
    # CASE 2
    John expense in 1st Month
    Month 1   10000
              10%
              11000
    Month 2   5000
              10%
              5500
              ----
              16500
              3000
    Month 3   3000
    Month 4   3000
    Month 5   2000
    1. Enter the fixed minimum payment amount (installment)
    2. to make an expense -> month will be taken care by algo
    3. to make a payment (fixed payment)
        give the forecast of the month where the bill will become 0
"""
amount_in_installment = int(input("Enter the fixed amount to be paid in every month in installments: "))
print("Amount in installment is :", amount_in_installment)

total = 0

months = ["month1", "month2", "month3", "month4", "month5", "month6", "month7","month8", "month9","month10","month11","month12"]

for month in months:

  print("Enter the amount spend in", month)
  spend_amount = int(input())
  print("Amount spent :", spend_amount)

  if spend_amount > 0:
    interest_amount = float(input("Interest on amount spend:"))

    interest_amount /= 12
    print(interest_amount)

    interest_amount *= spend_amount
    print("Interest on amount:", interest_amount)

    spend_amount += interest_amount
    print("You have to pay:", spend_amount)

    spend_amount = int(spend_amount)
    print("You have to pay:", spend_amount)


    total += spend_amount
    print("Total is:", total)


  elif spend_amount == 0:

    if total == 0:
      print("All clear in ",[month])
    elif total < 3000:
      print("Pay:",total)
      total = 0
      print("Now total is:", total)

    elif total > 3000:
      print("Pay:", amount_in_installment)
      total -= amount_in_installment
      print("Now total is:", total)
































