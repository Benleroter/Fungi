def EditedQParams(QParams):
	EQP = {}
	for q in list(QParams):
		if QParams[q] == '' or QParams[q] == 'None' or QParams[q] == 'value' or QParams[q] == 'initial':
			del QParams[q]

	return QParams