# Six-Microbes-GPT2

### Independent Study in Machine Learning project


New language models like BERT have substantially raised SOTA metrics tracking a variety of tasks in NLP, particularly for question-answering. 
Central to the enhanced functionality of these models is the advent of masked language model architecture. 
Simply, these models understand words by encoding word vectors with data from surrounding words, in both directions. 
Various incremental improvements have since been made (permuting masks and increasing sliding window sizes), but the actual implications of computers understanding natural language are surprisingly few.
One area where new NLP presents great potential deals with knowledge querying, especially in domains either with little-known, repeating terminology, or large texts that build upon prior information.

While tools to this end are being developed to increase the pace of research in the sciences, the use of this technology to enhance student education remains unexplored completely.
Education presents a particularly good fit for this technology for a variety of reasons.
First, teachers often operate using similar terminologies accross levels of technical depth (i.e. what starts out as "adding fingers" later becomes "addition" and "summation").
Second, many classes are often differentiated solely by the corpus of textbooks and scientific papers selected for the session, so any technology that indexes this information well provides obvious benefits for students.
Finally, class data remains scattered accross a variety of drive and educational platforms, so a single source of truth for all class documentation could prove a useful tool for many professors.

The project here is an expanding domain question answer system, containing services to automatically collate, index, search, and acquire new information, using these new language models. 
One service provides a portal for aggregating and indexing PDF's provided in a class. 
As was found from testing this is hilarously useful for extracting information from readings in a human-like fashion, without actually having read them.
With every new reading, a PDF can be acquired and dropped into the portal, and the model will reread all the texts available to it and produce a new index efficiently.
Another service provides a search engine that can be used to acquire info from the index in natural language. This is where actual question-answering occurs.
A copy of the search engine, hosted separately, expands the domain of knowledge available to the former engine by piping a natural language query into google, reading the top 15 search results, and indexing them with provided texts.
There're also a variety of monitoring tools that were bundled with the actual deployment that provide visibility into which services are online, when knowledge finishes getting indexed (for search engine availability), and when the application connects to the internet.



Sometimes it does it well

![img1](https://github.com/ssreekanth2000/Six2-Microbes-GPT/blob/master/86272161_199320974595932_4155295273066692608_n.png)



Sometimes it does not

![img1](https://github.com/ssreekanth2000/Six2-Microbes-GPT/blob/master/84541315_314429449513948_2325187185432592384_n.png)
