########################### to check same values between 2 texts ########################################################
# def find_common_lines(text1, text2):
#     # Split texts into lines and remove duplicates by converting to sets
#     lines1 = set(text1.splitlines())
#     lines2 = set(text2.splitlines())
    
#     # Find the intersection of both sets, which gives the common lines
#     common_lines = lines1.intersection(lines2)
    
#     # Return the common lines as a list
#     return list(common_lines)

# # Sample inputs
# text1 = """
# curr_ses_endBy value changed:  -> App
# stopCharging value changed: False -> True
# externalStop value changed: False -> True
# externalChargeStop value changed: None -> 1
# stopCCS value changed: None -> True
# phs value changed: 7 -> 8
# phsCha value changed: 4 -> 2
# phsStop value changed: 1 -> 2
# pilot value changed: 4 -> 2
# ChargingComplete value changed: 0 -> 1
# curr_ses_endBy value changed: App -> 
# curr_ses_errMsg value changed: ERR_NO_SLAC: No SLAC from EV -> 
# curr_ses_id value changed: d907233c-d544-4868-8e86-e1851a49f641 -> 
# curr_ses_error value changed: 74 -> 0
# phs value changed: 8 -> 1
# phsAuth value changed: 2 -> 1
# phsCC value changed: 2 -> 1
# phsCha value changed: 2 -> 1
# phsPD value changed: 2 -> 1
# phsPre value changed: 2 -> 1
# phsStart value changed: 2 -> 1
# phsStop value changed: 2 -> 1
# pilot value changed: 2 -> 7
# EVRESSSOC value changed: 55 -> -1
# auth value changed: True -> False
# busy value changed: True -> False
# curr_ses_active value changed: True -> False
# testEV value changed: True -> False
# EVReady value changed: 1 -> 0
# pilot value changed: 7 -> 0
# """

# text2 = """
# curr_ses_errMsg value changed: ERR_NO_SLAC: No SLAC from EV -> 
# curr_ses_id value changed: 4266fe92-e5be-4e47-92c3-960a54731ea9 -> 
# curr_ses_error value changed: 74 -> 0
# evsestat value changed: 1 -> 5
# phs value changed: 7 -> 1
# phsAuth value changed: 2 -> 1
# phsCC value changed: 2 -> 1
# phsCha value changed: 4 -> 1
# phsPD value changed: 2 -> 1
# phsPre value changed: 2 -> 1
# phsStart value changed: 2 -> 1
# auth value changed: True -> False
# busy value changed: True -> False
# curr_ses_active value changed: True -> False
# needsUnplug value changed: False -> True
# testEV value changed: True -> False
# EVReady value changed: 1 -> 0
# pilot value changed: 4 -> 7
# evsestat value changed: 5 -> 1
# pilot value changed: 7 -> 0
# EVRESSSOC value changed: 31 -> -1
# needsUnplug value changed: True -> False
# """

# # Find and print common lines
# common_lines = find_common_lines(text1, text2)
# for line in common_lines:
#     print(line)

#######################################################################################################




########################### to check same values between 7 texts ########################################################
# def find_common_lines(*texts):
#     # Convert each text to a set of lines
#     sets_of_lines = [set(text.splitlines()) for text in texts]
    
#     # Find the intersection of all sets to get lines common to all texts
#     common_lines = set.intersection(*sets_of_lines)
    
#     # Return the common lines as a list
#     return list(common_lines)

