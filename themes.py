import datetime
from llama_index.core import VectorStoreIndex, Document
from llama_index.core.output_parsers import LangchainOutputParser
from llama_index.llms.together import TogetherLLM
from llama_index.embeddings.together import TogetherEmbedding
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import json, os
import base64
from together.error import AuthenticationError
from together import Together
from langchain_core.exceptions import OutputParserException

def generate_image(prompt, filename):
    # Directly use the API key instead of getting it from environment variables
    api_key = "fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
    try:
        client = Together(api_key=api_key)
        response = client.images.generate(
            prompt=prompt,
            model="SG161222/Realistic_Vision_V3.0_VAE",
            width=1024,
            height=1024,
            steps=30,
            n=1,
            seed=-1
        )
        
        # Decode the base64 image and save it
        img_data = base64.b64decode(response.data[0].b64_json)
        golo =f"./static/generated/{filename}"
        with open(golo, 'wb') as f:
            f.write(img_data)
        
        return golo
    except AuthenticationError as e:
        print(f"Authentication Error: {e}")
        print("Please check your API key and ensure it's correct.")
        return None
    except Exception as e:
        print(f"An error occurred while generating the image: {e}")
        return None

import re

def get_youtube_embed_url(url):
    # Regular expression to match YouTube video IDs
    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)'
    
    # Extract the video ID
    match = re.search(pattern, url)
    if match:
        video_id = match.group(1)
        # Construct the embed URL
        embed_url = f'https://www.youtube.com/embed/{video_id}'
        return embed_url
    else:
        return None


