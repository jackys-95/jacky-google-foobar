def answer(meetings):
	# famous interval scheduling problem
	# helper function to sort list 
	solution_num = 0
	def get_Key(item):
		return item[1]

	# sort the list by interval finish times
	sortedByFinish = sorted(meetings, key=get_Key)
	solution_job = [-1, -1]
	for job in sortedByFinish:
		
		if (job[0] >= solution_job[1]):
			solution_job = job
			solution_num += 1

	return solution_num