# # Sample inputs
# text1 = """
# curr_ses_endBy value changed:  -> App
# stopCharging value changed: False -> True
# externalStop value changed: False -> True
# externalChargeStop value changed: None -> 1
# stopCCS value changed: None -> True
# phs value changed: 7 -> 8
# phsCha value changed: 4 -> 2
# phsStop value changed: 1 -> 2
# pilot value changed: 4 -> 2
# ChargingComplete value changed: 0 -> 1
# curr_ses_endBy value changed: App -> 
# curr_ses_errMsg value changed: ERR_NO_SLAC: No SLAC from EV -> 
# curr_ses_id value changed: d907233c-d544-4868-8e86-e1851a49f641 -> 
# curr_ses_error value changed: 74 -> 0
# phs value changed: 8 -> 1
# phsAuth value changed: 2 -> 1
# phsCC value changed: 2 -> 1
# phsCha value changed: 2 -> 1
# phsPD value changed: 2 -> 1
# phsPre value changed: 2 -> 1
# phsStart value changed: 2 -> 1
# phsStop value changed: 2 -> 1
# pilot value changed: 2 -> 7
# EVRESSSOC value changed: 55 -> -1
# auth value changed: True -> False
# busy value changed: True -> False
# curr_ses_active value changed: True -> False
# testEV value changed: True -> False
# EVReady value changed: 1 -> 0
# pilot value changed: 7 -> 0
# """

# text2 = """
# testEV value changed: True -> False
# curr_ses_errMsg value changed: ERR_NO_SLAC: No SLAC from EV -> 
# pilot value changed: 2 -> 7
# curr_ses_error value changed: 74 -> 0
# curr_ses_active value changed: True -> False
# busy value changed: True -> False
# pilot value changed: 7 -> 0
# """

# text3 = """
# busy value changed: True -> False
# curr_ses_errMsg value changed: ERR_NO_SLAC: No SLAC from EV -> 
# auth value changed: True -> False
# ChargingComplete value changed: 0 -> 1
# testEV value changed: True -> False
# phsPre value changed: 2 -> 1
# phsAuth value changed: 2 -> 1
# EVReady value changed: 1 -> 0
# phsStop value changed: 2 -> 1
# curr_ses_active value changed: True -> False
# phsStart value changed: 2 -> 1
# pilot value changed: 4 -> 2
# curr_ses_error value changed: 74 -> 0
# phsPD value changed: 2 -> 1
# curr_ses_endBy value changed: App -> 
# phsStop value changed: 1 -> 2
# externalStop value changed: False -> True
# phsCha value changed: 2 -> 1
# curr_ses_endBy value changed:  -> App
# phsCha value changed: 4 -> 2
# EVRESSSOC value changed: 55 -> -1
# stopCharging value changed: False -> True
# pilot value changed: 7 -> 0
# phsCC value changed: 2 -> 1
# """

# text4 = """
# pilot value changed: 7 -> 0
# externalStop value changed: False -> True
# curr_ses_endBy value changed: App -> 
# phsCC value changed: 2 -> 1
# testEV value changed: True -> False
# EVRESSSOC value changed: 55 -> -1
# EVReady value changed: 1 -> 0
# stopCharging value changed: False -> True
# phsPD value changed: 2 -> 1
# busy value changed: True -> False
# curr_ses_active value changed: True -> False
# curr_ses_endBy value changed:  -> App
# auth value changed: True -> False
# phsAuth value changed: 2 -> 1
# """

# text5 = """
# stopCharging value changed: False -> True
# phsCC value changed: 2 -> 1
# testEV value changed: True -> False
# externalStop value changed: False -> True
# curr_ses_active value changed: True -> False
# pilot value changed: 7 -> 0
# phsAuth value changed: 2 -> 1
# EVReady value changed: 1 -> 0
# busy value changed: True -> False
# phsPD value changed: 2 -> 1
# EVRESSSOC value changed: 55 -> -1
# auth value changed: True -> False
# """

# text6 = """
# phsStop value changed: 1 -> 2
# phsStop value changed: 2 -> 1
# EVReady value changed: 1 -> 0
# phsCC value changed: 2 -> 1
# auth value changed: True -> False
# pilot value changed: 4 -> 2
# pilot value changed: 2 -> 7
# phsPre value changed: 2 -> 1
# phsStart value changed: 2 -> 1
# curr_ses_active value changed: True -> False
# phsAuth value changed: 2 -> 1
# phsPD value changed: 2 -> 1
# busy value changed: True -> False
# ChargingComplete value changed: 0 -> 1
# testEV value changed: True -> False
# """

