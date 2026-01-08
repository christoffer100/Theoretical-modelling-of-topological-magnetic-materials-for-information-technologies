include ../rspthome

../atomdens: atomdens.form element_77.a element_26.up element_46.b
	stick atomdens.form >$(@)

element_77.a: data_77.a
	cp data_77.a atom.data; $(RSPTHOME)/bin/atom; mv atom.dens $(@)
	mv atom.out out_77.a; mv wavef_chars radii_77.a; rm -f j* atom.data wavef*

element_26.up: data_26.up
	cp data_26.up atom.data; $(RSPTHOME)/bin/atom; mv atom.dens $(@)
	mv atom.out out_26.up; mv wavef_chars radii_26.up; rm -f j* atom.data wavef*

element_46.b: data_46.b
	cp data_46.b atom.data; $(RSPTHOME)/bin/atom; mv atom.dens $(@)
	mv atom.out out_46.b; mv wavef_chars radii_46.b; rm -f j* atom.data wavef*