def generate_content(doc_content, template='future', author='Anonymous', style='default', youtube_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"):
	template = template.lower()
	#EMBEDDED VERSION
	youtube_url = get_youtube_embed_url(youtube_url)

	if template == "future":
		document = Document(text=doc_content)
		embed_model = TogetherEmbedding(
			model_name="togethercomputer/m2-bert-80M-8k-retrieval",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)
		index = VectorStoreIndex.from_documents([document], embed_model=embed_model)

		response_schemas = [
			ResponseSchema(name="title", description="The main title of the blog post"),
			ResponseSchema(name="subtitle", description="A brief description or tagline for the blog post"),
			ResponseSchema(name="introduction", description="An introductory paragraph for the blog post"),
			ResponseSchema(name="main_points", description="A list of 5 main points or sections of the blog post, each explained in about 100 words"),
			ResponseSchema(name="conclusion", description="A concluding paragraph for the blog post"),
			ResponseSchema(name="image_descriptions", description="Descriptions for five images related to the content")
		]
		output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
		format_instructions = output_parser.get_format_instructions()

		llm = TogetherLLM(
			model="mistralai/Mixtral-8x7B-Instruct-v0.1",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)

		query_engine = index.as_query_engine(
			llm=llm,
			output_parser=LangchainOutputParser(output_parser),
		)

		response = query_engine.query(f"""Create a detailed and comprehensive blog post based on the given content. 
				The blog post should be at least 2000 words long, with 5 main points. 
				Provide in-depth explanations and examples for each point.
				{format_instructions}""")

		try:
			parsed_output = output_parser.parse(response.response)
		except json.JSONDecodeError as e:
			print(f"Error parsing JSON: {e}")
			print(f"Raw response: {response.response}")
			# Fallback to default values
			parsed_output = {
				"title": "Blog Post",
				"subtitle": "An interesting read",
				"introduction": "This is an introduction to the topic...",
				"main_points": ["Point 1", "Point 2", "Point 3", "Point 4", "Point 5"],
				"conclusion": "In conclusion...",
				"image_descriptions": ["A relevant image", "Another relevant image", "A third relevant image", "A fourth relevant image", "A fifth relevant image"]
			}
		print(parsed_output)
		# Generate images
		images = []
		for i, desc in enumerate(parsed_output["image_descriptions"]):
			print(desc)
		for i, desc in enumerate(parsed_output["image_descriptions"]):
			images.append(generate_image(desc, f"blog_image_{i}.png"))

		# Create mini posts content
		mini_posts = ''.join([f'''
			<article class="mini-post">
				<header>
					<h3><a href="#">{point[:30]}...</a></h3>
					<time class="published" datetime="{datetime.date.today().isoformat()}">{datetime.date.today().strftime('%B %d, %Y')}</time>
					<a href="#" class="author"><img src=".{images[i+1]}" alt="" /></a>
				</header>
				<a href="#" class="image"><img src=".{images[i+1]}" alt="" /></a>
			</article>
		''' for i, point in enumerate(parsed_output['main_points'][:4])])
		html_content = f"""
		<!DOCTYPE HTML>
		<html>
		<style>
		</style>
			<head>
				<title>{parsed_output['title']}</title>
				<meta charset="utf-8" />
				<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
				<link rel="stylesheet" href="assets/css/main.css" />
			</head>
			<body class="is-preload">

				<!-- Wrapper -->
					<div id="wrapper">

						<!-- Header -->
							<header id="header">
								<h1><a href="index.html">{parsed_output['title']}</a></h1>
								<nav class="links">
									<ul>
										<li><a href="#intro">Intro</a></li>
										<li><a href="#main-points">Main Points</a></li>
										<li><a href="#conclusion">Conclusion</a></li>
									</ul>
								</nav>
							</header>

						<!-- Main -->
							<div id="main">

								<!-- Post -->
									<article class="post">
										<header>
											<div class="title">
												<h2>{parsed_output['title']}</h2>
												<p>{parsed_output['subtitle']}</p>
											</div>
											<div class="meta">
												<time class="published" datetime="{datetime.date.today().isoformat()}">{datetime.date.today().strftime('%B %d, %Y')}</time>
												<a href="#" class="author"><span class="name">{author}</span><img src=".{images[0]}" alt="" /></a>
											</div>
										</header>
										<a href="#" class="image featured"><img src=".{images[0]}" alt="" /></a>
										<section id="intro">
											<h3>Introduction</h3>
											<p>{parsed_output['introduction']}</p>
										</section>
										<section id="main-points">
											<h3>Main Points</h3>
											{' '.join(f'<div><h4>Point {i+1}</h4><p>{point}</p></div>' for i, point in enumerate(parsed_output['main_points']))}
										</section>
										<section id="conclusion">
											<h3>Conclusion</h3>
											<p>{parsed_output['conclusion']}</p>
										</section>
										<section>
										<iframe  position: relative; width="560" height="315" src={youtube_url} 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>Website created based on this YouTube video</iframe>
										</section>
									</article>

							</div>

						<!-- Sidebar -->
							<section id="sidebar">

								<!-- Intro -->
									<section id="intro">
										<a href="#" class="logo"><img src=".{images[0]}" alt="" /></a>
										<header>
											<h2>{parsed_output['title']}</h2>
											<p>{parsed_output['subtitle']}</p>
										</header>
									</section>

								<!-- Mini Posts -->
									<section>
										<div class="mini-posts">
											{mini_posts}
										</div>
									</section>

								<!-- About -->
									<section class="blurb">
										<h2>About</h2>
										<p>{parsed_output['introduction'][:100]}...</p>
										<ul class="actions">
											<li><a href="#" class="button">Learn More</a></li>
										</ul>
									</section>

								<!-- Footer -->
									<section id="footer">
										<p class="copyright">&copy; {datetime.date.today().year} {author}. All rights reserved.</p>
									</section>

							</section>

					</div>
			</body>
		</html>
		"""
		return html_content

	elif template == 'editorial':
		document = Document(text=doc_content)
		embed_model = TogetherEmbedding(
			model_name="togethercomputer/m2-bert-80M-8k-retrieval",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)
		index = VectorStoreIndex.from_documents([document], embed_model=embed_model)

		response_schemas = [
			ResponseSchema(name="title", description="The main title of the blog post"),
			ResponseSchema(name="introduction", description="A brief introduction to the blog post"),
			ResponseSchema(name="subheading", description="Sub heading for the blog post"),
			ResponseSchema(name="subtitle", description="A brief description or tagline for the blog post"),
			ResponseSchema(name="content", description="The main content of the blog post, as a list of 4 text sections"),
			ResponseSchema(name="image_descriptions", description="Descriptions for 4 images related to the content, as a list of strings")
		]
		output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
		format_instructions = output_parser.get_format_instructions()

		llm = TogetherLLM(
			model="mistralai/Mixtral-8x7B-Instruct-v0.1",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)

		query_engine = index.as_query_engine(
			llm=llm,
			output_parser=LangchainOutputParser(output_parser),
		)

		response = query_engine.query(f"""Create a detailed and comprehensive blog post based on the given content. 
				The blog post should be at least 2000 words long, with 5 main points. 
				Provide in-depth explanations and examples for each point.
				{format_instructions}""")

		try:
			parsed_output = output_parser.parse(response.response)
		except OutputParserException as e:
			print(f"Error parsing output: {e}")
			# Provide default values
			parsed_output = {
				"title": "A Guide to Starting a Career in Tech",
				"intrdocution":"introduction about the blog",
				"subheading": "this can be a subheading for the blog",
				"subtitle": "Insights from industry professionals",
				"content": ["Section 1 content", "Section 2 content", "Section 3 content", "Section 4 content"],
				"image_descriptions": ["Tech workspace", "Coding on computer", "Team collaboration", "Tech innovation"]
			
			}

		# Ensure all expected keys are present
		expected_keys = ["title", "subtitle", "content", "image_descriptions", "introduction", "subheading"]
		for key in expected_keys:
			if key not in parsed_output:
				if key in ["content", "image_descriptions"]:
					parsed_output[key] = []
				else:
					parsed_output[key] = ""

		# Generate headings if content is present
		content_with_headings = []
		if parsed_output["content"]:
			for i, content in enumerate(parsed_output["content"]):
				heading_query = f"Generate a concise heading for the following content:\n\n{content[:200]}..."
				heading_response = query_engine.query(heading_query)
				content_with_headings.append({"heading": heading_response.response.strip(), "text": content})
		else:
			content_with_headings = [{"heading": f"Section {i+1}", "text": "Content unavailable"} for i in range(4)]

		# Generate images
		images = []
		for i, desc in enumerate(parsed_output["image_descriptions"][:4]):  # Limit to 4 images
			images.append(generate_image(desc, f"blog_image_{i}.png"))

		# Generate content HTML
		content_html = ""
		for section in content_with_headings:
			content_html += f"<h3>{section['heading']}</h3><p>{section['text']}</p>"
		html_content = f"""
		<!DOCTYPE HTML>
			<html>
			<style>
			</style>
				<head>
					<title>{parsed_output['title']}</title>
					<meta charset="utf-8" />
					<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
					<link rel="stylesheet" href="assets/css/main.css" />
				</head>
				<body class="is-preload">

					<!-- Wrapper -->
						<div id="wrapper">

							<!-- Main -->
								<div id="main">
									<div class="inner">

										<!-- Header -->
											<header id="header">
												<a href="index.html" class="logo"><strong>{parsed_output['title']}</strong> by {author}</a>
												<ul class="icons">
													<li><a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
													<li><a href="#" class="icon brands fa-facebook-f"><span class="label">Facebook</span></a></li>
													<li><a href="#" class="icon brands fa-snapchat-ghost"><span class="label">Snapchat</span></a></li>
													<li><a href="#" class="icon brands fa-instagram"><span class="label">Instagram</span></a></li>
													<li><a href="#" class="icon brands fa-medium-m"><span class="label">Medium</span></a></li>
												</ul>
											</header>

										<!-- Content -->
											<section>
												<header class="main">
													<h1>{parsed_output['title']}</h1>
												</header>

												<span class="image main"><img src=".{images[0]}" alt="" /></span>

												<p>{parsed_output['subtitle']}</p>

												{content_html}

											</section>

									</div>
								</div>

							<!-- Sidebar -->
								<div id="sidebar">
									<div class="inner">

										<!-- Search -->
											<section id="search" class="alt">
												<form method="post" action="#">
													<input type="text" name="query" id="query" placeholder="Search" />
												</form>
											</section>

										<!-- Menu -->
											<nav id="menu">
												<header class="major">
													<h2>Menu</h2>
												</header>
												<ul>
													<li><a href="index.html">Homepage</a></li>
													<li><a href="generic.html">Generic</a></li>
													<li><a href="elements.html">Elements</a></li>
												</ul>
											</nav>

										<!-- Section -->
											<section>
												<header class="major">
													<h2>Recent Posts</h2>
												</header>
												<div class="mini-posts">
													<article>
														<a href="#" class="image"><img src=".{images[1]}" alt="" /></a>
														<p>{content_with_headings[1]['heading']}</p>
													</article>
													<article>
														<a href="#" class="image"><img src=".{images[2]}" alt="" /></a>
														<p>{content_with_headings[2]['heading']}</p>
													</article>
													<article>
														<a href="#" class="image"><img src=".{images[3]}" alt="" /></a>
														<p>{content_with_headings[3]['heading']}</p>
													</article>
												</div>
												<ul class="actions">
													<li><a href="#" class="button">More</a></li>
												</ul>
											</section>
											<section><iframe  position: relative; width="400" height="315" src={youtube_url} 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>Website created based on this YouTube video</iframe></section>
												</section>

										<!-- Section -->
											<section>
												<header class="major">
													<h2>Get in touch</h2>
												</header>
												<p>If you have any questions or comments about this blog post, feel free to get in touch.</p>
												<ul class="contact">
													<li class="icon solid fa-envelope"><a href="#">information@example.com</a></li>
													<li class="icon solid fa-phone">(000) 000-0000</li>
													<li class="icon solid fa-home">1234 Somewhere Road #8254<br />
													Nashville, TN 00000-0000</li>
												</ul>
											</section>

										<!-- Footer -->
											<footer id="footer">
												<p class="copyright">&copy; {author}. All rights reserved. Design: <a href="https://html5up.net">HTML5 UP</a>.</p>
											</footer>

									</div>
								</div>

						</div>
				</body>
			</html>
			"""
		return html_content

	elif template == "reader":
		document = Document(text=doc_content)
		embed_model = TogetherEmbedding(
			model_name="togethercomputer/m2-bert-80M-8k-retrieval",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)
		index = VectorStoreIndex.from_documents([document], embed_model=embed_model)

		response_schemas = [
			ResponseSchema(name="title", description="The main title of the blog post"),
			ResponseSchema(name="introduction", description="introductory paragraph about the blog"),
			ResponseSchema(name="subtitle", description="A brief description or tagline for the blog post"),
			ResponseSchema(name="content", description="The main content of the blog post, as a list of 5 text sections"),
			ResponseSchema(name="image_descriptions", description="Descriptions for 4 images related to the content, as a list of strings")
		]
		output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
		format_instructions = output_parser.get_format_instructions()

		llm = TogetherLLM(
			model="mistralai/Mixtral-8x7B-Instruct-v0.1",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)

		query_engine = index.as_query_engine(
			llm=llm,
			output_parser=LangchainOutputParser(output_parser),
		)

		response = query_engine.query(f"""Create a detailed and comprehensive blog post based on the given content. 
				The blog post should be at least 2000 words long, with 5 main points. 
				Provide in-depth explanations and examples for each point.
				{format_instructions}""")

		try:
			parsed_output = output_parser.parse(response.response)
		except OutputParserException as e:
			print(f"Error parsing output: {e}")
			# Provide default values
			parsed_output = {
				"title": "A Guide to Starting a Career in Tech",
				"subtitle": "Insights from industry professionals",
				"content": ["Section 1 content", "Section 2 content", "Section 3 content", "Section 4 content"],
				"image_descriptions": ["image description 1", "image description 2", "image description 3", "image description 4"]
			}
		print(parsed_output)
		# Ensure all expected keys are present and have the correct type
		expected_keys = ["title", "subtitle", "content", "image_descriptions"]
		for key in expected_keys:
			if key not in parsed_output:
				if key in ["content", "image_descriptions"]:
					parsed_output[key] = []
				else:
					parsed_output[key] = ""

		# Generate headings if content is present
		content_with_headings = []
		if parsed_output["content"]:
			for i, content in enumerate(parsed_output["content"]):
				heading_query = f"Generate a concise heading for the following content:\n\n{content[:200]}..."
				heading_response = query_engine.query(heading_query)
				content_with_headings.append({"heading": heading_response.response.strip(), "text": content})
		else:
			content_with_headings = [{"heading": f"Section {i+1}", "text": "Content unavailable"} for i in range(5)]

		# Generate images
		images = []
		for i, desc in enumerate(parsed_output["image_descriptions"][:4]):  # Limit to 4 images
			images.append(generate_image(desc, f"blog_image_{i}.png"))
		print("Image Generated")

		while len(images) < 4:
			images.append("default_image.png")

		# Generate content HTML
		content_html = ""
		for section in content_with_headings:
			content_html += f"<h2>{section['heading']}</h2><p>{section['text']}</p>"

		# Generate image sections HTML
		image_sections = ""
		for i, (image, desc) in enumerate(zip(images, parsed_output["image_descriptions"])):
			image_sections += f"""
			<article>
				<a href="#" class="image"><img src=".{image}" alt="{desc}" /></a>
				<div class="inner">
					<p>{desc}</p>
				</div>
			</article>
			"""
		# HTML template using f-string
		html_content = f"""
		<!DOCTYPE HTML>
		<html>
		<style>
		</style>
			<head>
				<title>{parsed_output['title']}</title>
				<meta charset="utf-8" />
				<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
				<link rel="stylesheet" href="assets/css/main.css" />
			</head>
			<body class="is-preload">
				<section id="header">
					<header>
						<span class="image avatar"><img src=".{images[0]}" alt="" /></span>
						<h1 id="logo"><a href="#">{author}</a></h1>
						<p>{parsed_output['subtitle']}</p>
					</header>
					<nav id="nav">
						<ul>
							<li><a href="#one" class="active">About</a></li>
							<li><a href="#two">Main Content</a></li>
							<li><a href="#three">Images</a></li>
							<li><a href="#four">Contact</a></li>
						</ul>
					</nav>
					<footer>
						<ul class="icons">
							<li><a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
							<li><a href="#" class="icon brands fa-facebook-f"><span class="label">Facebook</span></a></li>
							<li><a href="#" class="icon brands fa-instagram"><span class="label">Instagram</span></a></li>
							<li><a href="#" class="icon brands fa-github"><span class="label">Github</span></a></li>
							<li><a href="#" class="icon solid fa-envelope"><span class="label">Email</span></a></li>
						</ul>
					</footer>
				</section>
				<div id="wrapper">
					<div id="main">
						<section id="one">
							<div class="image main" data-position="center">
								<img src=".{images[1]}" alt="" />
							</div>
							<div class="container">
								<header class="major">
									<h2>{parsed_output['title']}</h2>
									<p>{parsed_output['subtitle']}</p>
								</header>
								<p>{parsed_output['introduction']}</p>
							</div>
						</section>
						<section id="two">
							<div class="container">
								<h3>Main Content</h3>
								{content_html}
							</div>
						</section>
																																<iframe  position: relative; section style="display: flex; justify-content: right; align-items: right; flex-direction: column; height: 100%;"></section>><iframe  position: relative; style="text-align: right; "width="1200" height="600" src="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>Website created based on this YouTube video</iframe></section>
												</section>
							<div class="container">
								<h3>Images</h3>
								<div class="features">
									{image_sections}
								</div>
							</div>
						</section>
						<section><iframe width="560" height="315" src={youtube_url} 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>Website created based on this YouTube video</iframe></section>
						<section id="four">
							<div class="container">
								<h3>Contact Me</h3>
								<p>Get in touch for more information about {parsed_output['title']}.</p>
								<form method="post" action="#">
									<div class="row gtr-uniform">
										<div class="col-6 col-12-xsmall"><input type="text" name="name" id="name" placeholder="Name" /></div>
										<div class="col-6 col-12-xsmall"><input type="email" name="email" id="email" placeholder="Email" /></div>
										<div class="col-12"><input type="text" name="subject" id="subject" placeholder="Subject" /></div>
										<div class="col-12"><textarea name="message" id="message" placeholder="Message" rows="6"></textarea></div>
										<div class="col-12">
											<ul class="actions">
												<li><input type="submit" class="primary" value="Send Message" /></li>
												<li><input type="reset" value="Reset Form" /></li>
											</ul>
										</div>
									</div>
								</form>
							</div>
						</section>
					</div>
					<section id="footer">
						<div class="container">
							<ul class="copyright">
								<li>&copy; {author}. All rights reserved.</li>
							</ul>
						</div>
					</section>
				</div>
			</body>
		</html>
		"""

		return html_content


	elif template == 'arcana':
		document = Document(text=doc_content)
		embed_model = TogetherEmbedding(
			model_name="togethercomputer/m2-bert-80M-8k-retrieval",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)
		index = VectorStoreIndex.from_documents([document], embed_model=embed_model)

		response_schemas = [
			ResponseSchema(name="title", description="The main title of the blog post"),
			ResponseSchema(name="introduction", description="A brief introduction to the blog post"),
			ResponseSchema(name="subheading", description="Sub heading for the blog post"),
			ResponseSchema(name="subtitle", description="A brief description or tagline for the blog post"),
			ResponseSchema(name="content", description="The main content of the blog post, as a list of 4 text sections"),
			ResponseSchema(name="image_descriptions", description="Descriptions for 4 images related to the content, as a list of strings")
		]
		output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
		format_instructions = output_parser.get_format_instructions()

		llm = TogetherLLM(
			model="mistralai/Mixtral-8x7B-Instruct-v0.1",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)

		query_engine = index.as_query_engine(
			llm=llm,
			output_parser=LangchainOutputParser(output_parser),
		)

		response = query_engine.query(f"""Create a detailed and comprehensive blog post based on the given content. 
				The blog post should be at least 2000 words long, with 5 main points. 
				Provide in-depth explanations and examples for each point.
				{format_instructions}""")

		try:
			parsed_output = output_parser.parse(response.response)
		except OutputParserException as e:
			print(f"Error parsing output: {e}")
			# Provide default values
			parsed_output = {
				"title": "A Guide to Starting a Career in Tech",
				"intrdocution":"introduction about the blog",
				"subheading": "this can be a subheading for the blog",
				"subtitle": "Insights from industry professionals",
				"content": ["Section 1 content", "Section 2 content", "Section 3 content", "Section 4 content"],
				"image_descriptions": ["Tech workspace", "Coding on computer", "Team collaboration", "Tech innovation"]
			
			}

		# Ensure all expected keys are present
		expected_keys = ["title", "subtitle", "content", "image_descriptions", "introduction", "subheading"]
		for key in expected_keys:
			if key not in parsed_output:
				if key in ["content", "image_descriptions"]:
					parsed_output[key] = []
				else:
					parsed_output[key] = ""

		# Generate headings if content is present
		content_with_headings = []
		if parsed_output["content"]:
			for i, content in enumerate(parsed_output["content"]):
				heading_query = f"Generate a concise heading for the following content:\n\n{content[:200]}..."
				heading_response = query_engine.query(heading_query)
				content_with_headings.append({"heading": heading_response.response.strip(), "text": content})
		else:
			content_with_headings = [{"heading": f"Section {i+1}", "text": "Content unavailable"} for i in range(4)]

		# Generate images
		images = []
		for i, desc in enumerate(parsed_output["image_descriptions"][:4]):  # Limit to 4 images
			images.append(generate_image(desc, f"blog_image_{i}.png"))

		# Generate content HTML
		content_html = ""
		for section in content_with_headings:
			content_html += f"<h3>{section['heading']}</h3><p>{section['text']}</p>"
		html_content = f"""
		<!DOCTYPE HTML>
		<html>
		<style>
		</style>
			<head>
				<title>{parsed_output['title']}</title>
				<meta charset="utf-8" />
				<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
				<link rel="stylesheet" href="assets/css/main.css" />
			</head>
			<body class="is-preload">
				<div id="page-wrapper">
						<div id="header">
								<h1>{parsed_output['title']}</h1>
								<nav id="nav">
									<ul>
										<li>Home</a></li>
										<li>
											Dropdown
											<ul>
						
													Submenufc
					
												</li>
								
											</ul>
										</li>
										<li class="current"><a href="right-sidebar.html">Right Sidebar</a></li>
									</ul>
								</nav>

						</div>

					<!-- Main -->
						<section class="wrapper style1">
							<div class="container">
								<div class="row gtr-200">
									<div class="col-8 col-12-narrower">
										<div id="content">

											<!-- Content -->

												<article>
													<header>
														<h2>{parsed_output['title']}</h2>
														<p>{parsed_output['subtitle']}</p>
													</header>

													<span class="image featured"><img src=".{images[0]}" alt="" /></span>

													{content_html}

												</article>

										</div>
									</div>
									<div class="col-4 col-12-narrower">
										<div id="sidebar">

											<!-- Sidebar -->

												<section>
													<h3>{content_with_headings[1]['heading']}</h3>
													<p>{content_with_headings[1]['text']}</p>
													<footer>
														<a href="#" class="button">Continue Reading</a>
													</footer>
												</section>

												<section>
													<h3>Another Subheading</h3>
										<section><iframe width="560" height="315" src={youtube_url} 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>Website created based on this YouTube video</iframe></section>
												</section>

										</div>
									</div>
								</div>
							</div>
						</section>

					<!-- Footer -->
						<div id="footer">
							<div class="container">
								<div class="row">
									<section class="col-3 col-6-narrower col-12-mobilep">
										<h3>Links to Stuff(you can add)</h3>
										<ul class="links">
											<li><a href="#">Mattis et quis rutrum</a></li>
											<li><a href="#">Suspendisse amet varius</a></li>
										</ul>
									</section>
									<section class="col-6 col-12-narrower">
										<h3>Get In Touch with {author}</h3>
										<form>
											<div class="row gtr-50">
												<div class="col-6 col-12-mobilep">
													<input type="text" name="name" id="name" placeholder="Name" />
												</div>
												<div class="col-6 col-12-mobilep">
													<input type="email" name="email" id="email" placeholder="Email" />
												</div>
												<div class="col-12">
													<textarea name="message" id="message" placeholder="Message" rows="5"></textarea>
												</div>
												<div class="col-12">
													<ul class="actions">
														<li><input type="submit" class="button alt" value="Send Message" /></li>
													</ul>
												</div>
											</div>
										</form>
									</section>
								</div>
							</div>

							<!-- Icons -->
								<ul class="icons">
									<li><a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
									<li><a href="#" class="icon brands fa-facebook-f"><span class="label">Facebook</span></a></li>
									<li><a href="#" class="icon brands fa-github"><span class="label">GitHub</span></a></li>
									<li><a href="#" class="icon brands fa-linkedin-in"><span class="label">LinkedIn</span></a></li>
									<li><a href="#" class="icon brands fa-google-plus-g"><span class="label">Google+</span></a></li>
								</ul>


						</div>

				</div>

			</body>
		</html>
		"""
		return html_content
	

	elif template == 'hycuna':	
		document = Document(text=doc_content)
		embed_model = TogetherEmbedding(
			model_name="togethercomputer/m2-bert-80M-8k-retrieval",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)
		index = VectorStoreIndex.from_documents([document], embed_model=embed_model)

		response_schemas = [
			ResponseSchema(name="title", description="The main title of the blog post, make it short and catchy"),
			ResponseSchema(name="subtitle", description="A brief description or tagline for the blog post"),
			ResponseSchema(name="introduction", description="An introductory paragraph for the main content"),
			ResponseSchema(name="content", description="The main content of the blog post, as a list of 4 text sections"),
			ResponseSchema(name="sidebar_sections", description="Content for the sidebar, including headers and lists"),
			ResponseSchema(name="blurb", description="An informative text blurb for the footer"),
			ResponseSchema(name="image_descriptions", description="Descriptions for 4 images related to the content, as a list of strings"),
		]

		output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
		format_instructions = output_parser.get_format_instructions()

		llm = TogetherLLM(
			model="mistralai/Mixtral-8x7B-Instruct-v0.1",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)

		query_engine = index.as_query_engine(
			llm=llm,
			output_parser=LangchainOutputParser(output_parser),
		)

		response = query_engine.query(f"""Create a detailed and comprehensive blog post based on the given content. 
				The blog post should be at least 2000 words long, with 5 main points. 
				Provide in-depth explanations and examples for each point.
				{format_instructions}""")

		try:
			parsed_output = output_parser.parse(response.response)
		except OutputParserException as e:
			print(f"Error parsing output: {e}")
			# Provide default values
			parsed_output = {
				"title": "A Guide to Starting a Career in Tech",
				"intrdocution":"introduction about the blog",
				"subheading": "this can be a subheading for the blog",
				"subtitle": "Insights from industry professionals",
				"content": ["Section 1 content", "Section 2 content", "Section 3 content", "Section 4 content"],
				"image_descriptions": ["Tech workspace", "Coding on computer", "Team collaboration", "Tech innovation"]
			}

					# Ensure all expected keys are present
		expected_keys = ["title", "subtitle", "introduction","subheading", "content", "sidebar_sections", "footer_links", "blurb", "image_descriptions"]
		for key in expected_keys:
			if key not in parsed_output:
				parsed_output[key] = "" if key != "main_content" and key != "sidebar_sections" else []
		content_with_headings = []
		if parsed_output["content"]:
			for i, content in enumerate(parsed_output["content"]):
				heading_query = f"Generate a concise heading for the following content:\n\n{content[:200]}..."
				heading_response = query_engine.query(heading_query)
				content_with_headings.append({"heading": heading_response.response.strip(), "text": content})
		else:
			content_with_headings = [{"heading": f"Section {i+1}", "text": "Content unavailable"} for i in range(4)]
		images = []
		for i, desc in enumerate(parsed_output["image_descriptions"][:4]):  # Limit to 4 images
			images.append(generate_image(desc, f"blog_image_{i}.png"))
		content_html = ""
		for section in content_with_headings:
			content_html += f"<h2>{section['heading']}</h2><p>{section['text']}</p>"
		html_content = f"""
		<!DOCTYPE HTML>
		<html>
		<style>
		</style>
		<head>
			<title>{parsed_output['title']}</title>
			<meta charset="utf-8" />
			<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
			<link rel="stylesheet" href="assets/css/main.css" />
		</head>
		<body class="subpage">
			<div id="page-wrapper">

				<!-- Header -->
				<section id="header">
					<div class="container">
						<div class="row">
							<div class="col-12">
								<h1><a href="index.html" id="logo">{parsed_output['title']}</a></h1>S
							</div>
						</div>
					</div>
				</section>

				<!-- Content -->
				<section id="content">
					<div class="container">
						<div class="row">
							<div class="col-3 col-12-medium">
														<article>
																<a href="#" class="image"><img src=".{images[1]}" alt="" /></a>
																<p>{content_with_headings[1]['heading']}</p>
															</article>
															<article>
																<a href="#" class="image"><img src=".{images[2]}" alt="" /></a>
																<p>{content_with_headings[2]['heading']}</p>
															</article>
															<article>
																<a href="#" class="image"><img src=".{images[3]}" alt="" /></a>
																<p>{content_with_headings[3]['heading']}</p>
															</article>
							</div>
							<div class="col-9 col-12-medium imp-medium">

								<!-- Main Content -->
								<section>
									<header>
										<h2>{parsed_output['title']}</h2>
										<h3>{parsed_output['subtitle']}</h3>
									</header>
									<p>{parsed_output['introduction']}</p>
								<p>{parsed_output['subheading']}</p>
								{content_html}
								</section>
									<section><iframe width="560" height="315" src={youtube_url} 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>Website created based on this YouTube video</iframe></section>
												</section>
								
							</div>
						</div>
					</div>
				</section>

				<!-- Footer -->
				<section id="footer">
					<div class="container">
						<div class="row">
							<div class="col-8 col-12-medium">

								<!-- Links -->
								<section>
									<h2>Links to Important Stuff</h2>
									<div>
										<div class="row">
											{''.join([f"<div class='col-3 col-12-small'><ul class='link-list last-child'>{''.join([f'<li><a href=\"#\">{link}</a></li>' for link in parsed_output['footer_links'][i:i+4]])}</ul></div>" for i in range(0, len(parsed_output['footer_links']), 4)])}
										</div>
									</div>
								</section>
						</section>
									<section><iframe width="830" height="400" src=https://www.youtube.com/watch?v=dQw4w9WgXcQ 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>Website created based on this YouTube video</iframe></section>
												</section>
							</div>
							<div class="col-4 col-12-medium imp-medium">

								<!-- Blurb -->
								<section>
									<h2>An Informative Text Blurb</h2>
									<p>{parsed_output['blurb']}</p>
								</section>

							</div>
						</div>
					</div>
				</section>

			</div>
		</html>
		"""
		return html_content


	elif template == 'space':
		document = Document(text=doc_content)
		embed_model = TogetherEmbedding(
			model_name="togethercomputer/m2-bert-80M-8k-retrieval",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)
		index = VectorStoreIndex.from_documents([document], embed_model=embed_model)

		# Update the response schema to match the new template
		response_schemas = [
			ResponseSchema(name="intro_title", description="The title for the intro section"),
			ResponseSchema(name="intro_content", description="The content for the intro section"),
			ResponseSchema(name="one_title", description="Title for the first section"),
			ResponseSchema(name="one_content", description="Content for the first section"),
			ResponseSchema(name="two_title", description="Title for the second section"),
			ResponseSchema(name="two_content", description="Content for the second section"),
			ResponseSchema(name="three_title", description="Title for the third section"),
			ResponseSchema(name="three_content", description="Content for the third section"),
			ResponseSchema(name="contact_info", description="Contact information to be displayed"),
			ResponseSchema(name="image_descriptions", description="Descriptions for 4 images related to the content, as a list of strings"),
		]

		output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
		format_instructions = output_parser.get_format_instructions()

		llm = TogetherLLM(
			model="mistralai/Mixtral-8x7B-Instruct-v0.1",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)

		query_engine = index.as_query_engine(
			llm=llm,
			output_parser=LangchainOutputParser(output_parser),
		)

		response = query_engine.query(f"""Create a detailed and comprehensive blog post based on the given content. 
				The blog post should be at least 2000 words long, with 5 main points. 
				Provide in-depth explanations and examples for each point.
				{format_instructions}""")

		try:
			parsed_output = output_parser.parse(response.response)
		except OutputParserException as e:
			print(f"Error parsing output: {e}")
			# Provide default values
			parsed_output = {
				"intro_title": "Welcome to Hyperspace",
				"intro_content": "A brief introduction about the blog.",
				"one_title": "Who we are",
				"one_content": "Description about the team or company.",
				"two_title": "What we do",
				"two_content": "Details about the services or products.",
				"three_title": "Get in touch",
				"three_content": "Information on how to contact."}
			
		expected_keys = ["title", "subtitle", "introduction", "content", "sidebar_sections", "footer_links", "blurb", "image_descriptions"]
		for key in expected_keys:
			if key not in parsed_output:
				parsed_output[key] = "" if key != "main_content" and key != "sidebar_sections" else []
		
		images = []
		for i, desc in enumerate(parsed_output["image_descriptions"][:4]):  # Limit to 4 images
			images.append(generate_image(desc, f"blog_image_{i}.png"))
		html_content = f"""
		<!DOCTYPE HTML>
		<html>
		<style>
		</style>
			<head>
				<title>Exploring the Future of Creativity with AI: A New Era of Music, Video, and Image Generation</title>
				<meta charset="utf-8" />
				<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
				<link rel="stylesheet" href="assets/css/main.css" />
				<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
			</head>
			<body class="is-preload">
			
				<!-- Sidebar -->
				<section id="sidebar">
					<div class="inner">
						<nav>
							<ul>
								<li>Welcome</a></li>
								<li>{parsed_output['one_title']}</a></li>
								<li>{parsed_output['two_title']}</a></li>
								<li>{parsed_output['three_title']}</a></li>
							</ul>
						</nav>
					</div>
				</section>

				<!-- Wrapper -->
				<div id="wrapper">
			
					<!-- Intro -->
					<section class="wrapper">
								<div class="inner">
									<h1>{parsed_output['intro_title']}</h1>
									<p>{parsed_output['intro_content']}</p>
									<ul class="actions">
										<li><a href="#one" class="button scrolly">Learn more</a></li>
									</ul>
								</div>
					</section>
			
					<!-- One -->
					<section class="wrapper style2 spotlights">
						<section>
							<a href="#" class="image"><img src=".blog_image_0.png" alt="" data-position="center center" /></a>
						</section>
					</section>
			
					<!-- Two -->
					<section class="wrapper">
						<div class="inner">
							<h2>{parsed_output['one_title']}</h2>
							<p>{parsed_output['one_content']}</p>
						</div>
					</section>
			
					<!-- Veo -->
					<section class="wrapper style2 spotlights">
						<section>
							<a href="#" class="image"><img src=".blog_image_1.png" alt="" data-position="center center" /></a>
								
								
						</section>
					</section>

					<section class="wrapper">
						<div class="inner">
							<h2>{parsed_output['two_title']}</h2>
							<p>{parsed_output['two_content']}</p>
						</div>
					</section>
					<section class="wrapper style2 spotlights">
						<section>
							<a href="#" class="image"><img src=".blog_image_2.png" alt="" data-position="center center" /></a>
						</section>
					</section>
					<section class="wrapper">
						<div class="inner">
							<h2>{parsed_output['three_title']}</h2>
							<p>{parsed_output['three_content']}</p>
						</div>
					</section>
					<section><iframe width="560" height="315" src={youtube_url} 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>Website created based on this YouTube video</iframe></section>
												</section>
					<!-- Three -->
					<section id="three" class="wrapper">
						<div class="split style1">
							<section>
								<form method="post" action="#">
									<div class="fields">
										<div class="field half">
											<label for="name">Name</label>
											<input type="text" name="name" id="name" />
										</div>
										<div class="field half">
											<label for="email">Email</label>
											<input type="text" name="email" id="email" />
										</div>
										<div class="field">
											<label for="message">Message</label>
											<textarea name="message" id="message" rows="5"></textarea>
										</div>
									</div>
									<ul class="actions">
										<li><a href="" class="button submit">Send Message</a></li>
									</ul>
								</form>
							</section>
							<section>
								<ul class="contact">
									<li>
										<h3>Address</h3>
									</li>
									<li>
										<h3>Email</h3>
									</li>
									<li>
										<h3>Phone</h3>
									</li>
									<li>
										<h3>Social</h3>
										<ul class="icons">
											<!-- Social Icons Here -->
										</ul>
									</li>
								</ul>
							</section>
						</div>
					</section>
			
				</div>
			
				<!-- Footer -->
				<footer id="footer" class="wrapper style1-alt">
					<div class="inner">
						<!-- Footer Content Here -->
					</div>
				</footer>
			
			</body>
			</html>"""
		return html_content
	
	elif template == "strata":
		document = Document(text=doc_content)

		embed_model = TogetherEmbedding(
			model_name="togethercomputer/m2-bert-80M-8k-retrieval",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)

		# Step 2: Create Index and Response Schemas
		index = VectorStoreIndex.from_documents([document], embed_model=embed_model)

		response_schemas = [
			ResponseSchema(name="title", description="The main title of the blog post"),
			ResponseSchema(name="subtitle", description="A brief description or tagline for the blog post"),
			ResponseSchema(name="introduction", description="An introductory paragraph for the main content"),
			ResponseSchema(name="content", description="The main content of the blog post, as a list of 4 text sections"),
			ResponseSchema(name="blurb", description="An informative text blurb for the footer"),
			ResponseSchema(name="image_descriptions", description="Descriptions for 4 images related to the content, as a list of strings"),
		]

		output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
		format_instructions = output_parser.get_format_instructions()
		print("done")
		# Step 3: Setup LLM and Query Engine
		llm = TogetherLLM(
			model="mistralai/Mixtral-8x7B-Instruct-v0.1",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)

		query_engine = index.as_query_engine(
			llm=llm,
			output_parser=LangchainOutputParser(output_parser),
		)

		# Step 4: Query to generate the blog post
		response = query_engine.query(f"""Create a detailed and comprehensive blog post based on the given content. 
				The blog post should be at least 2000 words long, with 5 main points. 
				Provide in-depth explanations and examples for each point.
				{format_instructions}""")

		print(response)
		print()
		# Step 5: Handle Output Parsing
		try:
			print('what')
			parsed_output = output_parser.parse(response.response)
			print('what')
		except OutputParserException as e:
			print(f"Error parsing output: {e}")
			# Provide default values if there's an error in parsing
			parsed_output = {
				"title": "A Guide to Starting a Career in Tech",
				"introduction": "Introduction about the blog",
				"subtitle": "Insights from industry professionals",
				"content": ["Section 1 content", "Section 2 content", "Section 3 content", "Section 4 content"],
				"image_descriptions": ["Tech workspace", "Coding on computer", "Team collaboration", "Tech innovation"],
				"blurb": "An insightful note on the tech industry",
			}
		print(parsed_output)
		# Ensure all expected keys are present
		expected_keys = ["title", "subtitle", "introduction", "content", "blurb", "image_descriptions"]
		for key in expected_keys:
			if key not in parsed_output:
				parsed_output[key] = "" if key != "content" and key != "sidebar_sections" else []

		# Step 6: Generate Content with Headings
		content_with_headings = []
		if parsed_output["content"]:
			for i, content in enumerate(parsed_output["content"]):
				heading_query = f"Generate a concise heading for the following content:\n\n{content[:200]}..."
				heading_response = query_engine.query(heading_query)
				content_with_headings.append({"heading": heading_response.response.strip(), "text": content})
		else:
			content_with_headings = [{"heading": f"Section {i+1}", "text": "Content unavailable"} for i in range(4)]

		# Step 7: Generate Images

		images = []
		for i, desc in enumerate(parsed_output["image_descriptions"][:4]):  # Limit to 4 images
			images.append(generate_image(desc, f"blog_image_{i}.png"))

		# Step 8: Generate Content HTML
		content_html = ""
		for section in content_with_headings:
			content_html += f"<h2>{section['heading']}</h2><p>{section['text']}</p>"

		# Step 9: Replace HTML Template
		html_content = f"""
		<!DOCTYPE HTML>
		<html>
		<style>
		</style>
			<head>
				<title>{parsed_output['title']}</title>
				<meta charset="utf-8" />
				<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
				<link rel="stylesheet" href="assets/css/main.css" />
			</head>
			<body class="is-preload">

				<!-- Header -->
					<header id="header">
						<div class="inner">
							<a href="#" class="image avatar"><img src=".{images[0]}" alt="" /></a>
							<h1><strong>{parsed_output['title']}</strong><br />
							{parsed_output['subtitle']}</h1>
						</div>
					</header>

				<!-- Main -->
					<div id="main">

						<!-- One -->
							<section id="one">
								<header class="major">
									<h2>{content_with_headings[0]['heading']}</h2>
								</header>
								<p>{content_with_headings[0]['text']}</p>
								<ul class="actions">
									<li><a href="#" class="button">Learn More</a></li>
								</ul>
							</section>

						<!-- Two -->
							<section id="two">
								<h2>Recent Work</h2>
								<div class="row">
									<article class="col-6 col-12-xsmall work-item">
										<a href="{images[1]}" class="image fit thumb"><img src=".{images[1]}" alt="" /></a>
										<h3>{content_with_headings[1]['heading']}</h3>
										<p>{content_with_headings[1]['text']}</p>
									</article>
									<article class="col-6 col-12-xsmall work-item">
										<a href="{images[2]}" class="image fit thumb"><img src=".{images[2]}" alt="" /></a>
										<h3>{content_with_headings[2]['heading']}</h3>
										<p>{content_with_headings[2]['text']}</p>
									</article>
									<article class="col-6 col-12-xsmall work-item">
										<a href="{images[3]}" class="image fit thumb"><img src=".{images[3]}" alt="" /></a>
										<h3>{content_with_headings[3]['heading']}</h3>
										<p>{content_with_headings[3]['text']}</p>
									</article>
								</div>
								<section><iframe width="1000" height="600" src=https://www.youtube.com/watch?v=dQw4w9WgXcQ 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>Website created based on this YouTube video</iframe></section>
												</section>
								<ul class="actions">
									<li><a href="#" class="button">Full Portfolio</a></li>
								</ul>
							</section>

						<!-- Three -->
							<section id="three">
								<h2>Get In Touch</h2>
								<p>{parsed_output['blurb']}</p>
								<div class="row">
									<div class="col-8 col-12-small">
										<form method="post" action="#">
											<div class="row gtr-uniform gtr-50">
												<div class="col-6 col-12-xsmall"><input type="text" name="name" id="name" placeholder="Name" /></div>
												<div class="col-6 col-12-xsmall"><input type="email" name="email" id="email" placeholder="Email" /></div>
												<div class="col-12"><textarea name="message" id="message" placeholder="Message" rows="4"></textarea></div>
											</div>
										</form>
										<ul class="actions">
											<li><input type="submit" value="Send Message" /></li>
										</ul>
									</div>
									<div class="col-4 col-12-small">
										<ul class="labeled-icons">
											<li>
												<h3 class="icon solid fa-home"><span class="label">Address</span></h3>
												1234 Somewhere Rd.<br />
												Nashville, TN 00000<br />
												United States
											</li>
											<li>
												<h3 class="icon solid fa-mobile-alt"><span class="label">Phone</span></h3>
												000-000-0000
											</li>
											<li>
												<h3 class="icon solid fa-envelope"><span class="label">Email</span></h3>
												<a href="#">hello@untitled.tld</a>
											</li>
										</ul>
									</div>
								</div>
							</section>

					</div>

			</body>
		</html>
		"""
		return html_content
	
	elif template == "vintage":
				
		document = Document(text=doc_content)
		embed_model = TogetherEmbedding(
			model_name="togethercomputer/m2-bert-80M-8k-retrieval",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)
		index = VectorStoreIndex.from_documents([document], embed_model=embed_model)

		response_schemas = [
			ResponseSchema(name="title", description="The main title of the blog post"),
			ResponseSchema(name="subtitle", description="A brief description or tagline for the blog post"),
			ResponseSchema(name="introduction", description="An introductory paragraph for the main content"),
			ResponseSchema(name="content", description="The main content of the blog post, as a list of 4 text sections"),
			ResponseSchema(name="sidebar_sections", description="Content for the sidebar, including headers and lists"),
			ResponseSchema(name="image_descriptions", description="Descriptions for 4 images related to the content, as a list of strings"),
			ResponseSchema(name="blurb", description="An informative text blurb for the footer")
		]

		output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
		format_instructions = output_parser.get_format_instructions()

		llm = TogetherLLM(
			model="mistralai/Mixtral-8x7B-Instruct-v0.1",
			api_key="fb5107bddcd0f7f144ca41251d77bbb59f9f5f64cb21435473f15a2801d28d73"
		)

		query_engine = index.as_query_engine(
			llm=llm,
			output_parser=LangchainOutputParser(output_parser),
		)

		response = query_engine.query(f"""Create a detailed and comprehensive blog post based on the given content. 
				The blog post should be at least 2000 words long, with 5 main points. 
				Provide in-depth explanations and examples for each point.
				{format_instructions}""")

		try:
			parsed_output = output_parser.parse(response.response)
		except OutputParserException as e:
			print(f"Error parsing output: {e}")
			# Provide default values
			parsed_output = {
				"title": "A Guide to Starting a Career in Tech",
				"intrdocution":"introduction about the blog",
				"subheading": "this can be a subheading for the blog",
				"subtitle": "Insights from industry professionals",
				"content": ["Section 1 content", "Section 2 content", "Section 3 content", "Section 4 content"],
				"image_descriptions": ["Tech workspace", "Coding on computer", "Team collaboration", "Tech innovation"]
			}
		print(parsed_output)
		expected_keys = ["title", "subtitle", "introduction", "content", "sidebar_sections", "blurb", "image_descriptions"]
		for key in expected_keys:
			if key not in parsed_output:
				parsed_output[key] = "" if key != "main_content" and key != "sidebar_sections" else []
		content_with_headings = []
		if parsed_output["content"]:
			for i, content in enumerate(parsed_output["content"]):
				heading_query = f"Generate a concise heading for the following content:\n\n{content[:200]}..."
				heading_response = query_engine.query(heading_query)
				content_with_headings.append({"heading": heading_response.response.strip(), "text": content})
		else:
			content_with_headings = [{"heading": f"Section {i+1}", "text": "Content unavailable"} for i in range(4)]
		images = []
		for i, desc in enumerate(parsed_output["image_descriptions"][:4]):  # Limit to 4 images
			images.append(generate_image(desc, f"blog_image_{i}.png"))
		print("image generated")
		content_html = ""
		for section in content_with_headings:
			content_html += f"<h2>{section['heading']}</h2><p>{section['text']}</p>"
		html_content = f"""
		<!DOCTYPE HTML>
		<html>
		<style>
		</style>
    <head>
        <title>{parsed_output['title']}</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="assets/css/main.css" />
    </head>
    <body class="homepage is-preload">
        <div id="page-wrapper">

            <!-- Header -->
            <section id="header">
                <div class="container">

                    <!-- Logo -->
                    <h1 id="logo"><a href="index.html">{parsed_output['title']}</a></h1>
                    <p>{parsed_output['subtitle']}</p>

                    <!-- Nav -->
                    <nav id="nav">
                        <ul>
                            <li><a class="icon solid fa-home" href="index.html"><span>Introduction</span></a></li>
                            <li>

                            </li>
                            <li><a class="icon solid fa-cog"><span>Left Sidebar</span></a></li>
                            <li><a class="icon solid fa-retweet"><span>Right Sidebar</span></a></li>
                            <li><a class="icon solid fa-sitemap""><span>No Sidebar</span></a></li>
                        </ul>
                    </nav>

                </div>
            </section>

            <!-- Features -->
            <section id="features">
                <div class="container">
                    <header>
                        <h2>{parsed_output['title']}</h2>
                    </header>
                    <div class="row aln-center">
                        {''.join([
                            f'''
                            <div class="col-4 col-6-medium col-12-small">
                                <section>
                                    <a href="#" class="image featured"><img src=".{images[i]}" alt="" /></a>
                                    <header>
                                        <h3>{content_with_headings[i]['heading']}</h3>
                                    </header>
                                    <p>{content_with_headings[i]['text']}</p>
                                </section>
                            </div>
                            ''' for i in range(4)
                        ])}
                    </div>
                </div>
            </section>

            <!-- Banner -->
            <section id="banner">
                <div class="container">
                    <p>{parsed_output['blurb']}</p>
                </div>
            </section>

            <!-- Main -->
            <section id="main">
                <div class="container">
                    <div class="row">

                        <!-- Content -->
                        <div id="content" class="col-8 col-12-medium">

                            <!-- Post -->
                            <article class="box post">
                                <header>
                                    <h2>{content_with_headings[0]['heading']}</h2>
                                </header>
                                <a href="#" class="image featured"><img src="{images[0]}" alt="" /></a>
                                <p>{content_with_headings[0]['text']}</p>
                                <ul class="actions">
                                    <li><a href="#" class="button icon solid fa-file">Continue Reading</a></li>
                                </ul>
                            </article>
                                </ul>
							<section><iframe width="1000" height="600" src=https://www.youtube.com/watch?v=dQw4w9WgXcQ 
        title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>Website created based on this YouTube video</iframe></section>
							</section>

                        </div>

                        <!-- Sidebar -->
                        <div id="sidebar" class="col-4 col-12-medium">

                            <!-- Excerpts -->
                            <section>
                                <ul class="divided">
                                    {''.join([
                                        f'''
                                        <li>
                                            <article class="box excerpt">
                                                <header>
                                                    <span class="date">Section {i + 1}</span>
                                                    <h3><a href="#">{content_with_headings[i]['heading']}</a></h3>
                                                </header>
                                                <p>{content_with_headings[i]['text'][:150]}...</p>
                                            </article>
                                        </li>
                                        ''' for i in range(4)
                                    ])}
                                </ul>
                            </section>
														

                        </div>

                    </div>
                </div>
            </section>

            <!-- Footer -->
            <section id="footer">
                <div class="container">
                    <header>
                        <h2>Questions or comments? <strong>Get in touch:</strong></h2>
                    </header>
                    <div class="row">
                        <div class="col-6 col-12-medium">
                            <section>
                                <form method="post" action="#">
                                    <div class="row gtr-50">
                                        <div class="col-6 col-12-small">
                                            <input name="name" placeholder="Name" type="text" />
                                        </div>
                                        <div class="col-6 col-12-small">
                                            <input name="email" placeholder="Email" type="text" />
                                        </div>
                                        <div class="col-12">
                                            <textarea name="message" placeholder="Message"></textarea>
                                        </div>
                                        <div class="col-12">
                                            <ul class="actions">
                                                <li><input type="submit" value="Send Message" /></li>
                                            </ul>
                                        </div>
                                    </div>
                                </form>
                            </section>
                        </div>
                        <div class="col-6 col-12-medium">
                            <section>
                                <h3>Contact Information</h3>
                                <ul class="icons">
                                    <li><a href="#" class="icon solid fa-twitter"><span class="label">Twitter</span></a></li>
                                    <li><a href="#" class="icon solid fa-facebook"><span class="label">Facebook</span></a></li>
                                    <li><a href="#" class="icon solid fa-instagram"><span class="label">Instagram</span></a></li>
                                    <li><a href="#" class="icon solid fa-linkedin"><span class="label">LinkedIn</span></a></li>
                                </ul>
                            </section>
                        </div>
                    </div>
                </div>
            </section>

        </div>
    </body>
</html>
		"""
		return html_content
