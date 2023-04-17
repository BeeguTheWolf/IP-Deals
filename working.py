
# IP Deals

# User inputted variables
seller_name = input("Enter the Seller Name = ")
seller_name = str(seller_name)
buyer_name = input("Enter the Buyer Name = ")
buyer_name = str(buyer_name)
addy_of_sold = input("Enter the IP address being sold = ")
addy_of_sold = str(addy_of_sold)
purchase_price = input("Enter the Purchase Price = ")
purchase_price = float(purchase_price)
price_per_IP = input("Enter the Price Per IP = ")
price_per_IP = str(price_per_IP)
brokerCom = input("Enter the Broker Commission Percentage (10.5% = enter 10.5) = ")
brokerCom = float(brokerCom)
target_signing_date = input("Enter the Target Signing Date = ")
target_signing_date = str(target_signing_date)
target_closing_date = input("Enter the Target Closing Date = ")
target_closing_date = str(target_closing_date)
seller_ORG_ID = input("Enter the Seller ORG-ID = ")
seller_ORG_ID = str(seller_ORG_ID)
buyer_ORG_ID = input("Enter the Buyer ORG-ID = ")
buyer_ORG_ID = str(buyer_ORG_ID)
transfer_type = input("Enter the Transfer Type = ")
transfer_type = str(transfer_type)

seller_ticket_num = input("Enter the seller ticket number = ")

brokerCom_value = purchase_price * brokerCom
total_buyer_cost = brokerCom_value + purchase_price

brokerCom_value = str(brokerCom_value)
brokerCom = str(brokerCom)
purchase_price = str(purchase_price)

placeholders = {
    "var1": str(seller_name),
    "var2": str(buyer_name),
    "var3": str(addy_of_sold),
    "var4": str(purchase_price),
    "var5": str(price_per_IP),
    "var6": str(brokerCom),
    "var7": str(target_signing_date),
    "var8": str(target_closing_date),
    "var9": str(seller_ORG_ID),
    "var10": str(buyer_ORG_ID),
    "var11": str(transfer_type),
    "var12": str(seller_ticket_num)
}

# Open the text file template
with open("IPtemplate_draft.rtf", "r") as template_file:
    template_content = template_file.read()

# Replace the placeholders with the user inputted variables
template_content = template_content.replace("{{var1}}", placeholders["var1"])
template_content = template_content.replace("{{var2}}", placeholders["var2"])
template_content = template_content.replace("{{var3}}", placeholders["var3"])

# Create a new file with the filled-in template content
with open("filled_template.rtf", "w") as filled_template_file:
    filled_template_file.write(template_content)

# Print a success message
print("Filled-in template saved successfully!")
