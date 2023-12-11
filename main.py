def remove_virus(files):
  lst = files.split(':')
  files_on_pc = [i.strip() for i in lst[1].split(',')]
  processed = []
  for i in files_on_pc:
    name = i.split('.')[0]
    exp1 = 'virus' in name
    exp2 = 'malware' in name
    exp3 = name in ['antivirus', 'notvirus']
    if not(exp1 or exp2) or exp3:
        processed.append(i)
  if not processed:
    return f'{lst[0]}: Пусто'
  else:
    return f'{lst[0]}: {", ".join(processed)}'