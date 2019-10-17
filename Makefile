%:      
	@:  

args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

action:
	@echo $(call args,defaultstring)

solve:
	@python src/8queen2dimax.py $(call args,not_found) | xargs -I{} ./minisat_static  {} out.txt ; python src/out28queen.py out.txt && cat final_answer.txt
   
clean:
	@rm out.txt ; rm final_answer.txt