# text7 = """
# phsPD value changed: 2 -> 1
# phsPre value changed: 2 -> 1
# phsCC value changed: 2 -> 1
# busy value changed: True -> False
# curr_ses_error value changed: 74 -> 0
# testEV value changed: True -> False
# pilot value changed: 7 -> 0
# curr_ses_active value changed: True -> False
# auth value changed: True -> False
# EVReady value changed: 1 -> 0
# phsStart value changed: 2 -> 1
# curr_ses_errMsg value changed: ERR_NO_SLAC: No SLAC from EV -> 
# phsAuth value changed: 2 -> 1
# """

# # Find and print common lines across all texts
# common_lines = find_common_lines(text1, text2, text3, text4, text5, text6, text7)
# for line in common_lines:
#     print(line)

################################################################################################################





########################### to check different values between 2 texts ########################################################





def find_different_lines(text1, text2):
    # Split texts into lines and convert to sets for comparison
    lines1 = set(text1.splitlines())
    lines2 = set(text2.splitlines())
    
    # Find lines unique to each set
    unique_to_text1 = lines1 - lines2
    unique_to_text2 = lines2 - lines1
    
    # Format the output
    output_text1 = "\n".join(unique_to_text1)
    output_text2 = "\n".join(unique_to_text2)
    
    # Return formatted output
    print(f"text different in text 1:\n{output_text1}")
    print(f"text different in text 2:\n{output_text2}")

# Sample inputs
text1 = """
curr_ses_endBy value changed:  -> App
stopCharging value changed: False -> True
externalStop value changed: False -> True
externalChargeStop value changed: None -> 1
stopCCS value changed: None -> True
phs value changed: 7 -> 8
phsCha value changed: 4 -> 2
phsStop value changed: 1 -> 2
pilot value changed: 4 -> 2
ChargingComplete value changed: 0 -> 1
curr_ses_endBy value changed: App -> 
curr_ses_errMsg value changed: ERR_NO_SLAC: No SLAC from EV -> 
curr_ses_id value changed: d907233c-d544-4868-8e86-e1851a49f641 -> 
curr_ses_error value changed: 74 -> 0
phs value changed: 8 -> 1
phsAuth value changed: 2 -> 1
phsCC value changed: 2 -> 1
phsCha value changed: 2 -> 1
phsPD value changed: 2 -> 1
phsPre value changed: 2 -> 1
phsStart value changed: 2 -> 1
phsStop value changed: 2 -> 1
pilot value changed: 2 -> 7
EVRESSSOC value changed: 55 -> -1
auth value changed: True -> False
busy value changed: True -> False
curr_ses_active value changed: True -> False
testEV value changed: True -> False
EVReady value changed: 1 -> 0
pilot value changed: 7 -> 0
"""

text2 = """
curr_ses_errMsg value changed: ERR_NO_SLAC: No SLAC from EV -> 
curr_ses_id value changed: 4266fe92-e5be-4e47-92c3-960a54731ea9 -> 
curr_ses_error value changed: 74 -> 0
evsestat value changed: 1 -> 5
phs value changed: 7 -> 1
phsAuth value changed: 2 -> 1
phsCC value changed: 2 -> 1
phsCha value changed: 4 -> 1
phsPD value changed: 2 -> 1
phsPre value changed: 2 -> 1
phsStart value changed: 2 -> 1
auth value changed: True -> False
busy value changed: True -> False
curr_ses_active value changed: True -> False
needsUnplug value changed: False -> True
testEV value changed: True -> False
EVReady value changed: 1 -> 0
pilot value changed: 4 -> 7
evsestat value changed: 5 -> 1
pilot value changed: 7 -> 0
EVRESSSOC value changed: 31 -> -1
needsUnplug value changed: True -> False
"""

# Find and print different lines
find_different_lines(text1, text2)

