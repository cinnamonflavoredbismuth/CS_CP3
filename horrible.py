def mass_element():
  elements = {"H":"1","He":"2","Li":"3","Be":"4","B":"5","C":"6","N":"7","O":"8","F":"9","Ne":"10","Na":"11","Mg":"12","Al":"13","Si":"14","P":"15","S":"16","Cl":"17","Ar":"18","K":"19","Ca":"20","Sc":"21","Ti":"22","V":"23","Cr":"24","Mn":"25","Fe":"26","Co":"27","Ni":"28","Cu":"29","Zn":"30","Ga":"31","Ge":"32","As":"33","Se":"34","Br":"35","Kr":"36","Rb":"37","Sr":"38","Y":"39","Zr":"40","Nb":"41","Mo":"42","Tc":"43","Ru":"44","Rh":"45","Pd":"46","Ag":"47","Cd":"48","In":"49","Sn":"50","Sb":"51","Te":"52","I":"53","Xe":"54","Cs":"55","Ba":"56","La":"57","Ce":"58","Pr":"59","Nd":"60","Pm":"61","Sm":"62","Eu":"63","Gd":"64","Tb":"65","Dy":"66","Ho":"67","Er":"68","Tm":"69","Yb":"70","Lu":"71","Hf":"72","Ta":"73","W":"74","Re":"75","Os":"76","Ir":"77","Pt":"78","Au":"79","Hg":"80","Tl":"81","Pb":"82","Bi":"83","Po":"84","At":"85","Rn":"86","Fr":"87","Ra":"88","Ac":"89","Th":"90","Pa":"91","U":"92","Np":"93","Pu":"94","Am":"95","Cm":"96","Bk":"97","Cf":"98","Es":"99","Fm":"100","Md":"101","No":"102","Lr":"103","Rf":"104","Db":"105","Sg":"106","Bh":"107","Hs":"108","Mt":"109","Ds":"110","Rg":"111","Cn":"112","Nh":"113","Fl":"114","Mc":"115","Lv":"116","Ts":"117","Og":"118"};choices = input('What information do you have? Enter the numbers of the pieces of information you have:\n1. Proton amount\n2. Neutron amount\n3. Electron amount\n4. Mass\n5. Symbol\n6. Charge\n\n0. Exit\n  ');ne = 0;valid = '0123456'
  if choices is None:print('No input!');return mass_element()
  if not any(char in valid for char in choices) :print('Invalid input!\n\n');return mass_element()
  proton, neutrons, electrons, mass, symbol, charge = None, None, None, None, None, None
  while ne <=6:
    if "1" in choices:proton=int(input('Enter the number of protons: '));choices = choices.replace('1', '')
    elif "2" in choices:neutrons = int(input('Enter the number of neutrons: '));choices = choices.replace('2', '')
    elif "3" in choices:electrons = int(input('Enter the number of electrons'));choices = choices.replace('3', '')
    elif "4" in choices:mass = int(input('Enter the mass: '));choices = choices.replace('4', '')
    elif "5" in choices:symbol = input('Enter the atomic symbol: ');choices = choices.replace('5', '')
    elif "6" in choices:
      charge = input('Enter the charge (- for negative, + for positive, 0 for neutral): ');vld = ['-','+','0']
      if not any(char in vld for char in charge):
        print('Invalid input!');pass
      choices = choices.replace('6', '')
    elif "0" in choices:return
    else:pass
    ne += 1
  data_out = {"Protons": proton,"Neutrons": neutrons,"Electrons": electrons,"Mass": mass,"Symbol": symbol,"Charge": charge}
  if proton is not None:
    for key, value in elements.items():
      if int(value) == int(proton):data_out['Symbol'] = key;break
    data_out['Protons'] = str(proton)
  if neutrons is not None: data_out['Neutrons'] = neutrons; data_out['Mass'] = proton + neutrons if proton is not None else None
  elif neutrons is None and proton is not None and mass is not None:data_out['Neutrons'] = mass - proton
  if electrons is not None:data_out['Electrons'] = electrons
  if charge is not None:
    data_out['Charge'] = charge
    if electrons is None and proton is not None:data_out['Electrons'] = proton if charge =='0' else '< ' + str(proton) if charge == "+" else '> ' + str(proton) if charge == '-' else proton     
    elif proton is None and electrons is not None:data_out['Protons'] = electrons if charge == '0' else '< ' + str(electrons) if charge == '+' else '> ' + str(electrons) if charge == '-' else electrons     
  else: data_out['Charge'] =electrons - proton if electrons is not None and proton is not None else None
  for key, value in data_out.items():print(f"{key}: {value}") if value is not None else print(f"{key}: Unknown")
  print("\n\n")
  return mass_element()
mass_element()
