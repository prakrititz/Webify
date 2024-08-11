default_styles = {
    'future':{
        "default":"""
    @import url(fontawesome-all.min.css);
@import url("https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700|Raleway:400,800,900");
html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	@-ms-viewport {
		width: device-width;
	}

	body {
		-ms-overflow-style: scrollbar;
	}

	@media screen and (max-width: 480px) {

		html, body {
			min-width: 320px;
		}

	}

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #F6E96B;
	}

		body.is-preload *, body.is-preload *:before, body.is-preload *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

/* Type */

	body, input, select, textarea {
		color: #BEDC74;
		font-family: "Source Sans Pro", Helvetica, sans-serif;
		font-size: 14pt;
		font-weight: 400;
		line-height: 1.75;
	}

		@media screen and (max-width: 1680px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 1280px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 980px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 736px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 480px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

	a {
		-moz-transition: color 0.2s ease, border-bottom-color 0.2s ease;
		-webkit-transition: color 0.2s ease, border-bottom-color 0.2s ease;
		-ms-transition: color 0.2s ease, border-bottom-color 0.2s ease;
		transition: color 0.2s ease, border-bottom-color 0.2s ease;
		border-bottom: dotted 1px rgba(160, 160, 160, 0.65);
		color: inherit;
		text-decoration: none;
	}

		a:before {
			-moz-transition: color 0.2s ease;
			-webkit-transition: color 0.2s ease;
			-ms-transition: color 0.2s ease;
			transition: color 0.2s ease;
		}

		a:hover {
			border-bottom-color: transparent;
			color: #2ebaae !important;
		}

			a:hover:before {
				color: #2ebaae !important;
			}

	strong, b {
		color: #3c3b3b;
		font-weight: 700;
	}

	em, i {
		font-style: italic;
	}

	p {
		margin: 0 0 2em 0;
	}

	h1, h2, h3, h4, h5, h6 {
		color: #3c3b3b;
		font-family: "Raleway", Helvetica, sans-serif;
		font-weight: 800;
		letter-spacing: 0.25em;
		line-height: 1.65;
		margin: 0 0 1em 0;
		text-transform: uppercase;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			color: inherit;
			border-bottom: 0;
		}

	h2 {
		font-size: 1.1em;
	}

	h3 {
		font-size: 0.9em;
	}

	h4 {
		font-size: 0.7em;
	}

	h5 {
		font-size: 0.7em;
	}

	h6 {
		font-size: 0.7em;
	}

	sub {
		font-size: 0.8em;
		position: relative;
		top: 0.5em;
	}

	sup {
		font-size: 0.8em;
		position: relative;
		top: -0.5em;
	}

	blockquote {
		border-left: solid 4px rgba(160, 160, 160, 0.3);
		font-style: italic;
		margin: 0 0 2em 0;
		padding: 0.5em 0 0.5em 2em;
	}

	code {
		background: rgba(160, 160, 160, 0.075);
		border: solid 1px rgba(160, 160, 160, 0.3);
		font-family: "Courier New", monospace;
		font-size: 0.9em;
		margin: 0 0.25em;
		padding: 0.25em 0.65em;
	}

	pre {
		-webkit-overflow-scrolling: touch;
		font-family: "Courier New", monospace;
		font-size: 0.9em;
		margin: 0 0 2em 0;
	}

		pre code {
			display: block;
			line-height: 1.75em;
			padding: 1em 1.5em;
			overflow-x: auto;
		}

	hr {
		border: 0;
		border-bottom: solid 1px rgba(160, 160, 160, 0.3);
		margin: 2em 0;
	}

		hr.major {
			margin: 3em 0;
		}

	.align-left {
		text-align: left;
	}

	.align-center {
		text-align: center;
	}

	.align-right {
		text-align: right;
	}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0;
			margin-left: 0em;
		}

			.row.gtr-0 > * {
				padding: 0 0 0 0em;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0em;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0em;
				}

		.row.gtr-25 {
			margin-top: 0;
			margin-left: -0.25em;
		}

			.row.gtr-25 > * {
				padding: 0 0 0 0.25em;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -0.25em;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 0.25em;
				}

		.row.gtr-50 {
			margin-top: 0;
			margin-left: -0.5em;
		}

			.row.gtr-50 > * {
				padding: 0 0 0 0.5em;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -0.5em;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 0.5em;
				}

		.row {
			margin-top: 0;
			margin-left: -1em;
		}

			.row > * {
				padding: 0 0 0 1em;
			}

			.row.gtr-uniform {
				margin-top: -1em;
			}

				.row.gtr-uniform > * {
					padding-top: 1em;
				}

		.row.gtr-150 {
			margin-top: 0;
			margin-left: -1.5em;
		}

			.row.gtr-150 > * {
				padding: 0 0 0 1.5em;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -1.5em;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 1.5em;
				}

		.row.gtr-200 {
			margin-top: 0;
			margin-left: -2em;
		}

			.row.gtr-200 > * {
				padding: 0 0 0 2em;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -2em;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 2em;
				}

		@media screen and (max-width: 1680px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xlarge {
					order: -1;
				}

				.row > .col-1-xlarge {
					width: 8.33333%;
				}

				.row > .off-1-xlarge {
					margin-left: 8.33333%;
				}

				.row > .col-2-xlarge {
					width: 16.66667%;
				}

				.row > .off-2-xlarge {
					margin-left: 16.66667%;
				}

				.row > .col-3-xlarge {
					width: 25%;
				}

				.row > .off-3-xlarge {
					margin-left: 25%;
				}

				.row > .col-4-xlarge {
					width: 33.33333%;
				}

				.row > .off-4-xlarge {
					margin-left: 33.33333%;
				}

				.row > .col-5-xlarge {
					width: 41.66667%;
				}

				.row > .off-5-xlarge {
					margin-left: 41.66667%;
				}

				.row > .col-6-xlarge {
					width: 50%;
				}

				.row > .off-6-xlarge {
					margin-left: 50%;
				}

				.row > .col-7-xlarge {
					width: 58.33333%;
				}

				.row > .off-7-xlarge {
					margin-left: 58.33333%;
				}

				.row > .col-8-xlarge {
					width: 66.66667%;
				}

				.row > .off-8-xlarge {
					margin-left: 66.66667%;
				}

				.row > .col-9-xlarge {
					width: 75%;
				}

				.row > .off-9-xlarge {
					margin-left: 75%;
				}

				.row > .col-10-xlarge {
					width: 83.33333%;
				}

				.row > .off-10-xlarge {
					margin-left: 83.33333%;
				}

				.row > .col-11-xlarge {
					width: 91.66667%;
				}

				.row > .off-11-xlarge {
					margin-left: 91.66667%;
				}

				.row > .col-12-xlarge {
					width: 100%;
				}

				.row > .off-12-xlarge {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.25em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.25em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.25em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.25em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row {
					margin-top: 0;
					margin-left: -1em;
				}

					.row > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-uniform > * {
							padding-top: 1em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2em;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-large {
					order: -1;
				}

				.row > .col-1-large {
					width: 8.33333%;
				}

				.row > .off-1-large {
					margin-left: 8.33333%;
				}

				.row > .col-2-large {
					width: 16.66667%;
				}

				.row > .off-2-large {
					margin-left: 16.66667%;
				}

				.row > .col-3-large {
					width: 25%;
				}

				.row > .off-3-large {
					margin-left: 25%;
				}

				.row > .col-4-large {
					width: 33.33333%;
				}

				.row > .off-4-large {
					margin-left: 33.33333%;
				}

				.row > .col-5-large {
					width: 41.66667%;
				}

				.row > .off-5-large {
					margin-left: 41.66667%;
				}

				.row > .col-6-large {
					width: 50%;
				}

				.row > .off-6-large {
					margin-left: 50%;
				}

				.row > .col-7-large {
					width: 58.33333%;
				}

				.row > .off-7-large {
					margin-left: 58.33333%;
				}

				.row > .col-8-large {
					width: 66.66667%;
				}

				.row > .off-8-large {
					margin-left: 66.66667%;
				}

				.row > .col-9-large {
					width: 75%;
				}

				.row > .off-9-large {
					margin-left: 75%;
				}

				.row > .col-10-large {
					width: 83.33333%;
				}

				.row > .off-10-large {
					margin-left: 83.33333%;
				}

				.row > .col-11-large {
					width: 91.66667%;
				}

				.row > .off-11-large {
					margin-left: 91.66667%;
				}

				.row > .col-12-large {
					width: 100%;
				}

				.row > .off-12-large {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.25em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.25em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.25em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.25em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row {
					margin-top: 0;
					margin-left: -1em;
				}

					.row > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-uniform > * {
							padding-top: 1em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2em;
						}

		}

		@media screen and (max-width: 980px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-medium {
					order: -1;
				}

				.row > .col-1-medium {
					width: 8.33333%;
				}

				.row > .off-1-medium {
					margin-left: 8.33333%;
				}

				.row > .col-2-medium {
					width: 16.66667%;
				}

				.row > .off-2-medium {
					margin-left: 16.66667%;
				}

				.row > .col-3-medium {
					width: 25%;
				}

				.row > .off-3-medium {
					margin-left: 25%;
				}

				.row > .col-4-medium {
					width: 33.33333%;
				}

				.row > .off-4-medium {
					margin-left: 33.33333%;
				}

				.row > .col-5-medium {
					width: 41.66667%;
				}

				.row > .off-5-medium {
					margin-left: 41.66667%;
				}

				.row > .col-6-medium {
					width: 50%;
				}

				.row > .off-6-medium {
					margin-left: 50%;
				}

				.row > .col-7-medium {
					width: 58.33333%;
				}

				.row > .off-7-medium {
					margin-left: 58.33333%;
				}

				.row > .col-8-medium {
					width: 66.66667%;
				}

				.row > .off-8-medium {
					margin-left: 66.66667%;
				}

				.row > .col-9-medium {
					width: 75%;
				}

				.row > .off-9-medium {
					margin-left: 75%;
				}

				.row > .col-10-medium {
					width: 83.33333%;
				}

				.row > .off-10-medium {
					margin-left: 83.33333%;
				}

				.row > .col-11-medium {
					width: 91.66667%;
				}

				.row > .off-11-medium {
					margin-left: 91.66667%;
				}

				.row > .col-12-medium {
					width: 100%;
				}

				.row > .off-12-medium {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.25em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.25em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.25em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.25em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row {
					margin-top: 0;
					margin-left: -1em;
				}

					.row > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-uniform > * {
							padding-top: 1em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2em;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-small {
					order: -1;
				}

				.row > .col-1-small {
					width: 8.33333%;
				}

				.row > .off-1-small {
					margin-left: 8.33333%;
				}

				.row > .col-2-small {
					width: 16.66667%;
				}

				.row > .off-2-small {
					margin-left: 16.66667%;
				}

				.row > .col-3-small {
					width: 25%;
				}

				.row > .off-3-small {
					margin-left: 25%;
				}

				.row > .col-4-small {
					width: 33.33333%;
				}

				.row > .off-4-small {
					margin-left: 33.33333%;
				}

				.row > .col-5-small {
					width: 41.66667%;
				}

				.row > .off-5-small {
					margin-left: 41.66667%;
				}

				.row > .col-6-small {
					width: 50%;
				}

				.row > .off-6-small {
					margin-left: 50%;
				}

				.row > .col-7-small {
					width: 58.33333%;
				}

				.row > .off-7-small {
					margin-left: 58.33333%;
				}

				.row > .col-8-small {
					width: 66.66667%;
				}

				.row > .off-8-small {
					margin-left: 66.66667%;
				}

				.row > .col-9-small {
					width: 75%;
				}

				.row > .off-9-small {
					margin-left: 75%;
				}

				.row > .col-10-small {
					width: 83.33333%;
				}

				.row > .off-10-small {
					margin-left: 83.33333%;
				}

				.row > .col-11-small {
					width: 91.66667%;
				}

				.row > .off-11-small {
					margin-left: 91.66667%;
				}

				.row > .col-12-small {
					width: 100%;
				}

				.row > .off-12-small {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.25em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.25em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.25em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.25em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row {
					margin-top: 0;
					margin-left: -1em;
				}

					.row > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-uniform > * {
							padding-top: 1em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2em;
						}

		}

		@media screen and (max-width: 480px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xsmall {
					order: -1;
				}

				.row > .col-1-xsmall {
					width: 8.33333%;
				}

				.row > .off-1-xsmall {
					margin-left: 8.33333%;
				}

				.row > .col-2-xsmall {
					width: 16.66667%;
				}

				.row > .off-2-xsmall {
					margin-left: 16.66667%;
				}

				.row > .col-3-xsmall {
					width: 25%;
				}

				.row > .off-3-xsmall {
					margin-left: 25%;
				}

				.row > .col-4-xsmall {
					width: 33.33333%;
				}

				.row > .off-4-xsmall {
					margin-left: 33.33333%;
				}

				.row > .col-5-xsmall {
					width: 41.66667%;
				}

				.row > .off-5-xsmall {
					margin-left: 41.66667%;
				}

				.row > .col-6-xsmall {
					width: 50%;
				}

				.row > .off-6-xsmall {
					margin-left: 50%;
				}

				.row > .col-7-xsmall {
					width: 58.33333%;
				}

				.row > .off-7-xsmall {
					margin-left: 58.33333%;
				}

				.row > .col-8-xsmall {
					width: 66.66667%;
				}

				.row > .off-8-xsmall {
					margin-left: 66.66667%;
				}

				.row > .col-9-xsmall {
					width: 75%;
				}

				.row > .off-9-xsmall {
					margin-left: 75%;
				}

				.row > .col-10-xsmall {
					width: 83.33333%;
				}

				.row > .off-10-xsmall {
					margin-left: 83.33333%;
				}

				.row > .col-11-xsmall {
					width: 91.66667%;
				}

				.row > .off-11-xsmall {
					margin-left: 91.66667%;
				}

				.row > .col-12-xsmall {
					width: 100%;
				}

				.row > .off-12-xsmall {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.25em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.25em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.25em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.25em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row {
					margin-top: 0;
					margin-left: -1em;
				}

					.row > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-uniform > * {
							padding-top: 1em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2em;
						}

		}

/* Author */

	.author {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: row;
		-webkit-flex-direction: row;
		-ms-flex-direction: row;
		flex-direction: row;
		-moz-align-items: center;
		-webkit-align-items: center;
		-ms-align-items: center;
		align-items: center;
		-moz-justify-content: -moz-flex-end;
		-webkit-justify-content: -webkit-flex-end;
		-ms-justify-content: -ms-flex-end;
		justify-content: flex-end;
		border-bottom: 0;
		font-family: "Raleway", Helvetica, sans-serif;
		font-size: 0.6em;
		font-weight: 400;
		letter-spacing: 0.25em;
		text-transform: uppercase;
		white-space: nowrap;
	}

		.author .name {
			-moz-transition: border-bottom-color 0.2s ease;
			-webkit-transition: border-bottom-color 0.2s ease;
			-ms-transition: border-bottom-color 0.2s ease;
			transition: border-bottom-color 0.2s ease;
			border-bottom: dotted 1px rgba(160, 160, 160, 0.65);
			display: block;
			margin: 0 1.5em 0 0;
		}

		.author img {
			border-radius: 100%;
			display: block;
			width: 4em;
		}

		.author:hover .name {
			border-bottom-color: transparent;
		}

/* Blurb */

	.blurb h2 {
		font-size: 0.8em;
		margin: 0 0 1.5em 0;
	}

	.blurb h3 {
		font-size: 0.7em;
	}

	.blurb p {
		font-size: 0.9em;
	}

/* Box */

	.box {
		border: solid 1px rgba(160, 160, 160, 0.3);
		margin-bottom: 2em;
		padding: 1.5em;
	}

		.box > :last-child,
		.box > :last-child > :last-child,
		.box > :last-child > :last-child > :last-child {
			margin-bottom: 0;
		}

		.box.alt {
			border: 0;
			border-radius: 0;
			padding: 0;
		}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	button,
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease;
		-webkit-transition: background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease;
		-ms-transition: background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease;
		transition: background-color 0.2s ease, box-shadow 0.2s ease, color 0.2s ease;
		background-color: transparent;
		border: 0;
		box-shadow: inset 0 0 0 1px rgba(160, 160, 160, 0.3);
		color: #3c3b3b !important;
		cursor: pointer;
		display: inline-block;
		font-family: "Raleway", Helvetica, sans-serif;
		font-size: 0.6em;
		font-weight: 800;
		height: 4.8125em;
		letter-spacing: 0.25em;
		line-height: 4.8125em;
		padding: 0 2.5em;
		text-align: center;
		text-decoration: none;
		text-transform: uppercase;
		white-space: nowrap;
	}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		button:hover,
		.button:hover {
			box-shadow: inset 0 0 0 1px #2ebaae;
			color: #2ebaae !important;
		}

			input[type="submit"]:hover:active,
			input[type="reset"]:hover:active,
			input[type="button"]:hover:active,
			button:hover:active,
			.button:hover:active {
				background-color: rgba(46, 186, 174, 0.05);
			}

		input[type="submit"]:before, input[type="submit"]:after,
		input[type="reset"]:before,
		input[type="reset"]:after,
		input[type="button"]:before,
		input[type="button"]:after,
		button:before,
		button:after,
		.button:before,
		.button:after {
			color: #aaaaaa;
			position: relative;
		}

		input[type="submit"]:before,
		input[type="reset"]:before,
		input[type="button"]:before,
		button:before,
		.button:before {
			left: -1em;
			padding: 0 0 0 0.75em;
		}

		input[type="submit"]:after,
		input[type="reset"]:after,
		input[type="button"]:after,
		button:after,
		.button:after {
			left: 1em;
			padding: 0 0.75em 0 0;
		}

		input[type="submit"].fit,
		input[type="reset"].fit,
		input[type="button"].fit,
		button.fit,
		.button.fit {
			width: 100%;
		}

		input[type="submit"].large,
		input[type="reset"].large,
		input[type="button"].large,
		button.large,
		.button.large {
			font-size: 0.7em;
			padding: 0 3em;
		}

		input[type="submit"].small,
		input[type="reset"].small,
		input[type="button"].small,
		button.small,
		.button.small {
			font-size: 0.5em;
		}

		input[type="submit"].disabled, input[type="submit"]:disabled,
		input[type="reset"].disabled,
		input[type="reset"]:disabled,
		input[type="button"].disabled,
		input[type="button"]:disabled,
		button.disabled,
		button:disabled,
		.button.disabled,
		.button:disabled {
			pointer-events: none;
			color: rgba(160, 160, 160, 0.3) !important;
		}

			input[type="submit"].disabled:before, input[type="submit"]:disabled:before,
			input[type="reset"].disabled:before,
			input[type="reset"]:disabled:before,
			input[type="button"].disabled:before,
			input[type="button"]:disabled:before,
			button.disabled:before,
			button:disabled:before,
			.button.disabled:before,
			.button:disabled:before {
				color: rgba(160, 160, 160, 0.3) !important;
			}

/* Form */

	form {
		margin: 0 0 2em 0;
	}

		form.search {
			text-decoration: none;
			position: relative;
		}

			form.search:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			form.search:before {
				color: #aaaaaa;
				content: '\\f002';
				display: block;
				height: 2.75em;
				left: 0;
				line-height: 2.75em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.5em;
			}

			form.search > input:first-child {
				padding-left: 2.5em;
			}

	label {
		color: #3c3b3b;
		display: block;
		font-size: 0.9em;
		font-weight: 700;
		margin: 0 0 1em 0;
	}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	input[type="tel"],
	select,
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		background: rgba(160, 160, 160, 0.075);
		border: none;
		border: solid 1px rgba(160, 160, 160, 0.3);
		border-radius: 0;
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 1em;
		text-decoration: none;
		width: 100%;
	}

		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		input[type="tel"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		input[type="tel"]:focus,
		select:focus,
		textarea:focus {
			border-color: #2ebaae;
			box-shadow: inset 0 0 0 1px #2ebaae;
		}

	.select-wrapper {
		text-decoration: none;
		display: block;
		position: relative;
	}

		.select-wrapper:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 900;
		}

		.select-wrapper:before {
			color: rgba(160, 160, 160, 0.3);
			content: '\\f078';
			display: block;
			height: 2.75em;
			line-height: 2.75em;
			pointer-events: none;
			position: absolute;
			right: 0;
			text-align: center;
			top: 0;
			width: 2.75em;
		}

		.select-wrapper select::-ms-expand {
			display: none;
		}

	select {
		background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' preserveAspectRatio='none' viewBox='0 0 40 40'%3E%3Cpath d='M9.4,12.3l10.4,10.4l10.4-10.4c0.2-0.2,0.5-0.4,0.9-0.4c0.3,0,0.6,0.1,0.9,0.4l3.3,3.3c0.2,0.2,0.4,0.5,0.4,0.9 c0,0.4-0.1,0.6-0.4,0.9L20.7,31.9c-0.2,0.2-0.5,0.4-0.9,0.4c-0.3,0-0.6-0.1-0.9-0.4L4.3,17.3c-0.2-0.2-0.4-0.5-0.4-0.9 c0-0.4,0.1-0.6,0.4-0.9l3.3-3.3c0.2-0.2,0.5-0.4,0.9-0.4S9.1,12.1,9.4,12.3z' fill='rgba(160, 160, 160, 0.3)' /%3E%3C/svg%3E");
		background-size: 1.25rem;
		background-repeat: no-repeat;
		background-position: calc(100% - 1rem) center;
		height: 2.75em;
		padding-right: 2.75em;
		text-overflow: ellipsis;
	}

		select option {
			color: #3c3b3b;
			background: #ffffff;
		}

		select:focus::-ms-value {
			background-color: transparent;
		}

		select::-ms-expand {
			display: none;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 2.75em;
	}

	textarea {
		padding: 0.75em 1em;
	}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2em;
		opacity: 0;
		width: 1em;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			color: #646464;
			cursor: pointer;
			display: inline-block;
			font-size: 1em;
			font-weight: 400;
			padding-left: 2.4em;
			padding-right: 0.75em;
			position: relative;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				background: rgba(160, 160, 160, 0.075);
				border: solid 1px rgba(160, 160, 160, 0.3);
				content: '';
				display: inline-block;
				font-size: 0.8em;
				height: 2.0625em;
				left: 0;
				line-height: 2.0625em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.0625em;
			}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			background: #3c3b3b;
			border-color: #3c3b3b;
			color: #ffffff;
			content: '\\f00c';
		}

		input[type="checkbox"]:focus + label:before,
		input[type="radio"]:focus + label:before {
			border-color: #2ebaae;
			box-shadow: 0 0 0 1px #2ebaae;
		}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		color: #aaaaaa !important;
		opacity: 1.0;
	}

	:-moz-placeholder {
		color: #aaaaaa !important;
		opacity: 1.0;
	}

	::-moz-placeholder {
		color: #aaaaaa !important;
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		color: #aaaaaa !important;
		opacity: 1.0;
	}

/* Icon */

	.icon {
		text-decoration: none;
		border-bottom: none;
		position: relative;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 400;
		}

		.icon > .label {
			display: none;
		}

		.icon:before {
			line-height: inherit;
		}

		.icon.solid:before {
			font-weight: 900;
		}

		.icon.brands:before {
			font-family: 'Font Awesome 5 Brands';
		}

		.icon.suffix:before {
			float: right;
		}

/* Image */

	.image {
		border: 0;
		display: inline-block;
		position: relative;
	}

		.image img {
			display: block;
		}

		.image.left, .image.right {
			max-width: 40%;
		}

			.image.left img, .image.right img {
				width: 100%;
			}

		.image.left {
			float: left;
			padding: 0 1.5em 1em 0;
			top: 0.25em;
		}

		.image.right {
			float: right;
			padding: 0 0 1em 1.5em;
			top: 0.25em;
		}

		.image.fit {
			display: block;
			margin: 0 0 2em 0;
			width: 100%;
		}

			.image.fit img {
				width: 100%;
			}

		.image.featured {
			display: block;
			margin: 0 0 3em 0;
			width: 100%;
		}

			.image.featured img {
				width: 100%;
			}

			@media screen and (max-width: 736px) {

				.image.featured {
					margin: 0 0 1.5em 0;
				}

			}

		.image.main {
			display: block;
			margin: 0 0 3em 0;
			width: 100%;
		}

			.image.main img {
				width: 100%;
			}

/* List */

	ol {
		list-style: decimal;
		margin: 0 0 2em 0;
		padding-left: 1.25em;
	}

		ol li {
			padding-left: 0.25em;
		}

	ul {
		list-style: disc;
		margin: 0 0 2em 0;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
		}

		ul.alt {
			list-style: none;
			padding-left: 0;
		}

			ul.alt li {
				border-top: solid 1px rgba(160, 160, 160, 0.3);
				padding: 0.5em 0;
			}

				ul.alt li:first-child {
					border-top: 0;
					padding-top: 0;
				}

	dl {
		margin: 0 0 2em 0;
	}

		dl dt {
			display: block;
			font-weight: 700;
			margin: 0 0 1em 0;
		}

		dl dd {
			margin-left: 2em;
		}

/* Actions */

	ul.actions {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		cursor: default;
		list-style: none;
		margin-left: -1em;
		padding-left: 0;
	}

		ul.actions li {
			padding: 0 0 0 1em;
			vertical-align: middle;
		}

		ul.actions.special {
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 100%;
			margin-left: 0;
		}

			ul.actions.special li:first-child {
				padding-left: 0;
			}

		ul.actions.stacked {
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			margin-left: 0;
		}

			ul.actions.stacked li {
				padding: 1.3em 0 0 0;
			}

				ul.actions.stacked li:first-child {
					padding-top: 0;
				}

		ul.actions.fit {
			width: calc(100% + 1em);
		}

			ul.actions.fit li {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				width: 100%;
			}

				ul.actions.fit li > * {
					width: 100%;
				}

			ul.actions.fit.stacked {
				width: 100%;
			}

		@media screen and (max-width: 480px) {

			ul.actions:not(.fixed) {
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
				margin-left: 0;
				width: 100% !important;
			}

				ul.actions:not(.fixed) li {
					-moz-flex-grow: 1;
					-webkit-flex-grow: 1;
					-ms-flex-grow: 1;
					flex-grow: 1;
					-moz-flex-shrink: 1;
					-webkit-flex-shrink: 1;
					-ms-flex-shrink: 1;
					flex-shrink: 1;
					padding: 1em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions:not(.fixed) li > * {
						width: 100%;
					}

					ul.actions:not(.fixed) li:first-child {
						padding-top: 0;
					}

					ul.actions:not(.fixed) li input[type="submit"],
					ul.actions:not(.fixed) li input[type="reset"],
					ul.actions:not(.fixed) li input[type="button"],
					ul.actions:not(.fixed) li button,
					ul.actions:not(.fixed) li .button {
						width: 100%;
					}

						ul.actions:not(.fixed) li input[type="submit"].icon:before,
						ul.actions:not(.fixed) li input[type="reset"].icon:before,
						ul.actions:not(.fixed) li input[type="button"].icon:before,
						ul.actions:not(.fixed) li button.icon:before,
						ul.actions:not(.fixed) li .button.icon:before {
							margin-left: -0.5em;
						}

		}

/* Icons */

	ul.icons {
		cursor: default;
		list-style: none;
		padding-left: 0;
	}

		ul.icons li {
			display: inline-block;
			padding: 0 1em 0 0;
		}

			ul.icons li:last-child {
				padding-right: 0;
			}

			ul.icons li > * {
				border: 0;
			}

				ul.icons li > * .label {
					display: none;
				}

/* Posts */

	ul.posts {
		list-style: none;
		padding: 0;
	}

		ul.posts li {
			border-top: dotted 1px rgba(160, 160, 160, 0.3);
			margin: 1.5em 0 0 0;
			padding: 1.5em 0 0 0;
		}

			ul.posts li:first-child {
				border-top: 0;
				margin-top: 0;
				padding-top: 0;
			}

		ul.posts article {
			display: -moz-flex;
			display: -webkit-flex;
			display: -ms-flex;
			display: flex;
			-moz-align-items: -moz-flex-start;
			-webkit-align-items: -webkit-flex-start;
			-ms-align-items: -ms-flex-start;
			align-items: flex-start;
			-moz-flex-direction: row-reverse;
			-webkit-flex-direction: row-reverse;
			-ms-flex-direction: row-reverse;
			flex-direction: row-reverse;
		}

			ul.posts article .image {
				display: block;
				margin-right: 1.5em;
				min-width: 4em;
				width: 4em;
			}

				ul.posts article .image img {
					width: 100%;
				}

			ul.posts article header {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-ms-flex: 1;
			}

				ul.posts article header h3 {
					font-size: 0.7em;
					margin-top: 0.125em;
				}

				ul.posts article header .published {
					display: block;
					font-family: "Raleway", Helvetica, sans-serif;
					font-size: 0.6em;
					font-weight: 400;
					letter-spacing: 0.25em;
					margin: -0.625em 0 1.7em 0;
					text-transform: uppercase;
				}

				ul.posts article header > :last-child {
					margin-bottom: 0;
				}

/* Mini Post */

	.mini-post {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: column-reverse;
		-webkit-flex-direction: column-reverse;
		-ms-flex-direction: column-reverse;
		flex-direction: column-reverse;
		background: #ffffff;
		border: solid 1px rgba(160, 160, 160, 0.3);
		margin: 0 0 2em 0;
	}

		.mini-post .image {
			overflow: hidden;
			width: 100%;
		}

			.mini-post .image img {
				-moz-transition: -moz-transform 0.2s ease-out;
				-webkit-transition: -webkit-transform 0.2s ease-out;
				-ms-transition: -ms-transform 0.2s ease-out;
				transition: transform 0.2s ease-out;
				width: 100%;
			}

			.mini-post .image:hover img {
				-moz-transform: scale(1.05);
				-webkit-transform: scale(1.05);
				-ms-transform: scale(1.05);
				transform: scale(1.05);
			}

		.mini-post header {
			padding: 1.25em 4.25em 0.1em 1.25em ;
			min-height: 4em;
			position: relative;
			-moz-flex-grow: 1;
			-webkit-flex-grow: 1;
			-ms-flex-grow: 1;
			flex-grow: 1;
		}

			.mini-post header h3 {
				font-size: 0.7em;
			}

			.mini-post header .published {
				display: block;
				font-family: "Raleway", Helvetica, sans-serif;
				font-size: 0.6em;
				font-weight: 400;
				letter-spacing: 0.25em;
				margin: -0.625em 0 1.7em 0;
				text-transform: uppercase;
			}

			.mini-post header .author {
				position: absolute;
				right: 2em;
				top: 2em;
			}

	.mini-posts {
		margin: 0 0 2em 0;
	}

		@media screen and (max-width: 1280px) {

			.mini-posts {
				display: -moz-flex;
				display: -webkit-flex;
				display: -ms-flex;
				display: flex;
				-moz-flex-wrap: wrap;
				-webkit-flex-wrap: wrap;
				-ms-flex-wrap: wrap;
				flex-wrap: wrap;
				width: calc(100% + 2em);
			}

				.mini-posts > * {
					margin: 2em 2em 0 0;
					width: calc(50% - 2em);
				}

				.mini-posts > :nth-child(-n + 2) {
					margin-top: 0;
				}

		}

		@media screen and (max-width: 480px) {

			.mini-posts {
				display: block;
				width: 100%;
			}

				.mini-posts > * {
					margin: 0 0 2em 0;
					width: 100%;
				}

		}

/* Post */

	.post {
		padding: 3em 3em 1em 3em ;
		background: #ffffff;
		border: solid 1px rgba(160, 160, 160, 0.3);
		margin: 0 0 3em 0;
		position: relative;
	}

		.post > header {
			display: -moz-flex;
			display: -webkit-flex;
			display: -ms-flex;
			display: flex;
			border-bottom: solid 1px rgba(160, 160, 160, 0.3);
			left: -3em;
			margin: -3em 0 3em 0;
			position: relative;
			width: calc(100% + 6em);
		}

			.post > header .title {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-ms-flex: 1;
				padding: 3.75em 3em 3.3em 3em;
			}

				.post > header .title h2 {
					font-weight: 900;
					font-size: 1.5em;
				}

				.post > header .title > :last-child {
					margin-bottom: 0;
				}

			.post > header .meta {
				padding: 3.75em 3em 1.75em 3em ;
				border-left: solid 1px rgba(160, 160, 160, 0.3);
				min-width: 17em;
				text-align: right;
				width: 17em;
			}

				.post > header .meta > * {
					margin: 0 0 1em 0;
				}

				.post > header .meta > :last-child {
					margin-bottom: 0;
				}

				.post > header .meta .published {
					color: #3c3b3b;
					display: block;
					font-family: "Raleway", Helvetica, sans-serif;
					font-size: 0.7em;
					font-weight: 800;
					letter-spacing: 0.25em;
					margin-top: 0.5em;
					text-transform: uppercase;
					white-space: nowrap;
				}

		.post > a.image.featured {
			overflow: hidden;
		}

			.post > a.image.featured img {
				-moz-transition: -moz-transform 0.2s ease-out;
				-webkit-transition: -webkit-transform 0.2s ease-out;
				-ms-transition: -ms-transform 0.2s ease-out;
				transition: transform 0.2s ease-out;
			}

			.post > a.image.featured:hover img {
				-moz-transform: scale(1.05);
				-webkit-transform: scale(1.05);
				-ms-transform: scale(1.05);
				transform: scale(1.05);
			}

		.post > footer {
			display: -moz-flex;
			display: -webkit-flex;
			display: -ms-flex;
			display: flex;
			-moz-align-items: center;
			-webkit-align-items: center;
			-ms-align-items: center;
			align-items: center;
		}

			.post > footer .actions {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
			}

			.post > footer .stats {
				cursor: default;
				list-style: none;
				padding: 0;
			}

				.post > footer .stats li {
					border-left: solid 1px rgba(160, 160, 160, 0.3);
					display: inline-block;
					font-family: "Raleway", Helvetica, sans-serif;
					font-size: 0.6em;
					font-weight: 400;
					letter-spacing: 0.25em;
					line-height: 1;
					margin: 0 0 0 2em;
					padding: 0 0 0 2em;
					text-transform: uppercase;
				}

					.post > footer .stats li:first-child {
						border-left: 0;
						margin-left: 0;
						padding-left: 0;
					}

					.post > footer .stats li .icon {
						border-bottom: 0;
					}

						.post > footer .stats li .icon:before {
							color: rgba(160, 160, 160, 0.3);
							margin-right: 0.75em;
						}

		@media screen and (max-width: 980px) {

			.post {
				border-left: 0;
				border-right: 0;
				left: -3em;
				width: calc(100% + (3em * 2));
			}

				.post > header {
					-moz-flex-direction: column;
					-webkit-flex-direction: column;
					-ms-flex-direction: column;
					flex-direction: column;
					padding: 3.75em 3em 1.25em 3em ;
					border-left: 0;
				}

					.post > header .title {
						-ms-flex: 0 1 auto;
						margin: 0 0 2em 0;
						padding: 0;
						text-align: center;
					}

					.post > header .meta {
						-moz-align-items: center;
						-webkit-align-items: center;
						-ms-align-items: center;
						align-items: center;
						display: -moz-flex;
						display: -webkit-flex;
						display: -ms-flex;
						display: flex;
						-moz-justify-content: center;
						-webkit-justify-content: center;
						-ms-justify-content: center;
						justify-content: center;
						border-left: 0;
						margin: 0 0 2em 0;
						padding-top: 0;
						padding: 0;
						text-align: left;
						width: 100%;
					}

						.post > header .meta > * {
							border-left: solid 1px rgba(160, 160, 160, 0.3);
							margin-left: 2em;
							padding-left: 2em;
						}

						.post > header .meta > :first-child {
							border-left: 0;
							margin-left: 0;
							padding-left: 0;
						}

						.post > header .meta .published {
							margin-bottom: 0;
							margin-top: 0;
						}

						.post > header .meta .author {
							-moz-flex-direction: row-reverse;
							-webkit-flex-direction: row-reverse;
							-ms-flex-direction: row-reverse;
							flex-direction: row-reverse;
							margin-bottom: 0;
						}

							.post > header .meta .author .name {
								margin: 0 0 0 1.5em;
							}

							.post > header .meta .author img {
								width: 3.5em;
							}

		}

		@media screen and (max-width: 736px) {

			.post {
				padding: 1.5em 1.5em 0.1em 1.5em ;
				left: -1.5em;
				margin: 0 0 2em 0;
				width: calc(100% + (1.5em * 2));
			}

				.post > header {
					padding: 3em 1.5em 0.5em 1.5em ;
					left: -1.5em;
					margin: -1.5em 0 1.5em 0;
					width: calc(100% + 3em);
				}

					.post > header .title h2 {
						font-size: 1.1em;
					}

		}

		@media screen and (max-width: 480px) {

			.post > header .meta {
				-moz-align-items: center;
				-webkit-align-items: center;
				-ms-align-items: center;
				align-items: center;
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
			}

				.post > header .meta > * {
					border-left: 0;
					margin: 1em 0 0 0;
					padding-left: 0;
				}

				.post > header .meta .author .name {
					display: none;
				}

			.post > .image.featured {
				margin-left: -1.5em;
				margin-top: calc(-1.5em - 1px);
				width: calc(100% + 3em);
			}

			.post > footer {
				-moz-align-items: -moz-stretch;
				-webkit-align-items: -webkit-stretch;
				-ms-align-items: -ms-stretch;
				align-items: stretch;
				-moz-flex-direction: column-reverse;
				-webkit-flex-direction: column-reverse;
				-ms-flex-direction: column-reverse;
				flex-direction: column-reverse;
			}

				.post > footer .stats {
					text-align: center;
				}

					.post > footer .stats li {
						margin: 0 0 0 1.25em;
						padding: 0 0 0 1.25em;
					}

		}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header p {
		font-family: "Raleway", Helvetica, sans-serif;
		font-size: 0.7em;
		font-weight: 400;
		letter-spacing: 0.25em;
		line-height: 2.5;
		margin-top: -1em;
		text-transform: uppercase;
	}

/* Table */

	.table-wrapper {
		-webkit-overflow-scrolling: touch;
		overflow-x: auto;
	}

	table {
		margin: 0 0 2em 0;
		width: 100%;
	}

		table tbody tr {
			border: solid 1px rgba(160, 160, 160, 0.3);
			border-left: 0;
			border-right: 0;
		}

			table tbody tr:nth-child(2n + 1) {
				background-color: rgba(160, 160, 160, 0.075);
			}

		table td {
			padding: 0.75em 0.75em;
		}

		table th {
			color: #3c3b3b;
			font-size: 0.9em;
			font-weight: 700;
			padding: 0 0.75em 0.75em 0.75em;
			text-align: left;
		}

		table thead {
			border-bottom: solid 2px rgba(160, 160, 160, 0.3);
		}

		table tfoot {
			border-top: solid 2px rgba(160, 160, 160, 0.3);
		}

		table.alt {
			border-collapse: separate;
		}

			table.alt tbody tr td {
				border: solid 1px rgba(160, 160, 160, 0.3);
				border-left-width: 0;
				border-top-width: 0;
			}

				table.alt tbody tr td:first-child {
					border-left-width: 1px;
				}

			table.alt tbody tr:first-child td {
				border-top-width: 1px;
			}

			table.alt thead {
				border-bottom: 0;
			}

			table.alt tfoot {
				border-top: 0;
			}

/* Header */

	body {
		padding-top: 3.5em;
	}

	#header {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-justify-content: space-between;
		-webkit-justify-content: space-between;
		-ms-justify-content: space-between;
		justify-content: space-between;
		background-color: #ffffff;
		border-bottom: solid 1px rgba(160, 160, 160, 0.3);
		height: 3.5em;
		left: 0;
		line-height: 3.5em;
		position: fixed;
		top: 0;
		width: 100%;
		z-index: 10000;
	}

		#header a {
			color: inherit;
			text-decoration: none;
		}

		#header ul {
			list-style: none;
			margin: 0;
			padding-left: 0;
		}

			#header ul li {
				display: inline-block;
				padding-left: 0;
			}

		#header h1 {
			height: inherit;
			line-height: inherit;
			padding: 0 0 0 1.5em;
			white-space: nowrap;
		}

			#header h1 a {
				font-size: 0.7em;
			}

		#header .links {
			-moz-flex: 1;
			-webkit-flex: 1;
			-ms-flex: 1;
			flex: 1;
			border-left: solid 1px rgba(160, 160, 160, 0.3);
			height: inherit;
			line-height: inherit;
			margin-left: 1.5em;
			overflow: hidden;
			padding-left: 1.5em;
		}

			#header .links ul li {
				border-left: solid 1px rgba(160, 160, 160, 0.3);
				line-height: 1;
				margin-left: 1em;
				padding-left: 1em;
			}

				#header .links ul li:first-child {
					border-left: 0;
					margin-left: 0;
					padding-left: 0;
				}

				#header .links ul li a {
					border-bottom: 0;
					font-family: "Raleway", Helvetica, sans-serif;
					font-size: 0.7em;
					font-weight: 400;
					letter-spacing: 0.25em;
					text-transform: uppercase;
				}

		#header .main {
			height: inherit;
			line-height: inherit;
			text-align: right;
		}

			#header .main ul {
				height: inherit;
				line-height: inherit;
			}

				#header .main ul li {
					border-left: solid 1px rgba(160, 160, 160, 0.3);
					height: inherit;
					line-height: inherit;
					white-space: nowrap;
				}

					#header .main ul li > * {
						display: block;
						float: left;
					}

					#header .main ul li > a {
						text-decoration: none;
						border-bottom: 0;
						color: #aaaaaa;
						overflow: hidden;
						position: relative;
						text-indent: 4em;
						width: 4em;
					}

						#header .main ul li > a:before {
							-moz-osx-font-smoothing: grayscale;
							-webkit-font-smoothing: antialiased;
							display: inline-block;
							font-style: normal;
							font-variant: normal;
							text-rendering: auto;
							line-height: 1;
							text-transform: none !important;
							font-family: 'Font Awesome 5 Free';
							font-weight: 900;
						}

						#header .main ul li > a:before {
							display: block;
							height: inherit;
							left: 0;
							line-height: inherit;
							position: absolute;
							text-align: center;
							text-indent: 0;
							top: 0;
							width: inherit;
						}

		#header form {
			margin: 0;
		}

			#header form input {
				display: inline-block;
				height: 2.5em;
				position: relative;
				top: -2px;
				vertical-align: middle;
			}

		#header #search {
			-moz-transition: all 0.5s ease;
			-webkit-transition: all 0.5s ease;
			-ms-transition: all 0.5s ease;
			transition: all 0.5s ease;
			max-width: 0;
			opacity: 0;
			overflow: hidden;
			padding: 0;
			white-space: nowrap;
		}

			#header #search input {
				width: 12em;
			}

			#header #search.visible {
				max-width: 12.5em;
				opacity: 1;
				padding: 0 0.5em 0 0;
			}

		@media screen and (max-width: 980px) {

			#header .links {
				display: none;
			}

		}

		@media screen and (max-width: 736px) {

			#header {
				height: 2.75em;
				line-height: 2.75em;
			}

				#header h1 {
					padding: 0 0 0 1em;
				}

				#header .main .search {
					display: none;
				}

		}

/* Wrapper */

	#wrapper {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: row-reverse;
		-webkit-flex-direction: row-reverse;
		-ms-flex-direction: row-reverse;
		flex-direction: row-reverse;
		-moz-transition: opacity 0.5s ease;
		-webkit-transition: opacity 0.5s ease;
		-ms-transition: opacity 0.5s ease;
		transition: opacity 0.5s ease;
		margin: 0 auto;
		max-width: 100%;
		opacity: 1;
		padding: 4.5em;
		width: 90em;
	}

		body.is-menu-visible #wrapper {
			opacity: 0.15;
		}

		@media screen and (max-width: 1680px) {

			#wrapper {
				padding: 3em;
			}

		}

		@media screen and (max-width: 1280px) {

			#wrapper {
				display: block;
			}

		}

		@media screen and (max-width: 736px) {

			#wrapper {
				padding: 1.5em;
			}

		}

		body.single #wrapper {
			display: block;
		}

/* Main */

	#main {
		-moz-flex-grow: 1;
		-webkit-flex-grow: 1;
		-ms-flex-grow: 1;
		flex-grow: 1;
		-ms-flex: 1;
		width: 100%;
	}

/* Sidebar */

	#sidebar {
		margin-right: 3em;
		min-width: 22em;
		width: 22em;
	}

		#sidebar > * {
			border-top: solid 1px rgba(160, 160, 160, 0.3);
			margin: 3em 0 0 0;
			padding: 3em 0 0 0;
		}

		#sidebar > :first-child {
			border-top: 0;
			margin-top: 0;
			padding-top: 0;
		}

		@media screen and (max-width: 1280px) {

			#sidebar {
				border-top: solid 1px rgba(160, 160, 160, 0.3);
				margin: 3em 0 0 0;
				min-width: 0;
				padding: 3em 0 0 0;
				width: 100%;
				overflow-x: hidden;
			}

		}

/* Intro */

	#intro .logo {
		border-bottom: 0;
		display: inline-block;
		margin: 0 0 1em 0;
		overflow: hidden;
		position: relative;
		width: 4em;
	}

		#intro .logo:before {
			background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100px' height='100px' viewBox='0 0 100 100' preserveAspectRatio='none' zoomAndPan='disable'%3E%3Cpolygon points='0,0 100,0 100,25 50,0 0,25' style='fill:%23f4f4f4' /%3E%3Cpolygon points='0,100 100,100 100,75 50,100 0,75' style='fill:%23f4f4f4' /%3E%3C/svg%3E");
			background-position: top left;
			background-repeat: no-repeat;
			background-size: 100% 100%;
			content: '';
			display: block;
			height: 100%;
			left: 0;
			position: absolute;
			top: 0;
			width: 100%;
		}

		#intro .logo img {
			display: block;
			margin-left: -0.25em;
			width: 4.5em;
		}

	#intro header h2 {
		font-size: 2em;
		font-weight: 900;
	}

	#intro header p {
		font-size: 0.8em;
	}

	@media screen and (max-width: 1280px) {

		#intro {
			margin: 0 0 3em 0;
			text-align: center;
		}

			#intro header h2 {
				font-size: 2em;
			}

			#intro header p {
				font-size: 0.7em;
			}

	}

	@media screen and (max-width: 736px) {

		#intro {
			margin: 0 0 1.5em 0;
			padding: 1.25em 0;
		}

			#intro > :last-child {
				margin-bottom: 0;
			}

			#intro .logo {
				margin: 0 0 0.5em 0;
			}

			#intro header h2 {
				font-size: 1.25em;
			}

			#intro header > :last-child {
				margin-bottom: 0;
			}

	}

/* Footer */

	#footer .icons {
		color: #aaaaaa;
	}

	#footer .copyright {
		color: #aaaaaa;
		font-family: "Raleway", Helvetica, sans-serif;
		font-size: 0.5em;
		font-weight: 400;
		letter-spacing: 0.25em;
		text-transform: uppercase;
	}

	body.single #footer {
		text-align: center;
	}

/* Menu */

	#menu {
		-moz-transform: translateX(25em);
		-webkit-transform: translateX(25em);
		-ms-transform: translateX(25em);
		transform: translateX(25em);
		-moz-transition: -moz-transform 0.5s ease, visibility 0.5s;
		-webkit-transition: -webkit-transform 0.5s ease, visibility 0.5s;
		-ms-transition: -ms-transform 0.5s ease, visibility 0.5s;
		transition: transform 0.5s ease, visibility 0.5s;
		-webkit-overflow-scrolling: touch;
		background: #ffffff;
		border-left: solid 1px rgba(160, 160, 160, 0.3);
		box-shadow: none;
		height: 100%;
		max-width: 80%;
		overflow-y: auto;
		position: fixed;
		right: 0;
		top: 0;
		visibility: hidden;
		width: 25em;
		z-index: 10002;
	}

		#menu > * {
			border-top: solid 1px rgba(160, 160, 160, 0.3);
			padding: 3em;
		}

			#menu > * > :last-child {
				margin-bottom: 0;
			}

		#menu > :first-child {
			border-top: 0;
		}

		#menu .links {
			list-style: none;
			padding: 0;
		}

			#menu .links > li {
				border: 0;
				border-top: dotted 1px rgba(160, 160, 160, 0.3);
				margin: 1.5em 0 0 0;
				padding: 1.5em 0 0 0;
			}

				#menu .links > li a {
					display: block;
					border-bottom: 0;
				}

					#menu .links > li a h3 {
						-moz-transition: color 0.2s ease;
						-webkit-transition: color 0.2s ease;
						-ms-transition: color 0.2s ease;
						transition: color 0.2s ease;
						font-size: 0.7em;
					}

					#menu .links > li a p {
						font-family: "Raleway", Helvetica, sans-serif;
						font-size: 0.6em;
						font-weight: 400;
						letter-spacing: 0.25em;
						margin-bottom: 0;
						text-decoration: none;
						text-transform: uppercase;
					}

					#menu .links > li a:hover h3 {
						color: #2ebaae;
					}

				#menu .links > li:first-child {
					border-top: 0;
					margin-top: 0;
					padding-top: 0;
				}

		body.is-menu-visible #menu {
			-moz-transform: translateX(0);
			-webkit-transform: translateX(0);
			-ms-transform: translateX(0);
			transform: translateX(0);
			visibility: visible;
		}

		@media screen and (max-width: 736px) {

			#menu > * {
				padding: 1.5em;
			}

		}""", 
        "lime": """body {
    background-color: #F6E96B;
    color: #hycuna; /* Text color */
}

/* Header Background and Text Color */
header {
    background-color: #F6E96B;
    color: #387F39;
}

/* Section Background and Text Color */
section {
    background-color: #F6E96B;
    color: #387F39;
}

/* Footer Background and Text Color */
footer {
    background-color: #387F39;
    color: #F6E96B;
}

/* Links Color */
a {
    color: #387F39;
}

a:hover {
    color: #A2CA71;
}

/* Buttons */
button {
    background-color: #BEDC74;
    color: #387F39;
    border: 2px solid #387F39;
}

button:hover {
    background-color: #A2CA71;
    color: #F6E96B;
}
.post {
    background-color: #ffffff;
    color: #F6E96B;
}

/* Other elements */
h1, h2, h3, h4, h5, h6 {
    color: #387F39;
}

p {
    color: #387F39;
}
""",
        "valley": """		body {
			background-color: #CCD5AE;
			color: #FEFAE0; /* Text color */
		}
		
		/* Header Background and Text Color */
		header {
			background-color: #CCD5AE;
			color: #39250a;
		}
		
		/* Section Background and Text Color */
		section {
			background-color: #CCD5AE;
			color: #FEFAE0;
		}
		
		/* Footer Background and Text Color */
		footer {
			background-color: #FEFAE0;
			color: #CCD5AE;
		}
		
		/* Links Color */
		a {
			color: #39250a;
		}
		
		a:hover {
			color: #ffe29e;
		}
		
		/* Buttons */
		button {
			background-color: #E0E5B6;
			color: #FEFAE0;
			border: 2px solid #FEFAE0;
		}
		
		button:hover {
			background-color: #FAEDCE;
			color: #CCD5AE;
		}
		
		.post {
			background-color: #ffffff;
			color: #CCD5AE;
		}
		
		/* Other elements */
		h2, h3, h4, h5, h6 {
			color: #FEFAE0;
		}
		
		p {
			color: #39250a;
		}
		""", 
        "phantom": """		body {
			background-color: #17153B; /* Dark background */
			color: #C8ACD6; /* Light text color */
		}
		
		/* Header Background and Text Color */
		header {
			background-color: #2E236C;
			color: #C8ACD6;
		}
		
		/* Section Background and Text Color */
		section {
			background-color: #17153B;
			color: #C8ACD6;
		}
		
		/* Footer Background and Text Color */
		footer {
			background-color: #17153B;
			color: #C8ACD6;
		}
		
		/* Links Color */
		a {
			color: #C8ACD6;
		}
		
		a:hover {
			color: #433D8B;
		}
		
		/* Buttons */
		button {
			background-color: #433D8B;
			color: #C8ACD6;
			border: 2px solid #C8ACD6;
		}
		
		button:hover {
			background-color: #2E236C;
			color: #C8ACD6;
		}
		
		.post {
			background-color: #2E236C;
			color: #C8ACD6;
		}
		
		/* Other elements */
		h1, h2, h3, h4, h5, h6 {
			color: #C8ACD6;
		}
		
		p {
			color: #C8ACD6;
		}
		""",
        "sakura":"""		body {
			background-color: #FFEBD4;
			color: #F0A8D0; /* Text color */
		}
		
		/* Header Background and Text Color */
		header {
			background-color: #FFEBD4;
			color: #F0A8D0;
		}
		
		/* Section Background and Text Color */
		section {
			background-color: #FFEBD4;
			color: #F0A8D0;
		}
		
		/* Footer Background and Text Color */
		footer {
			background-color: #F0A8D0;
			color: #FFEBD4;
		}
		
		/* Links Color */
		a {
			color: #F0A8D0;
		}
		
		a:hover {
			color: #F7B5CA;
		}
		
		/* Buttons */
		button {
			background-color: #FFC6C6;
			color: #F0A8D0;
			border: 2px solid #F0A8D0;
		}
		
		button:hover {
			background-color: #F7B5CA;
			color: #FFEBD4;
		}
		
		.post {
			background-color: #F7B5CA;
			color: #ffffff;
		}
		
		/* Other elements */
		h1, h2, h3, h4, h5, h6 {
			color: #F0A8D0;
		}
		
		p {
			color: #FFEBD4;
		}
		""", 
        "elegant":"""body {
    background-color: #173B45; /* Dark background */
    color: #F8EDED; /* Light text color */
}

/* Header Background and Text Color */
header {
    background-color: #173B45;
    color: #F8EDED;
}

/* Section Background and Text Color */
section {
    background-color: #173B45;
    color: #F8EDED;
}

/* Footer Background and Text Color */
footer {
    background-color: #B43F3F;
    color: #F8EDED;
}

/* Links Color */
a {
    color: #FF8225;
}

a:hover {
    color: #B43F3F;
}

/* Buttons */
button {
    background-color: #B43F3F;
    color: #F8EDED;
    border: 2px solid #F8EDED;
}

button:hover {
    background-color: #FF8225;
    color: #173B45;
}

.post {
    background-color: #2E236C;
    color: #F8EDED;
}

h2, h3, h4, h5, h6 {
    color: #F8EDED;
}

p {
    color: #F8EDED;
}
"""}, 
"editorial" : {
     "default": """			@import url(fontawesome-all.min.css);
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,600,400italic,600italic|Roboto+Slab:400,700");
html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline; }

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
  display: block; }

body {
  line-height: 1; }

ol, ul {
  list-style: none; }

blockquote, q {
  quotes: none; }
  blockquote:before, blockquote:after, q:before, q:after {
    content: '';
    content: none; }

table {
  border-collapse: collapse;
  border-spacing: 0; }

body {
  -webkit-text-size-adjust: none; }

mark {
  background-color: transparent;
  color: inherit; }

input::-moz-focus-inner {
  border: 0;
  padding: 0; }

input, select, textarea {
  -moz-appearance: none;
  -webkit-appearance: none;
  -ms-appearance: none;
  appearance: none; }

/* Basic */
@-ms-viewport {
  width: device-width; }

body {
  -ms-overflow-style: scrollbar; }

@media screen and (max-width: 480px) {
  html, body {
    min-width: 320px; } }

html {
  box-sizing: border-box; }

*, *:before, *:after {
  box-sizing: inherit; }

body {
  background: #ffffff; }
  body.is-preload *, body.is-preload *:before, body.is-preload *:after, body.is-resizing *, body.is-resizing *:before, body.is-resizing *:after {
    -moz-animation: none !important;
    -webkit-animation: none !important;
    -ms-animation: none !important;
    animation: none !important;
    -moz-transition: none !important;
    -webkit-transition: none !important;
    -ms-transition: none !important;
    transition: none !important; }

/* Type */
body, input, select, textarea {
  color: #7f888f;
  font-family: "Open Sans", sans-serif;
  font-size: 13pt;
  font-weight: 400;
  line-height: 1.65; }
  @media screen and (max-width: 1680px) {
    body, input, select, textarea {
      font-size: 11pt; } }
  @media screen and (max-width: 1280px) {
    body, input, select, textarea {
      font-size: 10pt; } }
  @media screen and (max-width: 360px) {
    body, input, select, textarea {
      font-size: 9pt; } }

a {
  -moz-transition: color 0.2s ease-in-out, border-bottom-color 0.2s ease-in-out;
  -webkit-transition: color 0.2s ease-in-out, border-bottom-color 0.2s ease-in-out;
  -ms-transition: color 0.2s ease-in-out, border-bottom-color 0.2s ease-in-out;
  transition: color 0.2s ease-in-out, border-bottom-color 0.2s ease-in-out;
  border-bottom: dotted 1px;
  color: #f56a6a;
  text-decoration: none; }
  a:hover {
    border-bottom-color: #f56a6a;
    color: #f56a6a !important; }
    a:hover strong {
      color: inherit; }

strong, b {
  color: #3d4449;
  font-weight: 600; }

em, i {
  font-style: italic; }

p {
  margin: 0 0 2em 0; }

h1, h2, h3, h4, h5, h6 {
  color: #3d4449;
  font-family: "Roboto Slab", serif;
  font-weight: 700;
  line-height: 1.5;
  margin: 0 0 1em 0; }
  h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
    color: inherit;
    text-decoration: none;
    border-bottom: 0; }

h1 {
  font-size: 4em;
  margin: 0 0 0.5em 0;
  line-height: 1.3; }

h2 {
  font-size: 1.75em; }

h3 {
  font-size: 1.25em; }

h4 {
  font-size: 1.1em; }

h5 {
  font-size: 0.9em; }

h6 {
  font-size: 0.7em; }

@media screen and (max-width: 1680px) {
  h1 {
    font-size: 3.5em; } }

@media screen and (max-width: 980px) {
  h1 {
    font-size: 3.25em; } }

@media screen and (max-width: 736px) {
  h1 {
    font-size: 2em;
    line-height: 1.4; }
  h2 {
    font-size: 1.5em; } }

sub {
  font-size: 0.8em;
  position: relative;
  top: 0.5em; }

sup {
  font-size: 0.8em;
  position: relative;
  top: -0.5em; }

blockquote {
  border-left: solid 3px rgba(210, 215, 217, 0.75);
  font-style: italic;
  margin: 0 0 2em 0;
  padding: 0.5em 0 0.5em 2em; }

code {
  background: rgba(230, 235, 237, 0.25);
  border-radius: 0.375em;
  border: solid 1px rgba(210, 215, 217, 0.75);
  font-family: "Courier New", monospace;
  font-size: 0.9em;
  margin: 0 0.25em;
  padding: 0.25em 0.65em; }

pre {
  -webkit-overflow-scrolling: touch;
  font-family: "Courier New", monospace;
  font-size: 0.9em;
  margin: 0 0 2em 0; }
  pre code {
    display: block;
    line-height: 1.75;
    padding: 1em 1.5em;
    overflow-x: auto; }

hr {
  border: 0;
  border-bottom: solid 1px rgba(210, 215, 217, 0.75);
  margin: 2em 0; }
  hr.major {
    margin: 3em 0; }

.align-left {
  text-align: left; }

.align-center {
  text-align: center; }

.align-right {
  text-align: right; }

/* Row */
.row {
  display: flex;
  flex-wrap: wrap;
  box-sizing: border-box;
  align-items: stretch; }
  .row > * {
    box-sizing: border-box; }
  .row.gtr-uniform > * > :last-child {
    margin-bottom: 0; }
  .row.aln-left {
    justify-content: flex-start; }
  .row.aln-center {
    justify-content: center; }
  .row.aln-right {
    justify-content: flex-end; }
  .row.aln-top {
    align-items: flex-start; }
  .row.aln-middle {
    align-items: center; }
  .row.aln-bottom {
    align-items: flex-end; }
  .row > .imp {
    order: -1; }
  .row > .col-1 {
    width: 8.33333%; }
  .row > .off-1 {
    margin-left: 8.33333%; }
  .row > .col-2 {
    width: 16.66667%; }
  .row > .off-2 {
    margin-left: 16.66667%; }
  .row > .col-3 {
    width: 25%; }
  .row > .off-3 {
    margin-left: 25%; }
  .row > .col-4 {
    width: 33.33333%; }
  .row > .off-4 {
    margin-left: 33.33333%; }
  .row > .col-5 {
    width: 41.66667%; }
  .row > .off-5 {
    margin-left: 41.66667%; }
  .row > .col-6 {
    width: 50%; }
  .row > .off-6 {
    margin-left: 50%; }
  .row > .col-7 {
    width: 58.33333%; }
  .row > .off-7 {
    margin-left: 58.33333%; }
  .row > .col-8 {
    width: 66.66667%; }
  .row > .off-8 {
    margin-left: 66.66667%; }
  .row > .col-9 {
    width: 75%; }
  .row > .off-9 {
    margin-left: 75%; }
  .row > .col-10 {
    width: 83.33333%; }
  .row > .off-10 {
    margin-left: 83.33333%; }
  .row > .col-11 {
    width: 91.66667%; }
  .row > .off-11 {
    margin-left: 91.66667%; }
  .row > .col-12 {
    width: 100%; }
  .row > .off-12 {
    margin-left: 100%; }
  .row.gtr-0 {
    margin-top: 0;
    margin-left: 0em; }
    .row.gtr-0 > * {
      padding: 0 0 0 0em; }
    .row.gtr-0.gtr-uniform {
      margin-top: 0em; }
      .row.gtr-0.gtr-uniform > * {
        padding-top: 0em; }
  .row.gtr-25 {
    margin-top: 0;
    margin-left: -0.375em; }
    .row.gtr-25 > * {
      padding: 0 0 0 0.375em; }
    .row.gtr-25.gtr-uniform {
      margin-top: -0.375em; }
      .row.gtr-25.gtr-uniform > * {
        padding-top: 0.375em; }
  .row.gtr-50 {
    margin-top: 0;
    margin-left: -0.75em; }
    .row.gtr-50 > * {
      padding: 0 0 0 0.75em; }
    .row.gtr-50.gtr-uniform {
      margin-top: -0.75em; }
      .row.gtr-50.gtr-uniform > * {
        padding-top: 0.75em; }
  .row {
    margin-top: 0;
    margin-left: -1.5em; }
    .row > * {
      padding: 0 0 0 1.5em; }
    .row.gtr-uniform {
      margin-top: -1.5em; }
      .row.gtr-uniform > * {
        padding-top: 1.5em; }
  .row.gtr-150 {
    margin-top: 0;
    margin-left: -2.25em; }
    .row.gtr-150 > * {
      padding: 0 0 0 2.25em; }
    .row.gtr-150.gtr-uniform {
      margin-top: -2.25em; }
      .row.gtr-150.gtr-uniform > * {
        padding-top: 2.25em; }
  .row.gtr-200 {
    margin-top: 0;
    margin-left: -3em; }
    .row.gtr-200 > * {
      padding: 0 0 0 3em; }
    .row.gtr-200.gtr-uniform {
      margin-top: -3em; }
      .row.gtr-200.gtr-uniform > * {
        padding-top: 3em; }
  @media screen and (max-width: 1680px) {
    .row {
      display: flex;
      flex-wrap: wrap;
      box-sizing: border-box;
      align-items: stretch; }
      .row > * {
        box-sizing: border-box; }
      .row.gtr-uniform > * > :last-child {
        margin-bottom: 0; }
      .row.aln-left {
        justify-content: flex-start; }
      .row.aln-center {
        justify-content: center; }
      .row.aln-right {
        justify-content: flex-end; }
      .row.aln-top {
        align-items: flex-start; }
      .row.aln-middle {
        align-items: center; }
      .row.aln-bottom {
        align-items: flex-end; }
      .row > .imp-xlarge {
        order: -1; }
      .row > .col-1-xlarge {
        width: 8.33333%; }
      .row > .off-1-xlarge {
        margin-left: 8.33333%; }
      .row > .col-2-xlarge {
        width: 16.66667%; }
      .row > .off-2-xlarge {
        margin-left: 16.66667%; }
      .row > .col-3-xlarge {
        width: 25%; }
      .row > .off-3-xlarge {
        margin-left: 25%; }
      .row > .col-4-xlarge {
        width: 33.33333%; }
      .row > .off-4-xlarge {
        margin-left: 33.33333%; }
      .row > .col-5-xlarge {
        width: 41.66667%; }
      .row > .off-5-xlarge {
        margin-left: 41.66667%; }
      .row > .col-6-xlarge {
        width: 50%; }
      .row > .off-6-xlarge {
        margin-left: 50%; }
      .row > .col-7-xlarge {
        width: 58.33333%; }
      .row > .off-7-xlarge {
        margin-left: 58.33333%; }
      .row > .col-8-xlarge {
        width: 66.66667%; }
      .row > .off-8-xlarge {
        margin-left: 66.66667%; }
      .row > .col-9-xlarge {
        width: 75%; }
      .row > .off-9-xlarge {
        margin-left: 75%; }
      .row > .col-10-xlarge {
        width: 83.33333%; }
      .row > .off-10-xlarge {
        margin-left: 83.33333%; }
      .row > .col-11-xlarge {
        width: 91.66667%; }
      .row > .off-11-xlarge {
        margin-left: 91.66667%; }
      .row > .col-12-xlarge {
        width: 100%; }
      .row > .off-12-xlarge {
        margin-left: 100%; }
      .row.gtr-0 {
        margin-top: 0;
        margin-left: 0em; }
        .row.gtr-0 > * {
          padding: 0 0 0 0em; }
        .row.gtr-0.gtr-uniform {
          margin-top: 0em; }
          .row.gtr-0.gtr-uniform > * {
            padding-top: 0em; }
      .row.gtr-25 {
        margin-top: 0;
        margin-left: -0.375em; }
        .row.gtr-25 > * {
          padding: 0 0 0 0.375em; }
        .row.gtr-25.gtr-uniform {
          margin-top: -0.375em; }
          .row.gtr-25.gtr-uniform > * {
            padding-top: 0.375em; }
      .row.gtr-50 {
        margin-top: 0;
        margin-left: -0.75em; }
        .row.gtr-50 > * {
          padding: 0 0 0 0.75em; }
        .row.gtr-50.gtr-uniform {
          margin-top: -0.75em; }
          .row.gtr-50.gtr-uniform > * {
            padding-top: 0.75em; }
      .row {
        margin-top: 0;
        margin-left: -1.5em; }
        .row > * {
          padding: 0 0 0 1.5em; }
        .row.gtr-uniform {
          margin-top: -1.5em; }
          .row.gtr-uniform > * {
            padding-top: 1.5em; }
      .row.gtr-150 {
        margin-top: 0;
        margin-left: -2.25em; }
        .row.gtr-150 > * {
          padding: 0 0 0 2.25em; }
        .row.gtr-150.gtr-uniform {
          margin-top: -2.25em; }
          .row.gtr-150.gtr-uniform > * {
            padding-top: 2.25em; }
      .row.gtr-200 {
        margin-top: 0;
        margin-left: -3em; }
        .row.gtr-200 > * {
          padding: 0 0 0 3em; }
        .row.gtr-200.gtr-uniform {
          margin-top: -3em; }
          .row.gtr-200.gtr-uniform > * {
            padding-top: 3em; } }
  @media screen and (max-width: 1280px) {
    .row {
      display: flex;
      flex-wrap: wrap;
      box-sizing: border-box;
      align-items: stretch; }
      .row > * {
        box-sizing: border-box; }
      .row.gtr-uniform > * > :last-child {
        margin-bottom: 0; }
      .row.aln-left {
        justify-content: flex-start; }
      .row.aln-center {
        justify-content: center; }
      .row.aln-right {
        justify-content: flex-end; }
      .row.aln-top {
        align-items: flex-start; }
      .row.aln-middle {
        align-items: center; }
      .row.aln-bottom {
        align-items: flex-end; }
      .row > .imp-large {
        order: -1; }
      .row > .col-1-large {
        width: 8.33333%; }
      .row > .off-1-large {
        margin-left: 8.33333%; }
      .row > .col-2-large {
        width: 16.66667%; }
      .row > .off-2-large {
        margin-left: 16.66667%; }
      .row > .col-3-large {
        width: 25%; }
      .row > .off-3-large {
        margin-left: 25%; }
      .row > .col-4-large {
        width: 33.33333%; }
      .row > .off-4-large {
        margin-left: 33.33333%; }
      .row > .col-5-large {
        width: 41.66667%; }
      .row > .off-5-large {
        margin-left: 41.66667%; }
      .row > .col-6-large {
        width: 50%; }
      .row > .off-6-large {
        margin-left: 50%; }
      .row > .col-7-large {
        width: 58.33333%; }
      .row > .off-7-large {
        margin-left: 58.33333%; }
      .row > .col-8-large {
        width: 66.66667%; }
      .row > .off-8-large {
        margin-left: 66.66667%; }
      .row > .col-9-large {
        width: 75%; }
      .row > .off-9-large {
        margin-left: 75%; }
      .row > .col-10-large {
        width: 83.33333%; }
      .row > .off-10-large {
        margin-left: 83.33333%; }
      .row > .col-11-large {
        width: 91.66667%; }
      .row > .off-11-large {
        margin-left: 91.66667%; }
      .row > .col-12-large {
        width: 100%; }
      .row > .off-12-large {
        margin-left: 100%; }
      .row.gtr-0 {
        margin-top: 0;
        margin-left: 0em; }
        .row.gtr-0 > * {
          padding: 0 0 0 0em; }
        .row.gtr-0.gtr-uniform {
          margin-top: 0em; }
          .row.gtr-0.gtr-uniform > * {
            padding-top: 0em; }
      .row.gtr-25 {
        margin-top: 0;
        margin-left: -0.375em; }
        .row.gtr-25 > * {
          padding: 0 0 0 0.375em; }
        .row.gtr-25.gtr-uniform {
          margin-top: -0.375em; }
          .row.gtr-25.gtr-uniform > * {
            padding-top: 0.375em; }
      .row.gtr-50 {
        margin-top: 0;
        margin-left: -0.75em; }
        .row.gtr-50 > * {
          padding: 0 0 0 0.75em; }
        .row.gtr-50.gtr-uniform {
          margin-top: -0.75em; }
          .row.gtr-50.gtr-uniform > * {
            padding-top: 0.75em; }
      .row {
        margin-top: 0;
        margin-left: -1.5em; }
        .row > * {
          padding: 0 0 0 1.5em; }
        .row.gtr-uniform {
          margin-top: -1.5em; }
          .row.gtr-uniform > * {
            padding-top: 1.5em; }
      .row.gtr-150 {
        margin-top: 0;
        margin-left: -2.25em; }
        .row.gtr-150 > * {
          padding: 0 0 0 2.25em; }
        .row.gtr-150.gtr-uniform {
          margin-top: -2.25em; }
          .row.gtr-150.gtr-uniform > * {
            padding-top: 2.25em; }
      .row.gtr-200 {
        margin-top: 0;
        margin-left: -3em; }
        .row.gtr-200 > * {
          padding: 0 0 0 3em; }
        .row.gtr-200.gtr-uniform {
          margin-top: -3em; }
          .row.gtr-200.gtr-uniform > * {
            padding-top: 3em; } }
  @media screen and (max-width: 980px) {
    .row {
      display: flex;
      flex-wrap: wrap;
      box-sizing: border-box;
      align-items: stretch; }
      .row > * {
        box-sizing: border-box; }
      .row.gtr-uniform > * > :last-child {
        margin-bottom: 0; }
      .row.aln-left {
        justify-content: flex-start; }
      .row.aln-center {
        justify-content: center; }
      .row.aln-right {
        justify-content: flex-end; }
      .row.aln-top {
        align-items: flex-start; }
      .row.aln-middle {
        align-items: center; }
      .row.aln-bottom {
        align-items: flex-end; }
      .row > .imp-medium {
        order: -1; }
      .row > .col-1-medium {
        width: 8.33333%; }
      .row > .off-1-medium {
        margin-left: 8.33333%; }
      .row > .col-2-medium {
        width: 16.66667%; }
      .row > .off-2-medium {
        margin-left: 16.66667%; }
      .row > .col-3-medium {
        width: 25%; }
      .row > .off-3-medium {
        margin-left: 25%; }
      .row > .col-4-medium {
        width: 33.33333%; }
      .row > .off-4-medium {
        margin-left: 33.33333%; }
      .row > .col-5-medium {
        width: 41.66667%; }
      .row > .off-5-medium {
        margin-left: 41.66667%; }
      .row > .col-6-medium {
        width: 50%; }
      .row > .off-6-medium {
        margin-left: 50%; }
      .row > .col-7-medium {
        width: 58.33333%; }
      .row > .off-7-medium {
        margin-left: 58.33333%; }
      .row > .col-8-medium {
        width: 66.66667%; }
      .row > .off-8-medium {
        margin-left: 66.66667%; }
      .row > .col-9-medium {
        width: 75%; }
      .row > .off-9-medium {
        margin-left: 75%; }
      .row > .col-10-medium {
        width: 83.33333%; }
      .row > .off-10-medium {
        margin-left: 83.33333%; }
      .row > .col-11-medium {
        width: 91.66667%; }
      .row > .off-11-medium {
        margin-left: 91.66667%; }
      .row > .col-12-medium {
        width: 100%; }
      .row > .off-12-medium {
        margin-left: 100%; }
      .row.gtr-0 {
        margin-top: 0;
        margin-left: 0em; }
        .row.gtr-0 > * {
          padding: 0 0 0 0em; }
        .row.gtr-0.gtr-uniform {
          margin-top: 0em; }
          .row.gtr-0.gtr-uniform > * {
            padding-top: 0em; }
      .row.gtr-25 {
        margin-top: 0;
        margin-left: -0.375em; }
        .row.gtr-25 > * {
          padding: 0 0 0 0.375em; }
        .row.gtr-25.gtr-uniform {
          margin-top: -0.375em; }
          .row.gtr-25.gtr-uniform > * {
            padding-top: 0.375em; }
      .row.gtr-50 {
        margin-top: 0;
        margin-left: -0.75em; }
        .row.gtr-50 > * {
          padding: 0 0 0 0.75em; }
        .row.gtr-50.gtr-uniform {
          margin-top: -0.75em; }
          .row.gtr-50.gtr-uniform > * {
            padding-top: 0.75em; }
      .row {
        margin-top: 0;
        margin-left: -1.5em; }
        .row > * {
          padding: 0 0 0 1.5em; }
        .row.gtr-uniform {
          margin-top: -1.5em; }
          .row.gtr-uniform > * {
            padding-top: 1.5em; }
      .row.gtr-150 {
        margin-top: 0;
        margin-left: -2.25em; }
        .row.gtr-150 > * {
          padding: 0 0 0 2.25em; }
        .row.gtr-150.gtr-uniform {
          margin-top: -2.25em; }
          .row.gtr-150.gtr-uniform > * {
            padding-top: 2.25em; }
      .row.gtr-200 {
        margin-top: 0;
        margin-left: -3em; }
        .row.gtr-200 > * {
          padding: 0 0 0 3em; }
        .row.gtr-200.gtr-uniform {
          margin-top: -3em; }
          .row.gtr-200.gtr-uniform > * {
            padding-top: 3em; } }
  @media screen and (max-width: 736px) {
    .row {
      display: flex;
      flex-wrap: wrap;
      box-sizing: border-box;
      align-items: stretch; }
      .row > * {
        box-sizing: border-box; }
      .row.gtr-uniform > * > :last-child {
        margin-bottom: 0; }
      .row.aln-left {
        justify-content: flex-start; }
      .row.aln-center {
        justify-content: center; }
      .row.aln-right {
        justify-content: flex-end; }
      .row.aln-top {
        align-items: flex-start; }
      .row.aln-middle {
        align-items: center; }
      .row.aln-bottom {
        align-items: flex-end; }
      .row > .imp-small {
        order: -1; }
      .row > .col-1-small {
        width: 8.33333%; }
      .row > .off-1-small {
        margin-left: 8.33333%; }
      .row > .col-2-small {
        width: 16.66667%; }
      .row > .off-2-small {
        margin-left: 16.66667%; }
      .row > .col-3-small {
        width: 25%; }
      .row > .off-3-small {
        margin-left: 25%; }
      .row > .col-4-small {
        width: 33.33333%; }
      .row > .off-4-small {
        margin-left: 33.33333%; }
      .row > .col-5-small {
        width: 41.66667%; }
      .row > .off-5-small {
        margin-left: 41.66667%; }
      .row > .col-6-small {
        width: 50%; }
      .row > .off-6-small {
        margin-left: 50%; }
      .row > .col-7-small {
        width: 58.33333%; }
      .row > .off-7-small {
        margin-left: 58.33333%; }
      .row > .col-8-small {
        width: 66.66667%; }
      .row > .off-8-small {
        margin-left: 66.66667%; }
      .row > .col-9-small {
        width: 75%; }
      .row > .off-9-small {
        margin-left: 75%; }
      .row > .col-10-small {
        width: 83.33333%; }
      .row > .off-10-small {
        margin-left: 83.33333%; }
      .row > .col-11-small {
        width: 91.66667%; }
      .row > .off-11-small {
        margin-left: 91.66667%; }
      .row > .col-12-small {
        width: 100%; }
      .row > .off-12-small {
        margin-left: 100%; }
      .row.gtr-0 {
        margin-top: 0;
        margin-left: 0em; }
        .row.gtr-0 > * {
          padding: 0 0 0 0em; }
        .row.gtr-0.gtr-uniform {
          margin-top: 0em; }
          .row.gtr-0.gtr-uniform > * {
            padding-top: 0em; }
      .row.gtr-25 {
        margin-top: 0;
        margin-left: -0.375em; }
        .row.gtr-25 > * {
          padding: 0 0 0 0.375em; }
        .row.gtr-25.gtr-uniform {
          margin-top: -0.375em; }
          .row.gtr-25.gtr-uniform > * {
            padding-top: 0.375em; }
      .row.gtr-50 {
        margin-top: 0;
        margin-left: -0.75em; }
        .row.gtr-50 > * {
          padding: 0 0 0 0.75em; }
        .row.gtr-50.gtr-uniform {
          margin-top: -0.75em; }
          .row.gtr-50.gtr-uniform > * {
            padding-top: 0.75em; }
      .row {
        margin-top: 0;
        margin-left: -1.5em; }
        .row > * {
          padding: 0 0 0 1.5em; }
        .row.gtr-uniform {
          margin-top: -1.5em; }
          .row.gtr-uniform > * {
            padding-top: 1.5em; }
      .row.gtr-150 {
        margin-top: 0;
        margin-left: -2.25em; }
        .row.gtr-150 > * {
          padding: 0 0 0 2.25em; }
        .row.gtr-150.gtr-uniform {
          margin-top: -2.25em; }
          .row.gtr-150.gtr-uniform > * {
            padding-top: 2.25em; }
      .row.gtr-200 {
        margin-top: 0;
        margin-left: -3em; }
        .row.gtr-200 > * {
          padding: 0 0 0 3em; }
        .row.gtr-200.gtr-uniform {
          margin-top: -3em; }
          .row.gtr-200.gtr-uniform > * {
            padding-top: 3em; } }
  @media screen and (max-width: 480px) {
    .row {
      display: flex;
      flex-wrap: wrap;
      box-sizing: border-box;
      align-items: stretch; }
      .row > * {
        box-sizing: border-box; }
      .row.gtr-uniform > * > :last-child {
        margin-bottom: 0; }
      .row.aln-left {
        justify-content: flex-start; }
      .row.aln-center {
        justify-content: center; }
      .row.aln-right {
        justify-content: flex-end; }
      .row.aln-top {
        align-items: flex-start; }
      .row.aln-middle {
        align-items: center; }
      .row.aln-bottom {
        align-items: flex-end; }
      .row > .imp-xsmall {
        order: -1; }
      .row > .col-1-xsmall {
        width: 8.33333%; }
      .row > .off-1-xsmall {
        margin-left: 8.33333%; }
      .row > .col-2-xsmall {
        width: 16.66667%; }
      .row > .off-2-xsmall {
        margin-left: 16.66667%; }
      .row > .col-3-xsmall {
        width: 25%; }
      .row > .off-3-xsmall {
        margin-left: 25%; }
      .row > .col-4-xsmall {
        width: 33.33333%; }
      .row > .off-4-xsmall {
        margin-left: 33.33333%; }
      .row > .col-5-xsmall {
        width: 41.66667%; }
      .row > .off-5-xsmall {
        margin-left: 41.66667%; }
      .row > .col-6-xsmall {
        width: 50%; }
      .row > .off-6-xsmall {
        margin-left: 50%; }
      .row > .col-7-xsmall {
        width: 58.33333%; }
      .row > .off-7-xsmall {
        margin-left: 58.33333%; }
      .row > .col-8-xsmall {
        width: 66.66667%; }
      .row > .off-8-xsmall {
        margin-left: 66.66667%; }
      .row > .col-9-xsmall {
        width: 75%; }
      .row > .off-9-xsmall {
        margin-left: 75%; }
      .row > .col-10-xsmall {
        width: 83.33333%; }
      .row > .off-10-xsmall {
        margin-left: 83.33333%; }
      .row > .col-11-xsmall {
        width: 91.66667%; }
      .row > .off-11-xsmall {
        margin-left: 91.66667%; }
      .row > .col-12-xsmall {
        width: 100%; }
      .row > .off-12-xsmall {
        margin-left: 100%; }
      .row.gtr-0 {
        margin-top: 0;
        margin-left: 0em; }
        .row.gtr-0 > * {
          padding: 0 0 0 0em; }
        .row.gtr-0.gtr-uniform {
          margin-top: 0em; }
          .row.gtr-0.gtr-uniform > * {
            padding-top: 0em; }
      .row.gtr-25 {
        margin-top: 0;
        margin-left: -0.375em; }
        .row.gtr-25 > * {
          padding: 0 0 0 0.375em; }
        .row.gtr-25.gtr-uniform {
          margin-top: -0.375em; }
          .row.gtr-25.gtr-uniform > * {
            padding-top: 0.375em; }
      .row.gtr-50 {
        margin-top: 0;
        margin-left: -0.75em; }
        .row.gtr-50 > * {
          padding: 0 0 0 0.75em; }
        .row.gtr-50.gtr-uniform {
          margin-top: -0.75em; }
          .row.gtr-50.gtr-uniform > * {
            padding-top: 0.75em; }
      .row {
        margin-top: 0;
        margin-left: -1.5em; }
        .row > * {
          padding: 0 0 0 1.5em; }
        .row.gtr-uniform {
          margin-top: -1.5em; }
          .row.gtr-uniform > * {
            padding-top: 1.5em; }
      .row.gtr-150 {
        margin-top: 0;
        margin-left: -2.25em; }
        .row.gtr-150 > * {
          padding: 0 0 0 2.25em; }
        .row.gtr-150.gtr-uniform {
          margin-top: -2.25em; }
          .row.gtr-150.gtr-uniform > * {
            padding-top: 2.25em; }
      .row.gtr-200 {
        margin-top: 0;
        margin-left: -3em; }
        .row.gtr-200 > * {
          padding: 0 0 0 3em; }
        .row.gtr-200.gtr-uniform {
          margin-top: -3em; }
          .row.gtr-200.gtr-uniform > * {
            padding-top: 3em; } }

/* Section/Article */
section.special, article.special {
  text-align: center; }

header p {
  font-family: "Roboto Slab", serif;
  font-size: 1em;
  font-weight: 400;
  letter-spacing: 0.075em;
  margin-top: -0.5em;
  text-transform: uppercase; }

header.major > :last-child {
  border-bottom: solid 3px #f56a6a;
  display: inline-block;
  margin: 0 0 2em 0;
  padding: 0 0.75em 0.5em 0; }

header.main > :last-child {
  margin: 0 0 1em 0; }

/* Form */
form {
  margin: 0 0 2em 0; }

label {
  color: #3d4449;
  display: block;
  font-size: 0.9em;
  font-weight: 600;
  margin: 0 0 1em 0; }

input[type="text"],
input[type="password"],
input[type="email"],
input[type="tel"],
input[type="search"],
input[type="url"],
select,
textarea {
  -moz-appearance: none;
  -webkit-appearance: none;
  -ms-appearance: none;
  appearance: none;
  background: #ffffff;
  border-radius: 0.375em;
  border: none;
  border: solid 1px rgba(210, 215, 217, 0.75);
  color: inherit;
  display: block;
  outline: 0;
  padding: 0 1em;
  text-decoration: none;
  width: 100%; }
  input[type="text"]:invalid,
  input[type="password"]:invalid,
  input[type="email"]:invalid,
  input[type="tel"]:invalid,
  input[type="search"]:invalid,
  input[type="url"]:invalid,
  select:invalid,
  textarea:invalid {
    box-shadow: none; }
  input[type="text"]:focus,
  input[type="password"]:focus,
  input[type="email"]:focus,
  input[type="tel"]:focus,
  input[type="search"]:focus,
  input[type="url"]:focus,
  select:focus,
  textarea:focus {
    border-color: #f56a6a;
    box-shadow: 0 0 0 1px #f56a6a; }

select {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' preserveAspectRatio='none' viewBox='0 0 40 40'%3E%3Cpath d='M9.4,12.3l10.4,10.4l10.4-10.4c0.2-0.2,0.5-0.4,0.9-0.4c0.3,0,0.6,0.1,0.9,0.4l3.3,3.3c0.2,0.2,0.4,0.5,0.4,0.9 c0,0.4-0.1,0.6-0.4,0.9L20.7,31.9c-0.2,0.2-0.5,0.4-0.9,0.4c-0.3,0-0.6-0.1-0.9-0.4L4.3,17.3c-0.2-0.2-0.4-0.5-0.4-0.9 c0-0.4,0.1-0.6,0.4-0.9l3.3-3.3c0.2-0.2,0.5-0.4,0.9-0.4S9.1,12.1,9.4,12.3z' fill='rgba(210, 215, 217, 0.75)' /%3E%3C/svg%3E");
  background-size: 1.25em;
  background-repeat: no-repeat;
  background-position: calc(100% - 1em) center;
  height: 2.75em;
  padding-right: 2.75em;
  text-overflow: ellipsis; }
  select option {
    color: #3d4449;
    background: #ffffff; }
  select:focus::-ms-value {
    background-color: transparent; }
  select::-ms-expand {
    display: none; }

input[type="text"],
input[type="password"],
input[type="email"],
input[type="tel"],
input[type="search"],
input[type="url"],
select {
  height: 2.75em; }

textarea {
  padding: 0.75em 1em; }

input[type="checkbox"],
input[type="radio"] {
  -moz-appearance: none;
  -webkit-appearance: none;
  -ms-appearance: none;
  appearance: none;
  display: block;
  float: left;
  margin-right: -2em;
  opacity: 0;
  width: 1em;
  z-index: -1; }
  input[type="checkbox"] + label,
  input[type="radio"] + label {
    text-decoration: none;
    color: #7f888f;
    cursor: pointer;
    display: inline-block;
    font-size: 1em;
    font-weight: 400;
    padding-left: 2.4em;
    padding-right: 0.75em;
    position: relative; }
    input[type="checkbox"] + label:before,
    input[type="radio"] + label:before {
      -moz-osx-font-smoothing: grayscale;
      -webkit-font-smoothing: antialiased;
      display: inline-block;
      font-style: normal;
      font-variant: normal;
      text-rendering: auto;
      line-height: 1;
      text-transform: none !important;
      font-family: 'Font Awesome 5 Free';
      font-weight: 900; }
    input[type="checkbox"] + label:before,
    input[type="radio"] + label:before {
      background: #ffffff;
      border-radius: 0.375em;
      border: solid 1px rgba(210, 215, 217, 0.75);
      content: '';
      display: inline-block;
      font-size: 0.8em;
      height: 2.0625em;
      left: 0;
      line-height: 2.0625em;
      position: absolute;
      text-align: center;
      top: 0;
      width: 2.0625em; }
  input[type="checkbox"]:checked + label:before,
  input[type="radio"]:checked + label:before {
    background: #3d4449;
    border-color: #3d4449;
    color: #ffffff;
    content: '\\f00c'; }
  input[type="checkbox"]:focus + label:before,
  input[type="radio"]:focus + label:before {
    border-color: #f56a6a;
    box-shadow: 0 0 0 1px #f56a6a; }

input[type="checkbox"] + label:before {
  border-radius: 0.375em; }

input[type="radio"] + label:before {
  border-radius: 100%; }

::-webkit-input-placeholder {
  color: #9fa3a6 !important;
  opacity: 1.0; }

:-moz-placeholder {
  color: #9fa3a6 !important;
  opacity: 1.0; }

::-moz-placeholder {
  color: #9fa3a6 !important;
  opacity: 1.0; }

:-ms-input-placeholder {
  color: #9fa3a6 !important;
  opacity: 1.0; }

/* Box */
.box {
  border-radius: 0.375em;
  border: solid 1px rgba(210, 215, 217, 0.75);
  margin-bottom: 2em;
  padding: 1.5em; }
  .box > :last-child,
  .box > :last-child > :last-child,
  .box > :last-child > :last-child > :last-child {
    margin-bottom: 0; }
  .box.alt {
    border: 0;
    border-radius: 0;
    padding: 0; }

/* Icon */
.icon {
  text-decoration: none;
  border-bottom: none;
  position: relative; }
  .icon:before {
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
    display: inline-block;
    font-style: normal;
    font-variant: normal;
    text-rendering: auto;
    line-height: 1;
    text-transform: none !important;
    font-family: 'Font Awesome 5 Free';
    font-weight: 400; }
  .icon > .label {
    display: none; }
  .icon:before {
    line-height: inherit; }
  .icon.solid:before {
    font-weight: 900; }
  .icon.brands:before {
    font-family: 'Font Awesome 5 Brands'; }

/* Image */
.image {
  border-radius: 0.375em;
  border: 0;
  display: inline-block;
  position: relative; }
  .image img {
    border-radius: 0.375em;
    display: block; }
  .image.left, .image.right {
    max-width: 40%; }
    .image.left img, .image.right img {
      width: 100%; }
  .image.left {
    float: left;
    padding: 0 1.5em 1em 0;
    top: 0.25em; }
  .image.right {
    float: right;
    padding: 0 0 1em 1.5em;
    top: 0.25em; }
  .image.fit {
    display: block;
    margin: 0 0 2em 0;
    width: 100%; }
    .image.fit img {
      width: 100%; }
  .image.main {
    display: block;
    margin: 0 0 3em 0;
    width: 100%; }
    .image.main img {
      width: 100%; }

a.image {
  overflow: hidden; }
  a.image img {
    -moz-transition: -moz-transform 0.2s ease;
    -webkit-transition: -webkit-transform 0.2s ease;
    -ms-transition: -ms-transform 0.2s ease;
    transition: transform 0.2s ease; }
  a.image:hover img {
    -moz-transform: scale(1.075);
    -webkit-transform: scale(1.075);
    -ms-transform: scale(1.075);
    transform: scale(1.075); }

/* List */
ol {
  list-style: decimal;
  margin: 0 0 2em 0;
  padding-left: 1.25em; }
  ol li {
    padding-left: 0.25em; }

ul {
  list-style: disc;
  margin: 0 0 2em 0;
  padding-left: 1em; }
  ul li {
    padding-left: 0.5em; }
  ul.alt {
    list-style: none;
    padding-left: 0; }
    ul.alt li {
      border-top: solid 1px rgba(210, 215, 217, 0.75);
      padding: 0.5em 0; }
      ul.alt li:first-child {
        border-top: 0;
        padding-top: 0; }

dl {
  margin: 0 0 2em 0; }
  dl dt {
    display: block;
    font-weight: 600;
    margin: 0 0 1em 0; }
  dl dd {
    margin-left: 2em; }

/* Actions */
ul.actions {
  display: -moz-flex;
  display: -webkit-flex;
  display: -ms-flex;
  display: flex;
  cursor: default;
  list-style: none;
  margin-left: -1em;
  padding-left: 0; }
  ul.actions li {
    padding: 0 0 0 1em;
    vertical-align: middle; }
  ul.actions.special {
    -moz-justify-content: center;
    -webkit-justify-content: center;
    -ms-justify-content: center;
    justify-content: center;
    width: 100%;
    margin-left: 0; }
    ul.actions.special li:first-child {
      padding-left: 0; }
  ul.actions.stacked {
    -moz-flex-direction: column;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column;
    margin-left: 0; }
    ul.actions.stacked li {
      padding: 1.3em 0 0 0; }
      ul.actions.stacked li:first-child {
        padding-top: 0; }
  ul.actions.fit {
    width: calc(100% + 1em); }
    ul.actions.fit li {
      -moz-flex-grow: 1;
      -webkit-flex-grow: 1;
      -ms-flex-grow: 1;
      flex-grow: 1;
      -moz-flex-shrink: 1;
      -webkit-flex-shrink: 1;
      -ms-flex-shrink: 1;
      flex-shrink: 1;
      width: 100%; }
      ul.actions.fit li > * {
        width: 100%; }
    ul.actions.fit.stacked {
      width: 100%; }

/* Icons */
ul.icons {
  cursor: default;
  list-style: none;
  padding-left: 0; }
  ul.icons li {
    display: inline-block;
    padding: 0 1em 0 0; }
    ul.icons li:last-child {
      padding-right: 0; }
    ul.icons li .icon {
      color: inherit; }
      ul.icons li .icon:before {
        font-size: 1.25em; }

/* Contact */
ul.contact {
  list-style: none;
  padding: 0; }
  ul.contact li {
    text-decoration: none;
    border-top: solid 1px rgba(210, 215, 217, 0.75);
    margin: 1.5em 0 0 0;
    padding: 1.5em 0 0 3em;
    position: relative; }
    ul.contact li:before {
      -moz-osx-font-smoothing: grayscale;
      -webkit-font-smoothing: antialiased;
      display: inline-block;
      font-style: normal;
      font-variant: normal;
      text-rendering: auto;
      line-height: 1;
      text-transform: none !important;
      font-family: 'Font Awesome 5 Free';
      font-weight: 400; }
    ul.contact li:before {
      color: #f56a6a;
      display: inline-block;
      font-size: 1.5em;
      height: 1.125em;
      left: 0;
      line-height: 1.125em;
      position: absolute;
      text-align: center;
      top: 1em;
      width: 1.5em; }
    ul.contact li:first-child {
      border-top: 0;
      margin-top: 0;
      padding-top: 0; }
      ul.contact li:first-child:before {
        top: 0; }
    ul.contact li a {
      color: inherit; }

/* Pagination */
ul.pagination {
  cursor: default;
  list-style: none;
  padding-left: 0; }
  ul.pagination li {
    display: inline-block;
    padding-left: 0;
    vertical-align: middle; }
    ul.pagination li > .page {
      -moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      -webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      -ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      border-bottom: 0;
      border-radius: 0.375em;
      display: inline-block;
      font-size: 0.8em;
      font-weight: 600;
      height: 2em;
      line-height: 2em;
      margin: 0 0.125em;
      min-width: 2em;
      padding: 0 0.5em;
      text-align: center; }
      ul.pagination li > .page.active {
        background-color: #f56a6a;
        color: #ffffff !important; }
        ul.pagination li > .page.active:hover {
          background-color: #f67878; }
        ul.pagination li > .page.active:active {
          background-color: #f45c5c; }
    ul.pagination li:first-child {
      padding-right: 0.75em; }
    ul.pagination li:last-child {
      padding-left: 0.75em; }
  @media screen and (max-width: 480px) {
    ul.pagination li:nth-child(n+2):nth-last-child(n+2) {
      display: none; }
    ul.pagination li:first-child {
      padding-right: 0; } }

/* Table */
.table-wrapper {
  -webkit-overflow-scrolling: touch;
  overflow-x: auto; }

table {
  margin: 0 0 2em 0;
  width: 100%; }
  table tbody tr {
    border: solid 1px rgba(210, 215, 217, 0.75);
    border-left: 0;
    border-right: 0; }
    table tbody tr:nth-child(2n + 1) {
      background-color: rgba(230, 235, 237, 0.25); }
  table td {
    padding: 0.75em 0.75em; }
  table th {
    color: #3d4449;
    font-size: 0.9em;
    font-weight: 600;
    padding: 0 0.75em 0.75em 0.75em;
    text-align: left; }
  table thead {
    border-bottom: solid 2px rgba(210, 215, 217, 0.75); }
  table tfoot {
    border-top: solid 2px rgba(210, 215, 217, 0.75); }
  table.alt {
    border-collapse: separate; }
    table.alt tbody tr td {
      border: solid 1px rgba(210, 215, 217, 0.75);
      border-left-width: 0;
      border-top-width: 0; }
      table.alt tbody tr td:first-child {
        border-left-width: 1px; }
    table.alt tbody tr:first-child td {
      border-top-width: 1px; }
    table.alt thead {
      border-bottom: 0; }
    table.alt tfoot {
      border-top: 0; }

/* Button */
input[type="submit"],
input[type="reset"],
input[type="button"],
button,
.button {
  -moz-appearance: none;
  -webkit-appearance: none;
  -ms-appearance: none;
  appearance: none;
  -moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
  -webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
  -ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
  transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
  background-color: transparent;
  border-radius: 0.375em;
  border: 0;
  box-shadow: inset 0 0 0 2px #f56a6a;
  color: #f56a6a !important;
  cursor: pointer;
  display: inline-block;
  font-family: "Roboto Slab", serif;
  font-size: 0.8em;
  font-weight: 700;
  height: 3.5em;
  letter-spacing: 0.075em;
  line-height: 3.5em;
  padding: 0 2.25em;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;
  white-space: nowrap; }
  input[type="submit"]:hover,
  input[type="reset"]:hover,
  input[type="button"]:hover,
  button:hover,
  .button:hover {
    background-color: rgba(245, 106, 106, 0.05); }
  input[type="submit"]:active,
  input[type="reset"]:active,
  input[type="button"]:active,
  button:active,
  .button:active {
    background-color: rgba(245, 106, 106, 0.15); }
  input[type="submit"].icon:before,
  input[type="reset"].icon:before,
  input[type="button"].icon:before,
  button.icon:before,
  .button.icon:before {
    margin-right: 0.5em; }
  input[type="submit"].fit,
  input[type="reset"].fit,
  input[type="button"].fit,
  button.fit,
  .button.fit {
    width: 100%; }
  input[type="submit"].small,
  input[type="reset"].small,
  input[type="button"].small,
  button.small,
  .button.small {
    font-size: 0.6em; }
  input[type="submit"].large,
  input[type="reset"].large,
  input[type="button"].large,
  button.large,
  .button.large {
    font-size: 1em;
    height: 3.65em;
    line-height: 3.65em; }
  input[type="submit"].primary,
  input[type="reset"].primary,
  input[type="button"].primary,
  button.primary,
  .button.primary {
    background-color: #f56a6a;
    box-shadow: none;
    color: #ffffff !important; }
    input[type="submit"].primary:hover,
    input[type="reset"].primary:hover,
    input[type="button"].primary:hover,
    button.primary:hover,
    .button.primary:hover {
      background-color: #f67878; }
    input[type="submit"].primary:active,
    input[type="reset"].primary:active,
    input[type="button"].primary:active,
    button.primary:active,
    .button.primary:active {
      background-color: #f45c5c; }
  input[type="submit"].disabled, input[type="submit"]:disabled,
  input[type="reset"].disabled,
  input[type="reset"]:disabled,
  input[type="button"].disabled,
  input[type="button"]:disabled,
  button.disabled,
  button:disabled,
  .button.disabled,
  .button:disabled {
    pointer-events: none;
    opacity: 0.25; }

/* Mini Posts */
.mini-posts article {
  border-top: solid 1px rgba(210, 215, 217, 0.75);
  margin-top: 2em;
  padding-top: 2em; }
  .mini-posts article .image {
    display: block;
    margin: 0 0 1.5em 0; }
    .mini-posts article .image img {
      display: block;
      width: 100%; }
  .mini-posts article:first-child {
    border-top: 0;
    margin-top: 0;
    padding-top: 0; }

/* Features */
.features {
  display: -moz-flex;
  display: -webkit-flex;
  display: -ms-flex;
  display: flex;
  -moz-flex-wrap: wrap;
  -webkit-flex-wrap: wrap;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  margin: 0 0 2em -3em;
  width: calc(100% + 3em); }
  .features article {
    -moz-align-items: center;
    -webkit-align-items: center;
    -ms-align-items: center;
    align-items: center;
    display: -moz-flex;
    display: -webkit-flex;
    display: -ms-flex;
    display: flex;
    margin: 0 0 3em 3em;
    position: relative;
    width: calc(50% - 3em); }
    .features article:nth-child(2n - 1) {
      margin-right: 1.5em; }
    .features article:nth-child(2n) {
      margin-left: 1.5em; }
    .features article:nth-last-child(1), .features article:nth-last-child(2) {
      margin-bottom: 0; }
    .features article .icon {
      -moz-flex-grow: 0;
      -webkit-flex-grow: 0;
      -ms-flex-grow: 0;
      flex-grow: 0;
      -moz-flex-shrink: 0;
      -webkit-flex-shrink: 0;
      -ms-flex-shrink: 0;
      flex-shrink: 0;
      display: block;
      height: 10em;
      line-height: 10em;
      margin: 0 2em 0 0;
      text-align: center;
      width: 10em; }
      .features article .icon:before {
        color: #f56a6a;
        font-size: 2.75rem;
        position: relative;
        top: 0.05em; }
      .features article .icon:after {
        -moz-transform: rotate(45deg);
        -webkit-transform: rotate(45deg);
        -ms-transform: rotate(45deg);
        transform: rotate(45deg);
        border-radius: 0.25rem;
        border: solid 2px rgba(210, 215, 217, 0.75);
        content: '';
        display: block;
        height: 7em;
        left: 50%;
        margin: -3.5em 0 0 -3.5em;
        position: absolute;
        top: 50%;
        width: 7em; }
    .features article .content {
      -moz-flex-grow: 1;
      -webkit-flex-grow: 1;
      -ms-flex-grow: 1;
      flex-grow: 1;
      -moz-flex-shrink: 1;
      -webkit-flex-shrink: 1;
      -ms-flex-shrink: 1;
      flex-shrink: 1;
      width: 100%; }
      .features article .content > :last-child {
        margin-bottom: 0; }
  @media screen and (max-width: 980px) {
    .features {
      margin: 0 0 2em 0;
      width: 100%; }
      .features article {
        margin: 0 0 3em 0;
        width: 100%; }
        .features article:nth-child(2n - 1) {
          margin-right: 0; }
        .features article:nth-child(2n) {
          margin-left: 0; }
        .features article:nth-last-child(1), .features article:nth-last-child(2) {
          margin-bottom: 3em; }
        .features article:last-child {
          margin-bottom: 0; }
        .features article .icon {
          height: 8em;
          line-height: 8em;
          width: 8em; }
          .features article .icon:before {
            font-size: 2.25rem; }
          .features article .icon:after {
            height: 6em;
            margin: -3em 0 0 -3em;
            width: 6em; } }
  @media screen and (max-width: 480px) {
    .features article {
      -moz-flex-direction: column;
      -webkit-flex-direction: column;
      -ms-flex-direction: column;
      flex-direction: column;
      -moz-align-items: -moz-flex-start;
      -webkit-align-items: -webkit-flex-start;
      -ms-align-items: -ms-flex-start;
      align-items: flex-start; }
      .features article .icon {
        height: 6em;
        line-height: 6em;
        margin: 0 0 1.5em 0;
        width: 6em; }
        .features article .icon:before {
          font-size: 1.5rem; }
        .features article .icon:after {
          height: 4em;
          margin: -2em 0 0 -2em;
          width: 4em; } }
  @media screen and (max-width: 480px) {
    .features article .icon:before {
      font-size: 1.25rem; } }

/* Posts */
.posts {
  display: -moz-flex;
  display: -webkit-flex;
  display: -ms-flex;
  display: flex;
  -moz-flex-wrap: wrap;
  -webkit-flex-wrap: wrap;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  margin: 0 0 2em -6em;
  width: calc(100% + 6em); }
  .posts article {
    -moz-flex-grow: 0;
    -webkit-flex-grow: 0;
    -ms-flex-grow: 0;
    flex-grow: 0;
    -moz-flex-shrink: 1;
    -webkit-flex-shrink: 1;
    -ms-flex-shrink: 1;
    flex-shrink: 1;
    margin: 0 0 6em 6em;
    position: relative;
    width: calc(33.33333% - 6em); }
    .posts article:before {
      background: rgba(210, 215, 217, 0.75);
      content: '';
      display: block;
      height: calc(100% + 6em);
      left: -3em;
      position: absolute;
      top: 0;
      width: 1px; }
    .posts article:after {
      background: rgba(210, 215, 217, 0.75);
      bottom: -3em;
      content: '';
      display: block;
      height: 1px;
      position: absolute;
      right: 0;
      width: calc(100% + 6em); }
    .posts article > :last-child {
      margin-bottom: 0; }
    .posts article .image {
      display: block;
      margin: 0 0 2em 0; }
      .posts article .image img {
        display: block;
        width: 100%; }
  @media screen and (min-width: 1681px) {
    .posts article:nth-child(3n + 1):before {
      display: none; }
    .posts article:nth-child(3n + 1):after {
      width: 100%; }
    .posts article:nth-last-child(1), .posts article:nth-last-child(2), .posts article:nth-last-child(3) {
      margin-bottom: 0; }
      .posts article:nth-last-child(1):before, .posts article:nth-last-child(2):before, .posts article:nth-last-child(3):before {
        height: 100%; }
      .posts article:nth-last-child(1):after, .posts article:nth-last-child(2):after, .posts article:nth-last-child(3):after {
        display: none; } }
  @media screen and (max-width: 1680px) {
    .posts article {
      width: calc(50% - 6em); }
      .posts article:nth-last-child(3) {
        margin-bottom: 6em; } }
  @media screen and (min-width: 481px) and (max-width: 1680px) {
    .posts article:nth-child(2n + 1):before {
      display: none; }
    .posts article:nth-child(2n + 1):after {
      width: 100%; }
    .posts article:nth-last-child(1), .posts article:nth-last-child(2) {
      margin-bottom: 0; }
      .posts article:nth-last-child(1):before, .posts article:nth-last-child(2):before {
        height: 100%; }
      .posts article:nth-last-child(1):after, .posts article:nth-last-child(2):after {
        display: none; } }
  @media screen and (max-width: 736px) {
    .posts {
      margin: 0 0 2em -4.5em;
      width: calc(100% + 4.5em); }
      .posts article {
        margin: 0 0 4.5em 4.5em;
        width: calc(50% - 4.5em); }
        .posts article:before {
          height: calc(100% + 4.5em);
          left: -2.25em; }
        .posts article:after {
          bottom: -2.25em;
          width: calc(100% + 4.5em); }
        .posts article:nth-last-child(3) {
          margin-bottom: 4.5em; } }
  @media screen and (max-width: 480px) {
    .posts {
      margin: 0 0 2em 0;
      width: 100%; }
      .posts article {
        margin: 0 0 4.5em 0;
        width: 100%; }
        .posts article:before {
          display: none; }
        .posts article:after {
          width: 100%; }
        .posts article:last-child {
          margin-bottom: 0; }
          .posts article:last-child:after {
            display: none; } }

/* Wrapper */
#wrapper {
  display: -moz-flex;
  display: -webkit-flex;
  display: -ms-flex;
  display: flex;
  -moz-flex-direction: row-reverse;
  -webkit-flex-direction: row-reverse;
  -ms-flex-direction: row-reverse;
  flex-direction: row-reverse;
  min-height: 100vh; }

/* Main */
#main {
  -moz-flex-grow: 1;
  -webkit-flex-grow: 1;
  -ms-flex-grow: 1;
  flex-grow: 1;
  -moz-flex-shrink: 1;
  -webkit-flex-shrink: 1;
  -ms-flex-shrink: 1;
  flex-shrink: 1;
  width: 100%; }
  #main > .inner {
    padding: 0 6em 0.1em 6em ;
    margin: 0 auto;
    max-width: 110em; }
    #main > .inner > section {
      padding: 6em 0 4em 0 ;
      border-top: solid 2px rgba(210, 215, 217, 0.75); }
      #main > .inner > section:first-of-type {
        border-top: 0 !important; }
  @media screen and (max-width: 1680px) {
    #main > .inner {
      padding: 0 5em 0.1em 5em ; }
      #main > .inner > section {
        padding: 5em 0 3em 0 ; } }
  @media screen and (max-width: 1280px) {
    #main > .inner {
      padding: 0 4em 0.1em 4em ; }
      #main > .inner > section {
        padding: 4em 0 2em 0 ; } }
  @media screen and (max-width: 736px) {
    #main > .inner {
      padding: 0 2em 0.1em 2em ; }
      #main > .inner > section {
        padding: 3em 0 1em 0 ; } }

/* Sidebar */
#search form {
  text-decoration: none;
  position: relative; }
  #search form:before {
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
    display: inline-block;
    font-style: normal;
    font-variant: normal;
    text-rendering: auto;
    line-height: 1;
    text-transform: none !important;
    font-family: 'Font Awesome 5 Free';
    font-weight: 900; }
  #search form:before {
    -moz-transform: scaleX(-1);
    -webkit-transform: scaleX(-1);
    -ms-transform: scaleX(-1);
    transform: scaleX(-1);
    color: #7f888f;
    content: '\\f002';
    cursor: default;
    display: block;
    font-size: 1.5em;
    height: 2em;
    line-height: 2em;
    opacity: 0.325;
    position: absolute;
    right: 0;
    text-align: center;
    top: 0;
    width: 2em; }
  #search form input[type="text"] {
    padding-right: 2.75em; }

#sidebar {
  -moz-flex-grow: 0;
  -webkit-flex-grow: 0;
  -ms-flex-grow: 0;
  flex-grow: 0;
  -moz-flex-shrink: 0;
  -webkit-flex-shrink: 0;
  -ms-flex-shrink: 0;
  flex-shrink: 0;
  -moz-transition: margin-left 0.5s ease, box-shadow 0.5s ease;
  -webkit-transition: margin-left 0.5s ease, box-shadow 0.5s ease;
  -ms-transition: margin-left 0.5s ease, box-shadow 0.5s ease;
  transition: margin-left 0.5s ease, box-shadow 0.5s ease;
  background-color: #f5f6f7;
  font-size: 0.9em;
  position: relative;
  width: 26em; }
  #sidebar h2 {
    font-size: 1.38889em; }
  #sidebar > .inner {
    padding: 2.22222em 2.22222em 2.44444em 2.22222em ;
    position: relative;
    width: 26em; }
    #sidebar > .inner > * {
      border-bottom: solid 2px rgba(210, 215, 217, 0.75);
      margin: 0 0 3.5em 0;
      padding: 0 0 3.5em 0; }
      #sidebar > .inner > * > :last-child {
        margin-bottom: 0; }
      #sidebar > .inner > *:last-child {
        border-bottom: 0;
        margin-bottom: 0;
        padding-bottom: 0; }
    #sidebar > .inner > .alt {
      background-color: #eff1f2;
      border-bottom: 0;
      margin: -2.22222em 0 4.44444em -2.22222em;
      padding: 2.22222em;
      width: calc(100% + 4.44444em); }
  #sidebar .toggle {
    text-decoration: none;
    -moz-transition: left 0.5s ease;
    -webkit-transition: left 0.5s ease;
    -ms-transition: left 0.5s ease;
    transition: left 0.5s ease;
    -webkit-tap-highlight-color: rgba(255, 255, 255, 0);
    border: 0;
    display: block;
    height: 7.5em;
    left: 26em;
    line-height: 7.5em;
    outline: 0;
    overflow: hidden;
    position: absolute;
    text-align: center;
    text-indent: -15em;
    white-space: nowrap;
    top: 0;
    width: 6em;
    z-index: 10000; }
    #sidebar .toggle:before {
      -moz-osx-font-smoothing: grayscale;
      -webkit-font-smoothing: antialiased;
      display: inline-block;
      font-style: normal;
      font-variant: normal;
      text-rendering: auto;
      line-height: 1;
      text-transform: none !important;
      font-family: 'Font Awesome 5 Free';
      font-weight: 900; }
    #sidebar .toggle:before {
      content: '\\f0c9';
      font-size: 2rem;
      height: inherit;
      left: 0;
      line-height: inherit;
      position: absolute;
      text-indent: 0;
      top: 0;
      width: inherit; }
  #sidebar.inactive {
    margin-left: -26em; }
  @media screen and (max-width: 1680px) {
    #sidebar {
      width: 24em; }
      #sidebar > .inner {
        padding: 1.66667em 1.66667em 1.33333em 1.66667em ;
        width: 24em; }
        #sidebar > .inner > .alt {
          margin: -1.66667em 0 3.33333em -1.66667em;
          padding: 1.66667em;
          width: calc(100% + 3.33333em); }
      #sidebar .toggle {
        height: 6.25em;
        left: 24em;
        line-height: 6.25em;
        text-indent: 5em;
        width: 5em; }
        #sidebar .toggle:before {
          font-size: 1.5rem; }
      #sidebar.inactive {
        margin-left: -24em; } }
  @media screen and (max-width: 1280px) {
    #sidebar {
      box-shadow: 0 0 5em 0 rgba(0, 0, 0, 0.175);
      height: 100%;
      left: 0;
      position: fixed;
      top: 0;
      z-index: 10000; }
      #sidebar.inactive {
        box-shadow: none; }
      #sidebar > .inner {
        -webkit-overflow-scrolling: touch;
        height: 100%;
        left: 0;
        overflow-x: hidden;
        overflow-y: auto;
        position: absolute;
        top: 0; }
        #sidebar > .inner:after {
          content: '';
          display: block;
          height: 4em;
          width: 100%; }
      #sidebar .toggle {
        text-indent: 6em;
        width: 6em; }
        #sidebar .toggle:before {
          font-size: 1.5rem;
          margin-left: -0.4375em; }
      body.is-preload #sidebar {
        display: none; } }
  @media screen and (max-width: 736px) {
    #sidebar .toggle {
      text-indent: 7.25em;
      width: 7.25em; }
      #sidebar .toggle:before {
        color: #7f888f;
        margin-left: -0.0625em;
        margin-top: -0.25em;
        font-size: 1.1rem;
        z-index: 1; }
      #sidebar .toggle:after {
        background: rgba(222, 225, 226, 0.75);
        border-radius: 0.375em;
        content: '';
        height: 3.5em;
        left: 1em;
        position: absolute;
        top: 1em;
        width: 5em; } }

/* Header */
#header {
  display: -moz-flex;
  display: -webkit-flex;
  display: -ms-flex;
  display: flex;
  border-bottom: solid 5px #f56a6a;
  padding: 6em 0 1em 0;
  position: relative; }
  #header > * {
    -moz-flex: 1;
    -webkit-flex: 1;
    -ms-flex: 1;
    flex: 1;
    margin-bottom: 0; }
  #header .logo {
    border-bottom: 0;
    color: inherit;
    font-family: "Roboto Slab", serif;
    font-size: 1.125em; }
  #header .icons {
    text-align: right; }
  @media screen and (max-width: 1680px) {
    #header {
      padding-top: 5em; } }
  @media screen and (max-width: 736px) {
    #header {
      padding-top: 6.5em; }
      #header .logo {
        font-size: 1.25em;
        margin: 0; }
      #header .icons {
        height: 5em;
        line-height: 5em;
        position: absolute;
        right: -0.5em;
        top: 0; } }

/* Banner */
#banner {
  padding: 6em 0 4em 0 ;
  display: -moz-flex;
  display: -webkit-flex;
  display: -ms-flex;
  display: flex; }
  #banner h1 {
    margin-top: -0.125em; }
  #banner .content {
    -moz-flex-grow: 1;
    -webkit-flex-grow: 1;
    -ms-flex-grow: 1;
    flex-grow: 1;
    -moz-flex-shrink: 1;
    -webkit-flex-shrink: 1;
    -ms-flex-shrink: 1;
    flex-shrink: 1;
    width: 50%; }
  #banner .image {
    -moz-flex-grow: 0;
    -webkit-flex-grow: 0;
    -ms-flex-grow: 0;
    flex-grow: 0;
    -moz-flex-shrink: 0;
    -webkit-flex-shrink: 0;
    -ms-flex-shrink: 0;
    flex-shrink: 0;
    display: block;
    margin: 0 0 2em 4em;
    width: 50%; }
    #banner .image img {
      height: 100%;
      -moz-object-fit: cover;
      -webkit-object-fit: cover;
      -ms-object-fit: cover;
      object-fit: cover;
      -moz-object-position: center;
      -webkit-object-position: center;
      -ms-object-position: center;
      object-position: center;
      width: 100%; }
  @media screen and (orientation: portrait) {
    #banner {
      -moz-flex-direction: column-reverse;
      -webkit-flex-direction: column-reverse;
      -ms-flex-direction: column-reverse;
      flex-direction: column-reverse; }
      #banner h1 br {
        display: none; }
      #banner .content {
        -moz-flex-grow: 0;
        -webkit-flex-grow: 0;
        -ms-flex-grow: 0;
        flex-grow: 0;
        -moz-flex-shrink: 0;
        -webkit-flex-shrink: 0;
        -ms-flex-shrink: 0;
        flex-shrink: 0;
        width: 100%; }
      #banner .image {
        -moz-flex-grow: 0;
        -webkit-flex-grow: 0;
        -ms-flex-grow: 0;
        flex-grow: 0;
        -moz-flex-shrink: 0;
        -webkit-flex-shrink: 0;
        -ms-flex-shrink: 0;
        flex-shrink: 0;
        margin: 0 0 4em 0;
        height: 25em;
        max-height: 50vh;
        min-height: 18em;
        width: 100%; } }
  @media screen and (orientation: portrait) and (max-width: 480px) {
    #banner .image {
      max-height: 35vh; } }

/* Footer */
#footer .copyright {
  color: #9fa3a6;
  font-size: 0.9em; }
  #footer .copyright a {
    color: inherit; }

/* Menu */
#menu ul {
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
  user-select: none;
  color: #3d4449;
  font-family: "Roboto Slab", serif;
  font-weight: 400;
  letter-spacing: 0.075em;
  list-style: none;
  margin-bottom: 0;
  padding: 0;
  text-transform: uppercase; }
  #menu ul a, #menu ul span {
    border-bottom: 0;
    color: inherit;
    cursor: pointer;
    display: block;
    font-size: 0.9em;
    padding: 0.625em 0; }
    #menu ul a:hover, #menu ul span:hover {
      color: #f56a6a; }
    #menu ul a.opener, #menu ul span.opener {
      -moz-transition: color 0.2s ease-in-out;
      -webkit-transition: color 0.2s ease-in-out;
      -ms-transition: color 0.2s ease-in-out;
      transition: color 0.2s ease-in-out;
      text-decoration: none;
      -webkit-tap-highlight-color: rgba(255, 255, 255, 0);
      position: relative; }
      #menu ul a.opener:before, #menu ul span.opener:before {
        -moz-osx-font-smoothing: grayscale;
        -webkit-font-smoothing: antialiased;
        display: inline-block;
        font-style: normal;
        font-variant: normal;
        text-rendering: auto;
        line-height: 1;
        text-transform: none !important;
        font-family: 'Font Awesome 5 Free';
        font-weight: 900; }
      #menu ul a.opener:before, #menu ul span.opener:before {
        -moz-transition: color 0.2s ease-in-out, -moz-transform 0.2s ease-in-out;
        -webkit-transition: color 0.2s ease-in-out, -webkit-transform 0.2s ease-in-out;
        -ms-transition: color 0.2s ease-in-out, -ms-transform 0.2s ease-in-out;
        transition: color 0.2s ease-in-out, transform 0.2s ease-in-out;
        color: #9fa3a6;
        content: '\\f078';
        position: absolute;
        right: 0; }
      #menu ul a.opener:hover:before, #menu ul span.opener:hover:before {
        color: #f56a6a; }
      #menu ul a.opener.active + ul, #menu ul span.opener.active + ul {
        display: block; }
      #menu ul a.opener.active:before, #menu ul span.opener.active:before {
        -moz-transform: rotate(-180deg);
        -webkit-transform: rotate(-180deg);
        -ms-transform: rotate(-180deg);
        transform: rotate(-180deg); }

#menu > ul > li {
  border-top: solid 1px rgba(210, 215, 217, 0.75);
  margin: 0.5em 0 0 0;
  padding: 0.5em 0 0 0; }
  #menu > ul > li > ul {
    color: #9fa3a6;
    display: none;
    margin: 0.5em 0 1.5em 0;
    padding-left: 1em; }
    #menu > ul > li > ul a, #menu > ul > li > ul span {
      font-size: 0.8em; }
    #menu > ul > li > ul > li {
      margin: 0.125em 0 0 0;
      padding: 0.125em 0 0 0; }
  #menu > ul > li:first-child {
    border-top: 0;
    margin-top: 0;
    padding-top: 0; }
    body {
      background-color: #F8EDED;
      color: #173B45; /* Text color */
    }
    
    /* Header Background and Text Color */
    header {
      background-color: #F8EDED;
      color: #173B45;
    }
    
    /* Section Background and Text Color */
    section {
      background-color: #F8EDED;
      color: #173B45;
    }
    
    /* Footer Background and Text Color */
    footer {
      background-color: #F8EDED;
      color: #F8EDED;
    }
    
    /* Links Color */
    a {
      color: #173B45;
    }
    
    a:hover {
      color: #FF8225;
    }
    
    /* Buttons */
    .button {
      background-color: #173B45;
      color: #B43F3F;
      border: 2px solid #B43F3F;
      box-shadow: inset 0 0 0 2px #173B45;
    }
    
    .button:hover {
      background-color: #FF8225;
      color: #F8EDED;
    }
    
    .post {
      background-color: #F8EDED;
      color: #173B45;
    }
    
    /* Other elements */
    h1, h2, h3, h4, h5, h6 {
      color: #173B45;
    }
    
    p {
      color: #173B45;
    }
    
    #sidebar {
      background-color: #F8EDED;
    }
    
    #search {
      background-color: #F8EDED;
    }
    
    #menu {
      color: #173B45;
    }
    
    #menu ul a, #menu ul span {
      border-bottom: 0;
      color: #173B45;
      display: block;
      padding: 0.625em 0;
    }
    
    .button {
      -moz-appearance: none;
      -webkit-appearance: none;
      -ms-appearance: none;
      appearance: none;
      -moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      -webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      -ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      background-color: transparent;
      border-radius: 0.375em;
      border: 0;
      box-shadow: inset 0 0 0 2px #173B45;
      color: #173B45 !important;
      cursor: pointer;
      display: inline-block;
      font-family: "Roboto Slab", serif;
      font-size: 0.8em;
      font-weight: 700;
      height: 3.5em;
      letter-spacing: 0.075em;
      line-height: 3.5em;
      padding: 0 2.25em;
      text-align: center;
      text-decoration: none;
      text-transform: uppercase;
      white-space: nowrap;
    }
    
    #sidebar > .inner > .alt {
      background-color: #F8EDED;
    }
    
    #search form {
      background-color: #173B45;
    }
""",
     "lime": """    body {
      background-color: #F6E96B;
      color: #387F39; /* Text color */
  }
  
  /* Header Background and Text Color */
  header {
      background-color: #F6E96B;
      color: #387F39;
  }
  
  /* Section Background and Text Color */
  section {
      background-color: #F6E96B;
      color: #387F39;
  }
  
  /* Footer Background and Text Color */
  footer {
      background-color: #F6E96B;;
      color: #F6E96B;
  }
  
  /* Links Color */
  a {
      color: #387F39;
  }
  
  a:hover {
      color: #A2CA71;
  }
  
  /* Buttons */
  .button {
      background-color: #BEDC74;
      color: #387F39;
      border: 2px solid #387F39;
      box-shadow: inset 0 0 0 2px #BEDC74;
      color: #BEDC74;
  }
  
  .button:hover {
      background-color: #A2CA71;
      color: #F6E96B;

  }
  .post {
      background-color: #F6E96B;
      color: #F6E96B;
  }
  
  /* Other elements */
  h1, h2, h3, h4, h5, h6 {
      color: #387F39;
  }
  
  p {
      color: #387F39;
  }
  #sidebar 
  {
    background-color: #F6E96B;
  }
  #search 
  {
    background-color: #F6E96B;
  }
  #menu
  {
    color: #387F39;
  }""",
     "valley": """    body {
      background-color: #C9DABF;
      color: #5F6F65; /* Text color */
    }

    /* Header Background and Text Color */
    header {
      background-color: #C9DABF;
      color: #5F6F65;
    }

    /* Section Background and Text Color */
    section {
      background-color: #C9DABF;
      color: #5F6F65;
    }

    /* Footer Background and Text Color */
    footer {
      background-color: #C9DABF;
      color: #C9DABF;
    }

    /* Links Color */
    a {
      color: #5F6F65;
    }

    a:hover {
      color: #9CA986;
    }

    /* Buttons */
    .button {
      background-color: #5F6F65;
      color: #5F6F65;
      border: 2px solid #5F6F65;
      box-shadow: inset 0 0 0 2px #5F6F65;
    }

    .button:hover {
      background-color: #808D7C;
      color: #C9DABF;
    }

    .post {
      background-color: #C9DABF;
      color: #5F6F65;
    }

    /* Other elements */
    h1, h2, h3, h4, h5, h6 {
      color: #5F6F65;
    }

    p {
      color: #5F6F65;
    }

    #sidebar {
      background-color: #C9DABF;
    }

    #search {
      background-color: #C9DABF;
    }

    #menu {
      color: #5F6F65;
    }

    #menu ul a, #menu ul span {
      border-bottom: 0;
      color: #5F6F65;
      display: block;
      padding: 0.625em 0;
    }

    .button {
      -moz-appearance: none;
      -webkit-appearance: none;
      -ms-appearance: none;
      appearance: none;
      -moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      -webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      -ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      background-color: transparent;
      border-radius: 0.375em;
      border: 0;
      box-shadow: inset 0 0 0 2px #5F6F65;
      color: #5F6F65 !important;
      cursor: pointer;
      display: inline-block;
      font-family: "Roboto Slab", serif;
      font-size: 0.8em;
      font-weight: 700;
      height: 3.5em;
      letter-spacing: 0.075em;
      line-height: 3.5em;
      padding: 0 2.25em;
      text-align: center;
      text-decoration: none;
      text-transform: uppercase;
      white-space: nowrap;
    }

    #sidebar > .inner > .alt {
      background-color: #C9DABF;
    }

    #search form {
      background-color: #5F6F65;
    }""",
     "sakura" : """    body {
      background-color: #FF8C9E;
      color: #FFEBD4; /* Text color */
    }
    
    /* Header Background and Text Color */
    header {
      background-color: #FF8C9E;
      color: #FFC6C6;
    }
    
    /* Section Background and Text Color */
    section {
      background-color: #FF8C9E;
      color: #FFEBD4;
    }
    
    /* Footer Background and Text Color */
    footer {
      background-color: #FF8C9E;
      color: #FF8C9E;
    }
    
    /* Links Color */
    a {
      color: #FFEBD4;
    }
    
    a:hover {
      color: #F0A8D0;
    }
    
    /* Buttons */
    .button {
      background-color: #FFEBD4;
      color: #FFC6C6;
      border: 2px solid #FFC6C6;
      box-shadow: inset 0 0 0 2px #FFEBD4;
    }
    
    .button:hover {
      background-color: #F7B5CA;
      color: #FF8C9E;
    }
    
    .post {
      background-color: #FF8C9E;
      color: #FFEBD4;
    }
    
    /* Other elements */
    h1, h2, h3, h4, h5, h6 {
      color: #FFEBD4;
    }
    
    p {
      color: #FFEBD4;
    }
    
    #sidebar {
      background-color: #FF8C9E;
    }
    
    #search {
      background-color: #FF8C9E;
    }
    
    #menu {
      color: #FFC6C6;
    }
    
    #menu ul a, #menu ul span {
      border-bottom: 0;
      color: #FFEBD4;
      display: block;
      padding: 0.625em 0;
    }
    
    .button {
      -moz-appearance: none;
      -webkit-appearance: none;
      -ms-appearance: none;
      appearance: none;
      -moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      -webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      -ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      background-color: transparent;
      border-radius: 0.375em;
      border: 0;
      box-shadow: inset 0 0 0 2px #FFEBD4;
      color: #FFEBD4 !important;
      cursor: pointer;
      display: inline-block;
      font-family: "Roboto Slab", serif;
      font-size: 0.8em;
      font-weight: 700;
      height: 3.5em;
      letter-spacing: 0.075em;
      line-height: 3.5em;
      padding: 0 2.25em;
      text-align: center;
      text-decoration: none;
      text-transform: uppercase;
      white-space: nowrap;
    }
    
    #sidebar > .inner > .alt {
      background-color: #FF8C9E;
    }
    
    #search form {
      background-color: #FFEBD4;
    }
    """,
     "phantom": """    body {
      background-color: #17153B;
      color: #C8ACD6; /* Text color */
    }
    
    /* Header Background and Text Color */
    header {
      background-color: #17153B;
      color: #433D8B;
    }
    
    /* Section Background and Text Color */
    section {
      background-color: #17153B;
      color: #C8ACD6;
    }
    
    /* Footer Background and Text Color */
    footer {
      background-color: #17153B;
      color: #17153B;
    }
    
    /* Links Color */
    a {
      color: #C8ACD6;
    }
    
    a:hover {
      color: #2E236C;
    }
    
    /* Buttons */
    .button {
      background-color: #C8ACD6;
      color: #433D8B;
      border: 2px solid #433D8B;
      box-shadow: inset 0 0 0 2px #C8ACD6;
      color: #C8ACD6;
    }
    
    .button:hover {
      background-color: #2E236C;
      color: #17153B;
    }
    
    .post {
      background-color: #17153B;
      color: #C8ACD6;
    }
    
    /* Other elements */
    h1, h2, h3, h4, h5, h6 {
      color: #C8ACD6;
    }
    
    p {
      color: #C8ACD6;
    }
    
    #sidebar {
      background-color: #17153B;
    }
    
    #search {
      background-color: #17153B;
    }
    
    #menu {
      color: #433D8B;
    }
    #menu ul a, #menu ul span {
      border-bottom: 0;
      color: #C8ACD6;
      display: block;
      padding: 0.625em 0;
  }
  .button {
    -moz-appearance: none;
    -webkit-appearance: none;
    -ms-appearance: none;
    appearance: none;
    -moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
    -webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
    -ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
    transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
    background-color: transparent;
    border-radius: 0.375em;
    border: 0;
    box-shadow: inset 0 0 0 2px #C8ACD6;
    color: #C8ACD6 !important;
    cursor: pointer;
    display: inline-block;
    font-family: "Roboto Slab", serif;
    font-size: 0.8em;
    font-weight: 700;
    height: 3.5em;
    letter-spacing: 0.075em;
    line-height: 3.5em;
    padding: 0 2.25em;
    text-align: center;
    text-decoration: none;
    text-transform: uppercase;
    white-space: nowrap;
}
#sidebar > .inner > .alt {
  background-color: #17153B;
}
#search form{
  background-color: #C8ACD6;
}""", "elegant": """    body {
      background-color: #F8EDED;
      color: #173B45; /* Text color */
    }
    
    /* Header Background and Text Color */
    header {
      background-color: #F8EDED;
      color: #173B45;
    }
    
    /* Section Background and Text Color */
    section {
      background-color: #F8EDED;
      color: #173B45;
    }
    
    /* Footer Background and Text Color */
    footer {
      background-color: #F8EDED;
      color: #F8EDED;
    }
    
    /* Links Color */
    a {
      color: #173B45;
    }
    
    a:hover {
      color: #FF8225;
    }
    
    /* Buttons */
    .button {
      background-color: #173B45;
      color: #B43F3F;
      border: 2px solid #B43F3F;
      box-shadow: inset 0 0 0 2px #173B45;
    }
    
    .button:hover {
      background-color: #FF8225;
      color: #F8EDED;
    }
    
    .post {
      background-color: #F8EDED;
      color: #173B45;
    }
    
    /* Other elements */
    h1, h2, h3, h4, h5, h6 {
      color: #173B45;
    }
    
    p {
      color: #173B45;
    }
    
    #sidebar {
      background-color: #F8EDED;
    }
    
    #search {
      background-color: #F8EDED;
    }
    
    #menu {
      color: #173B45;
    }
    
    #menu ul a, #menu ul span {
      border-bottom: 0;
      color: #173B45;
      display: block;
      padding: 0.625em 0;
    }
    
    .button {
      -moz-appearance: none;
      -webkit-appearance: none;
      -ms-appearance: none;
      appearance: none;
      -moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      -webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      -ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
      background-color: transparent;
      border-radius: 0.375em;
      border: 0;
      box-shadow: inset 0 0 0 2px #173B45;
      color: #173B45 !important;
      cursor: pointer;
      display: inline-block;
      font-family: "Roboto Slab", serif;
      font-size: 0.8em;
      font-weight: 700;
      height: 3.5em;
      letter-spacing: 0.075em;
      line-height: 3.5em;
      padding: 0 2.25em;
      text-align: center;
      text-decoration: none;
      text-transform: uppercase;
      white-space: nowrap;
    }
    
    #sidebar > .inner > .alt {
      background-color: #F8EDED;
    }
    
    #search form {
      background-color: #173B45;
    }
    """
},
"reader": {"default":"""@import url("fontawesome-all.min.css");
@import url("https://fonts.googleapis.com/css?family=Lato:400,400italic,700,700italic|Source+Code+Pro:400");

/*
	Read Only by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #fff;
	}

		body.is-preload *, body.is-preload *:before, body.is-preload *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

	body, input, select, textarea {
		color: #888;
		font-family: "Lato", sans-serif;
		font-size: 16pt;
		font-weight: 400;
		line-height: 1.75em;
	}

	a {
		-moz-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-webkit-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-ms-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		border-bottom: solid 1px #e4e4e4;
		color: inherit;
		text-decoration: none;
	}

		a:hover {
			border-bottom-color: transparent;
			color: #4acaa8 !important;
		}

	strong, b {
		color: #777;
		font-weight: 700;
	}

	em, i {
		font-style: italic;
	}

	p {
		margin: 0 0 2.25em 0;
	}

	h1, h2, h3, h4, h5, h6 {
		color: #777;
		font-weight: 700;
		line-height: 1em;
		margin: 0 0 0.5625em 0;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			border: 0;
			color: inherit;
			text-decoration: none;
		}

	h2 {
		font-size: 2em;
		line-height: 1.5em;
	}

	h3 {
		font-size: 1.75em;
		line-height: 1.5em;
	}

	h4 {
		font-size: 1.25em;
		line-height: 1.5em;
	}

	h5 {
		font-size: 0.9em;
		line-height: 1.5em;
	}

	h6 {
		font-size: 0.7em;
		line-height: 1.5em;
	}

	sub {
		font-size: 0.8em;
		position: relative;
		top: 0.5em;
	}

	sup {
		font-size: 0.8em;
		position: relative;
		top: -0.5em;
	}

	hr {
		border: 0;
		border-bottom: solid 2px #f4f4f4;
		margin: 2.25em 0;
	}

		hr.major {
			margin: 3.375em 0;
		}

	blockquote {
		border-left: solid 8px #e4e4e4;
		font-style: italic;
		margin: 0 0 2.25em 0;
		padding: 0.5em 0 0.5em 2em;
	}

	code {
		background: #555;
		border-radius: 5px;
		color: #fff;
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0.25em;
		padding: 0.25em 0.65em;
	}

	pre {
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0 2.25em 0;
	}

		pre code {
			-webkit-overflow-scrolling: touch;
			display: block;
			line-height: 1.5em;
			overflow-x: auto;
			padding: 1em 1.5em;
		}

	.align-left {
		text-align: left;
	}

	.align-center {
		text-align: center;
	}

	.align-right {
		text-align: right;
	}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0;
			margin-left: 0em;
		}

			.row.gtr-0 > * {
				padding: 0 0 0 0em;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0em;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0em;
				}

		.row.gtr-25 {
			margin-top: 0;
			margin-left: -0.5em;
		}

			.row.gtr-25 > * {
				padding: 0 0 0 0.5em;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -0.5em;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 0.5em;
				}

		.row.gtr-50 {
			margin-top: 0;
			margin-left: -1em;
		}

			.row.gtr-50 > * {
				padding: 0 0 0 1em;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -1em;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 1em;
				}

		.row {
			margin-top: 0;
			margin-left: -2em;
		}

			.row > * {
				padding: 0 0 0 2em;
			}

			.row.gtr-uniform {
				margin-top: -2em;
			}

				.row.gtr-uniform > * {
					padding-top: 2em;
				}

		.row.gtr-150 {
			margin-top: 0;
			margin-left: -3em;
		}

			.row.gtr-150 > * {
				padding: 0 0 0 3em;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -3em;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 3em;
				}

		.row.gtr-200 {
			margin-top: 0;
			margin-left: -4em;
		}

			.row.gtr-200 > * {
				padding: 0 0 0 4em;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -4em;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 4em;
				}

		@media screen and (max-width: 1680px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xlarge {
					order: -1;
				}

				.row > .col-1-xlarge {
					width: 8.33333%;
				}

				.row > .off-1-xlarge {
					margin-left: 8.33333%;
				}

				.row > .col-2-xlarge {
					width: 16.66667%;
				}

				.row > .off-2-xlarge {
					margin-left: 16.66667%;
				}

				.row > .col-3-xlarge {
					width: 25%;
				}

				.row > .off-3-xlarge {
					margin-left: 25%;
				}

				.row > .col-4-xlarge {
					width: 33.33333%;
				}

				.row > .off-4-xlarge {
					margin-left: 33.33333%;
				}

				.row > .col-5-xlarge {
					width: 41.66667%;
				}

				.row > .off-5-xlarge {
					margin-left: 41.66667%;
				}

				.row > .col-6-xlarge {
					width: 50%;
				}

				.row > .off-6-xlarge {
					margin-left: 50%;
				}

				.row > .col-7-xlarge {
					width: 58.33333%;
				}

				.row > .off-7-xlarge {
					margin-left: 58.33333%;
				}

				.row > .col-8-xlarge {
					width: 66.66667%;
				}

				.row > .off-8-xlarge {
					margin-left: 66.66667%;
				}

				.row > .col-9-xlarge {
					width: 75%;
				}

				.row > .off-9-xlarge {
					margin-left: 75%;
				}

				.row > .col-10-xlarge {
					width: 83.33333%;
				}

				.row > .off-10-xlarge {
					margin-left: 83.33333%;
				}

				.row > .col-11-xlarge {
					width: 91.66667%;
				}

				.row > .off-11-xlarge {
					margin-left: 91.66667%;
				}

				.row > .col-12-xlarge {
					width: 100%;
				}

				.row > .off-12-xlarge {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -1em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 1em;
						}

				.row {
					margin-top: 0;
					margin-left: -2em;
				}

					.row > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-uniform > * {
							padding-top: 2em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 3em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -4em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 4em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -4em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 4em;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-large {
					order: -1;
				}

				.row > .col-1-large {
					width: 8.33333%;
				}

				.row > .off-1-large {
					margin-left: 8.33333%;
				}

				.row > .col-2-large {
					width: 16.66667%;
				}

				.row > .off-2-large {
					margin-left: 16.66667%;
				}

				.row > .col-3-large {
					width: 25%;
				}

				.row > .off-3-large {
					margin-left: 25%;
				}

				.row > .col-4-large {
					width: 33.33333%;
				}

				.row > .off-4-large {
					margin-left: 33.33333%;
				}

				.row > .col-5-large {
					width: 41.66667%;
				}

				.row > .off-5-large {
					margin-left: 41.66667%;
				}

				.row > .col-6-large {
					width: 50%;
				}

				.row > .off-6-large {
					margin-left: 50%;
				}

				.row > .col-7-large {
					width: 58.33333%;
				}

				.row > .off-7-large {
					margin-left: 58.33333%;
				}

				.row > .col-8-large {
					width: 66.66667%;
				}

				.row > .off-8-large {
					margin-left: 66.66667%;
				}

				.row > .col-9-large {
					width: 75%;
				}

				.row > .off-9-large {
					margin-left: 75%;
				}

				.row > .col-10-large {
					width: 83.33333%;
				}

				.row > .off-10-large {
					margin-left: 83.33333%;
				}

				.row > .col-11-large {
					width: 91.66667%;
				}

				.row > .off-11-large {
					margin-left: 91.66667%;
				}

				.row > .col-12-large {
					width: 100%;
				}

				.row > .off-12-large {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 1024px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-medium {
					order: -1;
				}

				.row > .col-1-medium {
					width: 8.33333%;
				}

				.row > .off-1-medium {
					margin-left: 8.33333%;
				}

				.row > .col-2-medium {
					width: 16.66667%;
				}

				.row > .off-2-medium {
					margin-left: 16.66667%;
				}

				.row > .col-3-medium {
					width: 25%;
				}

				.row > .off-3-medium {
					margin-left: 25%;
				}

				.row > .col-4-medium {
					width: 33.33333%;
				}

				.row > .off-4-medium {
					margin-left: 33.33333%;
				}

				.row > .col-5-medium {
					width: 41.66667%;
				}

				.row > .off-5-medium {
					margin-left: 41.66667%;
				}

				.row > .col-6-medium {
					width: 50%;
				}

				.row > .off-6-medium {
					margin-left: 50%;
				}

				.row > .col-7-medium {
					width: 58.33333%;
				}

				.row > .off-7-medium {
					margin-left: 58.33333%;
				}

				.row > .col-8-medium {
					width: 66.66667%;
				}

				.row > .off-8-medium {
					margin-left: 66.66667%;
				}

				.row > .col-9-medium {
					width: 75%;
				}

				.row > .off-9-medium {
					margin-left: 75%;
				}

				.row > .col-10-medium {
					width: 83.33333%;
				}

				.row > .off-10-medium {
					margin-left: 83.33333%;
				}

				.row > .col-11-medium {
					width: 91.66667%;
				}

				.row > .off-11-medium {
					margin-left: 91.66667%;
				}

				.row > .col-12-medium {
					width: 100%;
				}

				.row > .off-12-medium {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-small {
					order: -1;
				}

				.row > .col-1-small {
					width: 8.33333%;
				}

				.row > .off-1-small {
					margin-left: 8.33333%;
				}

				.row > .col-2-small {
					width: 16.66667%;
				}

				.row > .off-2-small {
					margin-left: 16.66667%;
				}

				.row > .col-3-small {
					width: 25%;
				}

				.row > .off-3-small {
					margin-left: 25%;
				}

				.row > .col-4-small {
					width: 33.33333%;
				}

				.row > .off-4-small {
					margin-left: 33.33333%;
				}

				.row > .col-5-small {
					width: 41.66667%;
				}

				.row > .off-5-small {
					margin-left: 41.66667%;
				}

				.row > .col-6-small {
					width: 50%;
				}

				.row > .off-6-small {
					margin-left: 50%;
				}

				.row > .col-7-small {
					width: 58.33333%;
				}

				.row > .off-7-small {
					margin-left: 58.33333%;
				}

				.row > .col-8-small {
					width: 66.66667%;
				}

				.row > .off-8-small {
					margin-left: 66.66667%;
				}

				.row > .col-9-small {
					width: 75%;
				}

				.row > .off-9-small {
					margin-left: 75%;
				}

				.row > .col-10-small {
					width: 83.33333%;
				}

				.row > .off-10-small {
					margin-left: 83.33333%;
				}

				.row > .col-11-small {
					width: 91.66667%;
				}

				.row > .off-11-small {
					margin-left: 91.66667%;
				}

				.row > .col-12-small {
					width: 100%;
				}

				.row > .off-12-small {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

		@media screen and (max-width: 480px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xsmall {
					order: -1;
				}

				.row > .col-1-xsmall {
					width: 8.33333%;
				}

				.row > .off-1-xsmall {
					margin-left: 8.33333%;
				}

				.row > .col-2-xsmall {
					width: 16.66667%;
				}

				.row > .off-2-xsmall {
					margin-left: 16.66667%;
				}

				.row > .col-3-xsmall {
					width: 25%;
				}

				.row > .off-3-xsmall {
					margin-left: 25%;
				}

				.row > .col-4-xsmall {
					width: 33.33333%;
				}

				.row > .off-4-xsmall {
					margin-left: 33.33333%;
				}

				.row > .col-5-xsmall {
					width: 41.66667%;
				}

				.row > .off-5-xsmall {
					margin-left: 41.66667%;
				}

				.row > .col-6-xsmall {
					width: 50%;
				}

				.row > .off-6-xsmall {
					margin-left: 50%;
				}

				.row > .col-7-xsmall {
					width: 58.33333%;
				}

				.row > .off-7-xsmall {
					margin-left: 58.33333%;
				}

				.row > .col-8-xsmall {
					width: 66.66667%;
				}

				.row > .off-8-xsmall {
					margin-left: 66.66667%;
				}

				.row > .col-9-xsmall {
					width: 75%;
				}

				.row > .off-9-xsmall {
					margin-left: 75%;
				}

				.row > .col-10-xsmall {
					width: 83.33333%;
				}

				.row > .off-10-xsmall {
					margin-left: 83.33333%;
				}

				.row > .col-11-xsmall {
					width: 91.66667%;
				}

				.row > .off-11-xsmall {
					margin-left: 91.66667%;
				}

				.row > .col-12-xsmall {
					width: 100%;
				}

				.row > .off-12-xsmall {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

/* Container */

	.container {
		margin: 0 auto;
		max-width: calc(100% - 4.5em);
		width: 45em;
	}

		.container.xsmall {
			width: 11.25em;
		}

		.container.small {
			width: 22.5em;
		}

		.container.medium {
			width: 33.75em;
		}

		.container.large {
			width: 56.25em;
		}

		.container.xlarge {
			width: 67.5em;
		}

		.container.max {
			width: 100%;
		}

		@media screen and (max-width: 1024px) {

			.container {
				width: 100% !important;
			}

		}

		@media screen and (max-width: 480px) {

			.container {
				max-width: calc(100% - 3.375em);
			}

		}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header p {
		color: #aaa;
		position: relative;
		margin: 0 0 1.6875em 0;
	}

	header h2 + p {
		font-size: 1.25em;
		margin-top: -0.5em;
		line-height: 1.5em;
	}

	header h3 + p {
		font-size: 1.1em;
		margin-top: -0.35em;
		line-height: 1.5em;
	}

	header h4 + p,
	header h5 + p,
	header h6 + p {
		font-size: 0.9em;
		margin-top: -0.25em;
		line-height: 1.5em;
	}

	header.major h2 {
		color: #4acaa8;
		font-size: 3.5em;
	}

		header.major h2 + p {
			color: #777;
			font-size: 1.75em;
			font-weight: 700;
			margin-top: -0.75em;
		}

/* Form */

	form {
		margin: 0 0 2.25em 0;
	}

	label {
		color: #777;
		display: block;
		font-size: 0.9em;
		font-weight: 700;
		margin: 0 0 1.125em 0;
	}

	input::-moz-focus-inner {
		border: 0;
		padding: 0;
	}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select,
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		border-radius: 5px;
		border: none;
		border: solid 2px #e4e4e4;
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 1em;
		text-decoration: none;
		width: 100%;
	}

		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		select:focus,
		textarea:focus {
			border-color: #4acaa8;
		}

	select {
		background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' preserveAspectRatio='none' viewBox='0 0 40 40'%3E%3Cpath d='M9.4,12.3l10.4,10.4l10.4-10.4c0.2-0.2,0.5-0.4,0.9-0.4c0.3,0,0.6,0.1,0.9,0.4l3.3,3.3c0.2,0.2,0.4,0.5,0.4,0.9 c0,0.4-0.1,0.6-0.4,0.9L20.7,31.9c-0.2,0.2-0.5,0.4-0.9,0.4c-0.3,0-0.6-0.1-0.9-0.4L4.3,17.3c-0.2-0.2-0.4-0.5-0.4-0.9 c0-0.4,0.1-0.6,0.4-0.9l3.3-3.3c0.2-0.2,0.5-0.4,0.9-0.4S9.1,12.1,9.4,12.3z' fill='%23e4e4e4' /%3E%3C/svg%3E");
		background-size: 1.25em;
		background-repeat: no-repeat;
		background-position: calc(100% - 1em) center;
		height: 2.75em;
		padding-right: 2.75em;
		text-overflow: ellipsis;
	}

		select option {
			color: #777;
			background: #fff;
		}

		select:focus::-ms-value {
			background-color: transparent;
		}

		select::-ms-expand {
			display: none;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 2.75em;
	}

	textarea {
		padding: 0.75em 1em;
	}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2em;
		opacity: 0;
		width: 1em;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			color: #888;
			cursor: pointer;
			display: inline-block;
			font-size: 1em;
			font-weight: 400;
			padding-left: 2.4em;
			padding-right: 0.75em;
			position: relative;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				background: #fafafa;
				border-radius: 5px;
				border: solid 2px #e4e4e4;
				content: '';
				display: inline-block;
				font-size: 0.8em;
				height: 2.0625em;
				left: 0;
				line-height: 2.0625em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.0625em;
			}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			background: #989898;
			border-color: #989898;
			color: #ffffff;
			content: '\\f00c';
		}

		input[type="checkbox"]:focus + label:before,
		input[type="radio"]:focus + label:before {
			border-color: #4acaa8;
		}

	input[type="checkbox"] + label:before {
		border-radius: 5px;
	}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	::-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

/* Box */

	.box {
		border-radius: 5px;
		border: solid 2px #e4e4e4;
		margin-bottom: 2.25em;
		padding: 1.5em;
	}

		.box > :last-child,
		.box > :last-child > :last-child,
		.box > :last-child > :last-child > :last-child {
			margin-bottom: 0;
		}

		.box.alt {
			border: 0;
			border-radius: 0;
			padding: 0;
		}

/* Icon */

	.icon {
		text-decoration: none;
		border-bottom: none;
		position: relative;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 400;
		}

		.icon > .label {
			display: none;
		}

		.icon:before {
			line-height: inherit;
		}

		.icon.solid:before {
			font-weight: 900;
		}

		.icon.brands:before {
			font-family: 'Font Awesome 5 Brands';
		}

/* Image */

	.image {
		border-radius: 5px;
		border: 0;
		display: inline-block;
		position: relative;
	}

		.image[data-position] img {
			-moz-object-fit: cover;
			-webkit-object-fit: cover;
			-ms-object-fit: cover;
			object-fit: cover;
			display: block;
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
		}

		.image[data-position="top left"] img {
			-moz-object-position: top left;
			-webkit-object-position: top left;
			-ms-object-position: top left;
			object-position: top left;
		}

		.image[data-position="top"] img {
			-moz-object-position: top;
			-webkit-object-position: top;
			-ms-object-position: top;
			object-position: top;
		}

		.image[data-position="top right"] img {
			-moz-object-position: top right;
			-webkit-object-position: top right;
			-ms-object-position: top right;
			object-position: top right;
		}

		.image[data-position="right"] img {
			-moz-object-position: right;
			-webkit-object-position: right;
			-ms-object-position: right;
			object-position: right;
		}

		.image[data-position="bottom right"] img {
			-moz-object-position: bottom right;
			-webkit-object-position: bottom right;
			-ms-object-position: bottom right;
			object-position: bottom right;
		}

		.image[data-position="bottom"] img {
			-moz-object-position: bottom;
			-webkit-object-position: bottom;
			-ms-object-position: bottom;
			object-position: bottom;
		}

		.image[data-position="bottom left"] img {
			-moz-object-position: bottom left;
			-webkit-object-position: bottom left;
			-ms-object-position: bottom left;
			object-position: bottom left;
		}

		.image[data-position="left"] img {
			-moz-object-position: left;
			-webkit-object-position: left;
			-ms-object-position: left;
			object-position: left;
		}

		.image[data-position="center"] img {
			-moz-object-position: center;
			-webkit-object-position: center;
			-ms-object-position: center;
			object-position: center;
		}

		.image[data-position="25% 25%"] img {
			-moz-object-position: 25% 25%;
			-webkit-object-position: 25% 25%;
			-ms-object-position: 25% 25%;
			object-position: 25% 25%;
		}

		.image[data-position="75% 25%"] img {
			-moz-object-position: 75% 25%;
			-webkit-object-position: 75% 25%;
			-ms-object-position: 75% 25%;
			object-position: 75% 25%;
		}

		.image[data-position="75% 75%"] img {
			-moz-object-position: 75% 75%;
			-webkit-object-position: 75% 75%;
			-ms-object-position: 75% 75%;
			object-position: 75% 75%;
		}

		.image[data-position="25% 75%"] img {
			-moz-object-position: 25% 75%;
			-webkit-object-position: 25% 75%;
			-ms-object-position: 25% 75%;
			object-position: 25% 75%;
		}

		.image img {
			border-radius: 5px;
			display: block;
		}

		.image.left {
			float: left;
			margin: 0 2.5em 2em 0;
			top: 0.25em;
		}

		.image.right {
			float: right;
			margin: 0 0 2em 2.5em;
			top: 0.25em;
		}

		.image.fit {
			display: block;
			margin: 0 0 2.25em 0;
			width: 100%;
		}

			.image.fit img {
				display: block;
				width: 100%;
			}

		.image.avatar {
			border-radius: 100%;
			overflow: hidden;
		}

			.image.avatar img {
				border-radius: 100%;
				display: block;
				width: 100%;
			}

		.image.main {
			display: block;
			height: 20em;
			border-radius: 0;
		}

			.image.main img {
				border-radius: 0;
			}

/* List */

	ol {
		list-style: decimal;
		margin: 0 0 2.25em 0;
		padding-left: 1.25em;
	}

		ol li {
			padding-left: 0.25em;
		}

	ul {
		list-style: disc;
		margin: 0 0 2.25em 0;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
		}

		ul.alt {
			list-style: none;
			padding-left: 0;
		}

			ul.alt li {
				border-top: solid 2px #f4f4f4;
				padding: 0.5em 0;
			}

				ul.alt li:first-child {
					border-top: 0;
					padding-top: 0;
				}

	dl {
		margin: 0 0 2.25em 0;
	}

/* Actions */

	ul.actions {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		cursor: default;
		list-style: none;
		margin-left: -1.125em;
		padding-left: 0;
	}

		ul.actions li {
			padding: 0 0 0 1.125em;
			vertical-align: middle;
		}

		ul.actions.special {
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 100%;
			margin-left: 0;
		}

			ul.actions.special li:first-child {
				padding-left: 0;
			}

		ul.actions.stacked {
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			margin-left: 0;
		}

			ul.actions.stacked li {
				padding: 1.125em 0 0 0;
			}

				ul.actions.stacked li:first-child {
					padding-top: 0;
				}

		ul.actions.fit {
			width: calc(100% + 1.125em);
		}

			ul.actions.fit li {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				width: 100%;
			}

				ul.actions.fit li > * {
					width: 100%;
				}

			ul.actions.fit.stacked {
				width: 100%;
			}

		@media screen and (max-width: 480px) {

			ul.actions:not(.fixed) {
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
				margin-left: 0;
				width: 100% !important;
			}

				ul.actions:not(.fixed) li {
					-moz-flex-grow: 1;
					-webkit-flex-grow: 1;
					-ms-flex-grow: 1;
					flex-grow: 1;
					-moz-flex-shrink: 1;
					-webkit-flex-shrink: 1;
					-ms-flex-shrink: 1;
					flex-shrink: 1;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions:not(.fixed) li > * {
						width: 100%;
					}

					ul.actions:not(.fixed) li:first-child {
						padding-top: 0;
					}

					ul.actions:not(.fixed) li input[type="submit"],
					ul.actions:not(.fixed) li input[type="reset"],
					ul.actions:not(.fixed) li input[type="button"],
					ul.actions:not(.fixed) li button,
					ul.actions:not(.fixed) li .button {
						width: 100%;
					}

						ul.actions:not(.fixed) li input[type="submit"].icon:before,
						ul.actions:not(.fixed) li input[type="reset"].icon:before,
						ul.actions:not(.fixed) li input[type="button"].icon:before,
						ul.actions:not(.fixed) li button.icon:before,
						ul.actions:not(.fixed) li .button.icon:before {
							margin-left: -0.5rem;
						}

		}

/* Feature Icons */

	ul.feature-icons {
		list-style: none;
		padding-left: 0;
	}

		ul.feature-icons li {
			text-decoration: none;
			display: inline-block;
			margin: 0 0 1.6875em 0;
			padding: 0.35em 0 0 3.5em;
			position: relative;
			vertical-align: top;
			width: 48%;
		}

			ul.feature-icons li:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 400;
			}

			ul.feature-icons li:before {
				background: #4acaa8;
				border-radius: 100%;
				color: #ffffff;
				display: block;
				height: 2.5em;
				left: 0;
				line-height: 2.5em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.5em;
			}

/* Icons */

	ul.icons {
		cursor: default;
		list-style: none;
		padding-left: 0;
	}

		ul.icons li {
			display: inline-block;
			padding: 0 1em 0 0;
		}

			ul.icons li:last-child {
				padding-right: 0 !important;
			}

			ul.icons li .icon:before {
				font-size: 1.25em;
			}

/* Table */

	.table-wrapper {
		-webkit-overflow-scrolling: touch;
		overflow-x: auto;
	}

	table {
		margin: 0 0 2.25em 0;
		width: 100%;
	}

		table tbody tr {
			border: solid 2px #f4f4f4;
			border-left: 0;
			border-right: 0;
		}

			table tbody tr:nth-child(2n + 1) {
				background-color: #fafafa;
			}

		table td {
			padding: 0.75em 0.75em;
		}

		table th {
			color: #777;
			font-size: 0.9em;
			font-weight: 700;
			padding: 0 0.75em 0.75em 0.75em;
			text-align: left;
		}

		table thead {
			border-bottom: solid 4px #e4e4e4;
		}

		table tfoot {
			border-top: solid 4px #e4e4e4;
		}

		table.alt {
			border-collapse: separate;
		}

			table.alt tbody tr td {
				border: solid 2px #e4e4e4;
				border-left-width: 0;
				border-top-width: 0;
			}

				table.alt tbody tr td:first-child {
					border-left-width: 2px;
				}

			table.alt tbody tr:first-child td {
				border-top-width: 2px;
			}

			table.alt thead {
				border-bottom: 0;
			}

			table.alt tfoot {
				border-top: 0;
			}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		background-color: #989898;
		border-radius: 5px;
		border: 0;
		color: #ffffff !important;
		cursor: pointer;
		display: inline-block;
		font-weight: 700;
		height: 2.75em;
		line-height: 2.75em;
		padding: 0 1.5em;
		text-align: center;
		text-decoration: none;
		white-space: nowrap;
	}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		.button:hover {
			background-color: #a5a5a5;
			color: #ffffff !important;
		}

		input[type="submit"]:active,
		input[type="reset"]:active,
		input[type="button"]:active,
		.button:active {
			background-color: #8b8b8b;
		}

		input[type="submit"].icon,
		input[type="reset"].icon,
		input[type="button"].icon,
		.button.icon {
			padding-left: 1.35em;
		}

			input[type="submit"].icon:before,
			input[type="reset"].icon:before,
			input[type="button"].icon:before,
			.button.icon:before {
				margin-right: 0.5em;
			}

		input[type="submit"].fit,
		input[type="reset"].fit,
		input[type="button"].fit,
		.button.fit {
			width: 100%;
		}

		input[type="submit"].small,
		input[type="reset"].small,
		input[type="button"].small,
		.button.small {
			font-size: 0.8em;
		}

		input[type="submit"].large,
		input[type="reset"].large,
		input[type="button"].large,
		.button.large {
			font-size: 1.35em;
		}

		input[type="submit"].alt,
		input[type="reset"].alt,
		input[type="button"].alt,
		.button.alt {
			background-color: transparent;
			box-shadow: inset 0 0 0 2px #e4e4e4;
			color: #777 !important;
		}

			input[type="submit"].alt:hover,
			input[type="reset"].alt:hover,
			input[type="button"].alt:hover,
			.button.alt:hover {
				background-color: #f4f4f4;
				color: #777 !important;
			}

			input[type="submit"].alt:active,
			input[type="reset"].alt:active,
			input[type="button"].alt:active,
			.button.alt:active {
				background-color: #eaeaea;
			}

			input[type="submit"].alt.icon:before,
			input[type="reset"].alt.icon:before,
			input[type="button"].alt.icon:before,
			.button.alt.icon:before {
				color: #aaa;
			}

		input[type="submit"].primary,
		input[type="reset"].primary,
		input[type="button"].primary,
		.button.primary {
			background-color: #4acaa8;
			color: #ffffff !important;
		}

			input[type="submit"].primary:hover,
			input[type="reset"].primary:hover,
			input[type="button"].primary:hover,
			.button.primary:hover {
				background-color: #5ed0b1;
			}

			input[type="submit"].primary:active,
			input[type="reset"].primary:active,
			input[type="button"].primary:active,
			.button.primary:active {
				background-color: #39c29d;
			}

		input[type="submit"].disabled, input[type="submit"]:disabled,
		input[type="reset"].disabled,
		input[type="reset"]:disabled,
		input[type="button"].disabled,
		input[type="button"]:disabled,
		.button.disabled,
		.button:disabled {
			background-color: #888 !important;
			box-shadow: inset 0 -0.15em 0 0 rgba(0, 0, 0, 0.15);
			color: #fff !important;
			cursor: default;
			opacity: 0.25;
		}

/* Features */

	.features article {
		border-top: solid 3px #f4f4f4;
		margin-bottom: 2.25em;
		padding-top: 2.25em;
	}

		.features article:first-child {
			border-top: 0;
			padding-top: 0;
		}

		.features article .image {
			display: inline-block;
			padding-right: 2.5em;
			vertical-align: middle;
			width: 48%;
		}

			.features article .image img {
				display: block;
				width: 100%;
			}

		.features article .inner {
			display: inline-block;
			vertical-align: middle;
			width: 50%;
		}

			.features article .inner > :last-child {
				margin-bottom: 0;
			}

/* Header */

	#header {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: column;
		-webkit-flex-direction: column;
		-ms-flex-direction: column;
		flex-direction: column;
		-moz-justify-content: space-between;
		-webkit-justify-content: space-between;
		-ms-justify-content: space-between;
		justify-content: space-between;
		background: #4acaa8;
		color: #d2f2e9;
		height: 100%;
		overflow-y: auto;
		position: fixed;
		text-align: center;
		top: 0;
		width: 23em;
		right: 0;
	}

		#header h1, #header h2, #header h3, #header h4, #header h5, #header h6 {
			color: #ffffff;
		}

			#header h1 a, #header h2 a, #header h3 a, #header h4 a, #header h5 a, #header h6 a {
				color: #ffffff;
			}

		#header header p {
			color: #b7eadc;
		}

		#header a {
			color: #d2f2e9;
		}

			#header a:hover {
				color: #ffffff !important;
			}

		#header > header {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			padding: 3em;
		}

			#header > header .avatar {
				display: block;
				margin: 0 auto 2.25em auto;
				width: 8em;
			}

			#header > header h1 {
				font-size: 1.75em;
				margin: 0;
			}

			#header > header p {
				color: #d2f2e9;
				font-style: italic;
				margin: 1em 0 0 0;
			}

		#header > footer {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			bottom: 0;
			left: 0;
			padding: 2em;
			width: 100%;
		}

			#header > footer .icons {
				margin: 0;
			}

				#header > footer .icons li a {
					color: #b7eadc;
				}

		#header > nav {
			-moz-flex-grow: 1;
			-webkit-flex-grow: 1;
			-ms-flex-grow: 1;
			flex-grow: 1;
		}

			#header > nav ul {
				list-style: none;
				margin: 0;
				padding: 0;
			}

				#header > nav ul li {
					border-top: solid 2px #5ccfb1;
					display: block;
					padding: 0;
				}

					#header > nav ul li a {
						-moz-transition: none;
						-webkit-transition: none;
						-ms-transition: none;
						transition: none;
						border: 0;
						color: #ffffff !important;
						display: block;
						padding: 0.85em 0;
						text-decoration: none;
					}

						#header > nav ul li a.active {
							background: #fff;
							color: #4acaa8 !important;
						}

					#header > nav ul li:first-child {
						border-top: 0;
					}

/* Wrapper */

	#wrapper {
		background: #fff;
		padding-right: 23em;
	}

/* Main */

	#main > section {
		border-top: solid 6px #f4f4f4;
	}

		#main > section > .container {
			padding: 6em 0 4em 0;
		}

		#main > section:first-child {
			border-top: 0;
		}

/* Footer */

	#footer {
		background: #fafafa;
		border-top: 0;
		color: #c0c0c0;
		overflow: hidden;
		padding: 4em 0 2em 0;
	}

		#footer .copyright {
			line-height: 1em;
			list-style: none;
			padding: 0;
		}

			#footer .copyright li {
				border-left: solid 1px #d4d4d4;
				display: inline-block;
				font-size: 0.8em;
				margin-left: 1em;
				padding-left: 1em;
			}

				#footer .copyright li:first-child {
					border-left: 0;
					margin-left: 0;
					padding-left: 0;
				}

				#footer .copyright li a {
					color: inherit;
				}

/* XLarge */

	@media screen and (max-width: 1680px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 13pt;
			}

		/* Header */

			#header {
				width: 21em;
			}

				#header > header {
					padding: 2em;
				}

				#header > footer {
					padding: 1.5em;
				}

		/* Wrapper */

			#wrapper {
				padding-right: 21em;
			}

		/* Main */

			#main > section > .container {
				padding: 4em 0 2em 0;
			}

	}

/* Large */

	@media screen and (max-width: 1280px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 11pt;
			}

		/* Header */

			#header {
				width: 20em;
			}

		/* Wrapper */

			#wrapper {
				padding-right: 20em;
			}

	}

/* Medium */

	#titleBar {
		display: none;
	}

	@media screen and (max-width: 1024px) {

		/* Basic */

			html, body {
				overflow-x: hidden;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* Image */

			.image.left, .image.right {
				max-width: 40%;
			}

				.image.left img, .image.right img {
					width: 100%;
				}

			.image.main {
				height: 20em;
			}

		/* Header */

			#header {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 100%;
				overflow-y: auto;
				position: fixed;
				top: 0;
				width: 23em;
				z-index: 10002;
				-moz-transform: translateX(23em);
				-webkit-transform: translateX(23em);
				-ms-transform: translateX(23em);
				transform: translateX(23em);
				right: 0;
			}

				#header > footer {
					bottom: auto;
					left: auto;
					margin: 0.5em 0 0 0;
					position: relative;
					right: auto;
					top: auto;
				}

		/* Wrapper */

			#wrapper {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				padding: 44px 0 1px 0;
			}

		/* Header Panel */

			#titleBar {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 44px;
				left: 0;
				position: fixed;
				top: 0;
				width: 100%;
				z-index: 10001;
				background: #222;
				color: #fff;
				min-width: 320px;
			}

				#titleBar .title {
					color: #fff;
					display: block;
					font-weight: 700;
					height: 44px;
					line-height: 44px;
					padding: 0 1em;
					width: 100%;
					text-align: left;
				}

					#titleBar .title a {
						border: 0;
						text-decoration: none;
					}

				#titleBar .toggle {
					text-decoration: none;
					height: 4em;
					position: absolute;
					top: 0;
					width: 6em;
					border: 0;
					outline: 0;
					right: 0;
				}

					#titleBar .toggle:before {
						-moz-osx-font-smoothing: grayscale;
						-webkit-font-smoothing: antialiased;
						display: inline-block;
						font-style: normal;
						font-variant: normal;
						text-rendering: auto;
						line-height: 1;
						text-transform: none !important;
						font-family: 'Font Awesome 5 Free';
						font-weight: 900;
					}

					#titleBar .toggle:before {
						background: #4acaa8;
						color: #ffffff;
						content: '\\f0c9';
						display: block;
						font-size: 18px;
						height: 44px;
						line-height: 44px;
						position: absolute;
						text-align: center;
						top: 0;
						width: 64px;
						right: 0;
					}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-23em);
				-webkit-transform: translateX(-23em);
				-ms-transform: translateX(-23em);
				transform: translateX(-23em);
			}

			body.header-visible #header {
				-moz-transform: translateX(0);
				-webkit-transform: translateX(0);
				-ms-transform: translateX(0);
				transform: translateX(0);
			}

	}

/* Small */

	@media screen and (max-width: 736px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 12pt;
			}

			h1 br, h2 br, h3 br, h4 br, h5 br, h6 br {
				display: none;
			}

			h2 {
				font-size: 1.75em;
			}

			h3 {
				font-size: 1.5em;
			}

			h4 {
				font-size: 1em;
			}

		/* Image */

			.image.left {
				margin: 0 1.5em 1em 0;
			}

			.image.right {
				margin: 0 0 1em 1.5em;
			}

			.image.main {
				height: 12em;
			}

		/* Section/Article */

			header br {
				display: none;
			}

			header.major h2 {
				font-size: 2.5em;
			}

				header.major h2 + p {
					font-size: 1.5em;
				}

		/* Features */

			.features article .image {
				display: block;
				margin: 0 0 2.25em 0;
				padding-right: 0;
				width: 100%;
			}

			.features article .inner {
				display: block;
				width: 100%;
			}

		/* Header */

			#header {
				width: 17em;
				-moz-transform: translateX(17em);
				-webkit-transform: translateX(17em);
				-ms-transform: translateX(17em);
				transform: translateX(17em);
				right: 0;
			}

				#header > header {
					padding: 2em;
				}

					#header > header .avatar {
						margin: 0 auto 1.6875em auto;
						width: 6em;
					}

					#header > header h1 {
						font-size: 1.5em;
					}

					#header > header p {
						margin: 1em 0 0 0;
					}

				#header > footer {
					padding: 1.5em;
				}

		/* Main */

			#main > section > .container {
				padding: 2em 0 0 0;
			}

		/* Footer */

			#footer {
				text-align: center;
			}

				#footer .copyright li {
					border-left: 0;
					display: block;
					line-height: 1.75em;
					margin: 0.75em 0 0 0;
					padding-left: 0;
				}

					#footer .copyright li:first-child {
						margin-top: 0;
					}

		/* Header Panel */

			#titleBar .toggle {
				height: 4em;
				width: 6em;
			}

				#titleBar .toggle:before {
					font-size: 14px;
					width: 44px;
				}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-17em);
				-webkit-transform: translateX(-17em);
				-ms-transform: translateX(-17em);
				transform: translateX(-17em);
			}

	}

/* XSmall */

	@media screen and (max-width: 480px) {

		/* Basic */

			html, body {
				min-width: 320px;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* List */

			ul.actions {
				margin: 0 0 2.25em 0;
			}

				ul.actions li {
					display: block;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions li:first-child {
						padding-top: 0;
					}

					ul.actions li > * {
						width: 100%;
						margin: 0 !important;
					}

						ul.actions li > *.icon:before {
							margin-left: -2em;
						}

				ul.actions.small li {
					padding: 0.5625em 0 0 0;
				}

					ul.actions.small li:first-child {
						padding-top: 0;
					}

			ul.feature-icons li {
				display: block;
				width: 100%;
			}

		/* Button */

			input[type="submit"],
			input[type="reset"],
			input[type="button"],
			.button {
				padding: 0;
			}

	}""", "lime":"""@import url("fontawesome-all.min.css");
@import url("https://fonts.googleapis.com/css?family=Lato:400,400italic,700,700italic|Source+Code+Pro:400");



html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #fff;
	}

		body.is-preload *, body.is-preload *:before, body.is-preload *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

	body, input, select, textarea {
		color: #888;
		font-family: "Lato", sans-serif;
		font-size: 16pt;
		font-weight: 400;
		line-height: 1.75em;
	}

	a {
		-moz-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-webkit-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-ms-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		border-bottom: solid 1px #e4e4e4;
		color: inherit;
		text-decoration: none;
	}

		a:hover {
			border-bottom-color: transparent;
			color: #379777 !important;
		}

	strong, b {
		color: #777;
		font-weight: 700;
	}

	em, i {
		font-style: italic;
	}

	p {
		margin: 0 0 2.25em 0;
	}

	h1, h2, h3, h4, h5, h6 {
		color: #777;
		font-weight: 700;
		line-height: 1em;
		margin: 0 0 0.5625em 0;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			border: 0;
			color: inherit;
			text-decoration: none;
		}

	h2 {
		font-size: 2em;
		line-height: 1.5em;
	}

	h3 {
		font-size: 1.75em;
		line-height: 1.5em;
	}

	h4 {
		font-size: 1.25em;
		line-height: 1.5em;
	}

	h5 {
		font-size: 0.9em;
		line-height: 1.5em;
	}

	h6 {
		font-size: 0.7em;
		line-height: 1.5em;
	}

	sub {
		font-size: 0.8em;
		position: relative;
		top: 0.5em;
	}

	sup {
		font-size: 0.8em;
		position: relative;
		top: -0.5em;
	}

	hr {
		border: 0;
		border-bottom: solid 2px #f4f4f4;
		margin: 2.25em 0;
	}

		hr.major {
			margin: 3.375em 0;
		}

	blockquote {
		border-left: solid 8px #e4e4e4;
		font-style: italic;
		margin: 0 0 2.25em 0;
		padding: 0.5em 0 0.5em 2em;
	}

	code {
		background: #555;
		border-radius: 5px;
		color: #fff;
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0.25em;
		padding: 0.25em 0.65em;
	}

	pre {
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0 2.25em 0;
	}

		pre code {
			-webkit-overflow-scrolling: touch;
			display: block;
			line-height: 1.5em;
			overflow-x: auto;
			padding: 1em 1.5em;
		}

	.align-left {
		text-align: left;
	}

	.align-center {
		text-align: center;
	}

	.align-right {
		text-align: right;
	}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0;
			margin-left: 0em;
		}

			.row.gtr-0 > * {
				padding: 0 0 0 0em;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0em;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0em;
				}

		.row.gtr-25 {
			margin-top: 0;
			margin-left: -0.5em;
		}

			.row.gtr-25 > * {
				padding: 0 0 0 0.5em;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -0.5em;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 0.5em;
				}

		.row.gtr-50 {
			margin-top: 0;
			margin-left: -1em;
		}

			.row.gtr-50 > * {
				padding: 0 0 0 1em;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -1em;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 1em;
				}

		.row {
			margin-top: 0;
			margin-left: -2em;
		}

			.row > * {
				padding: 0 0 0 2em;
			}

			.row.gtr-uniform {
				margin-top: -2em;
			}

				.row.gtr-uniform > * {
					padding-top: 2em;
				}

		.row.gtr-150 {
			margin-top: 0;
			margin-left: -3em;
		}

			.row.gtr-150 > * {
				padding: 0 0 0 3em;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -3em;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 3em;
				}

		.row.gtr-200 {
			margin-top: 0;
			margin-left: -4em;
		}

			.row.gtr-200 > * {
				padding: 0 0 0 4em;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -4em;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 4em;
				}

		@media screen and (max-width: 1680px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xlarge {
					order: -1;
				}

				.row > .col-1-xlarge {
					width: 8.33333%;
				}

				.row > .off-1-xlarge {
					margin-left: 8.33333%;
				}

				.row > .col-2-xlarge {
					width: 16.66667%;
				}

				.row > .off-2-xlarge {
					margin-left: 16.66667%;
				}

				.row > .col-3-xlarge {
					width: 25%;
				}

				.row > .off-3-xlarge {
					margin-left: 25%;
				}

				.row > .col-4-xlarge {
					width: 33.33333%;
				}

				.row > .off-4-xlarge {
					margin-left: 33.33333%;
				}

				.row > .col-5-xlarge {
					width: 41.66667%;
				}

				.row > .off-5-xlarge {
					margin-left: 41.66667%;
				}

				.row > .col-6-xlarge {
					width: 50%;
				}

				.row > .off-6-xlarge {
					margin-left: 50%;
				}

				.row > .col-7-xlarge {
					width: 58.33333%;
				}

				.row > .off-7-xlarge {
					margin-left: 58.33333%;
				}

				.row > .col-8-xlarge {
					width: 66.66667%;
				}

				.row > .off-8-xlarge {
					margin-left: 66.66667%;
				}

				.row > .col-9-xlarge {
					width: 75%;
				}

				.row > .off-9-xlarge {
					margin-left: 75%;
				}

				.row > .col-10-xlarge {
					width: 83.33333%;
				}

				.row > .off-10-xlarge {
					margin-left: 83.33333%;
				}

				.row > .col-11-xlarge {
					width: 91.66667%;
				}

				.row > .off-11-xlarge {
					margin-left: 91.66667%;
				}

				.row > .col-12-xlarge {
					width: 100%;
				}

				.row > .off-12-xlarge {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -1em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 1em;
						}

				.row {
					margin-top: 0;
					margin-left: -2em;
				}

					.row > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-uniform > * {
							padding-top: 2em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 3em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -4em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 4em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -4em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 4em;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-large {
					order: -1;
				}

				.row > .col-1-large {
					width: 8.33333%;
				}

				.row > .off-1-large {
					margin-left: 8.33333%;
				}

				.row > .col-2-large {
					width: 16.66667%;
				}

				.row > .off-2-large {
					margin-left: 16.66667%;
				}

				.row > .col-3-large {
					width: 25%;
				}

				.row > .off-3-large {
					margin-left: 25%;
				}

				.row > .col-4-large {
					width: 33.33333%;
				}

				.row > .off-4-large {
					margin-left: 33.33333%;
				}

				.row > .col-5-large {
					width: 41.66667%;
				}

				.row > .off-5-large {
					margin-left: 41.66667%;
				}

				.row > .col-6-large {
					width: 50%;
				}

				.row > .off-6-large {
					margin-left: 50%;
				}

				.row > .col-7-large {
					width: 58.33333%;
				}

				.row > .off-7-large {
					margin-left: 58.33333%;
				}

				.row > .col-8-large {
					width: 66.66667%;
				}

				.row > .off-8-large {
					margin-left: 66.66667%;
				}

				.row > .col-9-large {
					width: 75%;
				}

				.row > .off-9-large {
					margin-left: 75%;
				}

				.row > .col-10-large {
					width: 83.33333%;
				}

				.row > .off-10-large {
					margin-left: 83.33333%;
				}

				.row > .col-11-large {
					width: 91.66667%;
				}

				.row > .off-11-large {
					margin-left: 91.66667%;
				}

				.row > .col-12-large {
					width: 100%;
				}

				.row > .off-12-large {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 1024px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-medium {
					order: -1;
				}

				.row > .col-1-medium {
					width: 8.33333%;
				}

				.row > .off-1-medium {
					margin-left: 8.33333%;
				}

				.row > .col-2-medium {
					width: 16.66667%;
				}

				.row > .off-2-medium {
					margin-left: 16.66667%;
				}

				.row > .col-3-medium {
					width: 25%;
				}

				.row > .off-3-medium {
					margin-left: 25%;
				}

				.row > .col-4-medium {
					width: 33.33333%;
				}

				.row > .off-4-medium {
					margin-left: 33.33333%;
				}

				.row > .col-5-medium {
					width: 41.66667%;
				}

				.row > .off-5-medium {
					margin-left: 41.66667%;
				}

				.row > .col-6-medium {
					width: 50%;
				}

				.row > .off-6-medium {
					margin-left: 50%;
				}

				.row > .col-7-medium {
					width: 58.33333%;
				}

				.row > .off-7-medium {
					margin-left: 58.33333%;
				}

				.row > .col-8-medium {
					width: 66.66667%;
				}

				.row > .off-8-medium {
					margin-left: 66.66667%;
				}

				.row > .col-9-medium {
					width: 75%;
				}

				.row > .off-9-medium {
					margin-left: 75%;
				}

				.row > .col-10-medium {
					width: 83.33333%;
				}

				.row > .off-10-medium {
					margin-left: 83.33333%;
				}

				.row > .col-11-medium {
					width: 91.66667%;
				}

				.row > .off-11-medium {
					margin-left: 91.66667%;
				}

				.row > .col-12-medium {
					width: 100%;
				}

				.row > .off-12-medium {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-small {
					order: -1;
				}

				.row > .col-1-small {
					width: 8.33333%;
				}

				.row > .off-1-small {
					margin-left: 8.33333%;
				}

				.row > .col-2-small {
					width: 16.66667%;
				}

				.row > .off-2-small {
					margin-left: 16.66667%;
				}

				.row > .col-3-small {
					width: 25%;
				}

				.row > .off-3-small {
					margin-left: 25%;
				}

				.row > .col-4-small {
					width: 33.33333%;
				}

				.row > .off-4-small {
					margin-left: 33.33333%;
				}

				.row > .col-5-small {
					width: 41.66667%;
				}

				.row > .off-5-small {
					margin-left: 41.66667%;
				}

				.row > .col-6-small {
					width: 50%;
				}

				.row > .off-6-small {
					margin-left: 50%;
				}

				.row > .col-7-small {
					width: 58.33333%;
				}

				.row > .off-7-small {
					margin-left: 58.33333%;
				}

				.row > .col-8-small {
					width: 66.66667%;
				}

				.row > .off-8-small {
					margin-left: 66.66667%;
				}

				.row > .col-9-small {
					width: 75%;
				}

				.row > .off-9-small {
					margin-left: 75%;
				}

				.row > .col-10-small {
					width: 83.33333%;
				}

				.row > .off-10-small {
					margin-left: 83.33333%;
				}

				.row > .col-11-small {
					width: 91.66667%;
				}

				.row > .off-11-small {
					margin-left: 91.66667%;
				}

				.row > .col-12-small {
					width: 100%;
				}

				.row > .off-12-small {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

		@media screen and (max-width: 480px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xsmall {
					order: -1;
				}

				.row > .col-1-xsmall {
					width: 8.33333%;
				}

				.row > .off-1-xsmall {
					margin-left: 8.33333%;
				}

				.row > .col-2-xsmall {
					width: 16.66667%;
				}

				.row > .off-2-xsmall {
					margin-left: 16.66667%;
				}

				.row > .col-3-xsmall {
					width: 25%;
				}

				.row > .off-3-xsmall {
					margin-left: 25%;
				}

				.row > .col-4-xsmall {
					width: 33.33333%;
				}

				.row > .off-4-xsmall {
					margin-left: 33.33333%;
				}

				.row > .col-5-xsmall {
					width: 41.66667%;
				}

				.row > .off-5-xsmall {
					margin-left: 41.66667%;
				}

				.row > .col-6-xsmall {
					width: 50%;
				}

				.row > .off-6-xsmall {
					margin-left: 50%;
				}

				.row > .col-7-xsmall {
					width: 58.33333%;
				}

				.row > .off-7-xsmall {
					margin-left: 58.33333%;
				}

				.row > .col-8-xsmall {
					width: 66.66667%;
				}

				.row > .off-8-xsmall {
					margin-left: 66.66667%;
				}

				.row > .col-9-xsmall {
					width: 75%;
				}

				.row > .off-9-xsmall {
					margin-left: 75%;
				}

				.row > .col-10-xsmall {
					width: 83.33333%;
				}

				.row > .off-10-xsmall {
					margin-left: 83.33333%;
				}

				.row > .col-11-xsmall {
					width: 91.66667%;
				}

				.row > .off-11-xsmall {
					margin-left: 91.66667%;
				}

				.row > .col-12-xsmall {
					width: 100%;
				}

				.row > .off-12-xsmall {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

/* Container */

	.container {
		margin: 0 auto;
		max-width: calc(100% - 4.5em);
		width: 45em;
	}

		.container.xsmall {
			width: 11.25em;
		}

		.container.small {
			width: 22.5em;
		}

		.container.medium {
			width: 33.75em;
		}

		.container.large {
			width: 56.25em;
		}

		.container.xlarge {
			width: 67.5em;
		}

		.container.max {
			width: 100%;
		}

		@media screen and (max-width: 1024px) {

			.container {
				width: 100% !important;
			}

		}

		@media screen and (max-width: 480px) {

			.container {
				max-width: calc(100% - 3.375em);
			}

		}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header p {
		color: #aaa;
		position: relative;
		margin: 0 0 1.6875em 0;
	}

	header h2 + p {
		font-size: 1.25em;
		margin-top: -0.5em;
		line-height: 1.5em;
	}

	header h3 + p {
		font-size: 1.1em;
		margin-top: -0.35em;
		line-height: 1.5em;
	}

	header h4 + p,
	header h5 + p,
	header h6 + p {
		font-size: 0.9em;
		margin-top: -0.25em;
		line-height: 1.5em;
	}

	header.major h2 {
		color: #379777;
		font-size: 3.5em;
	}

		header.major h2 + p {
			color: #777;
			font-size: 1.75em;
			font-weight: 700;
			margin-top: -0.75em;
		}

/* Form */

	form {
		margin: 0 0 2.25em 0;
	}

	label {
		color: #777;
		display: block;
		font-size: 0.9em;
		font-weight: 700;
		margin: 0 0 1.125em 0;
	}

	input::-moz-focus-inner {
		border: 0;
		padding: 0;
	}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select,
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		border-radius: 5px;
		border: none;
		border: solid 2px #e4e4e4;
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 1em;
		text-decoration: none;
		width: 100%;
	}

		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		select:focus,
		textarea:focus {
			border-color: #379777;
		}

	select {
		background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' preserveAspectRatio='none' viewBox='0 0 40 40'%3E%3Cpath d='M9.4,12.3l10.4,10.4l10.4-10.4c0.2-0.2,0.5-0.4,0.9-0.4c0.3,0,0.6,0.1,0.9,0.4l3.3,3.3c0.2,0.2,0.4,0.5,0.4,0.9 c0,0.4-0.1,0.6-0.4,0.9L20.7,31.9c-0.2,0.2-0.5,0.4-0.9,0.4c-0.3,0-0.6-0.1-0.9-0.4L4.3,17.3c-0.2-0.2-0.4-0.5-0.4-0.9 c0-0.4,0.1-0.6,0.4-0.9l3.3-3.3c0.2-0.2,0.5-0.4,0.9-0.4S9.1,12.1,9.4,12.3z' fill='%23e4e4e4' /%3E%3C/svg%3E");
		background-size: 1.25em;
		background-repeat: no-repeat;
		background-position: calc(100% - 1em) center;
		height: 2.75em;
		padding-right: 2.75em;
		text-overflow: ellipsis;
	}

		select option {
			color: #777;
			background: #fff;
		}

		select:focus::-ms-value {
			background-color: transparent;
		}

		select::-ms-expand {
			display: none;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 2.75em;
	}

	textarea {
		padding: 0.75em 1em;
	}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2em;
		opacity: 0;
		width: 1em;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			color: #888;
			cursor: pointer;
			display: inline-block;
			font-size: 1em;
			font-weight: 400;
			padding-left: 2.4em;
			padding-right: 0.75em;
			position: relative;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				background: #fafafa;
				border-radius: 5px;
				border: solid 2px #e4e4e4;
				content: '';
				display: inline-block;
				font-size: 0.8em;
				height: 2.0625em;
				left: 0;
				line-height: 2.0625em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.0625em;
			}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			background: #989898;
			border-color: #989898;
			color: #45474B;
			content: '\\f00c';
		}

		input[type="checkbox"]:focus + label:before,
		input[type="radio"]:focus + label:before {
			border-color: #379777;
		}

	input[type="checkbox"] + label:before {
		border-radius: 5px;
	}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	::-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

/* Box */

	.box {
		border-radius: 5px;
		border: solid 2px #e4e4e4;
		margin-bottom: 2.25em;
		padding: 1.5em;
	}

		.box > :last-child,
		.box > :last-child > :last-child,
		.box > :last-child > :last-child > :last-child {
			margin-bottom: 0;
		}

		.box.alt {
			border: 0;
			border-radius: 0;
			padding: 0;
		}

/* Icon */

	.icon {
		text-decoration: none;
		border-bottom: none;
		position: relative;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 400;
		}

		.icon > .label {
			display: none;
		}

		.icon:before {
			line-height: inherit;
		}

		.icon.solid:before {
			font-weight: 900;
		}

		.icon.brands:before {
			font-family: 'Font Awesome 5 Brands';
		}

/* Image */

	.image {
		border-radius: 5px;
		border: 0;
		display: inline-block;
		position: relative;
	}

		.image[data-position] img {
			-moz-object-fit: cover;
			-webkit-object-fit: cover;
			-ms-object-fit: cover;
			object-fit: cover;
			display: block;
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
		}

		.image[data-position="top left"] img {
			-moz-object-position: top left;
			-webkit-object-position: top left;
			-ms-object-position: top left;
			object-position: top left;
		}

		.image[data-position="top"] img {
			-moz-object-position: top;
			-webkit-object-position: top;
			-ms-object-position: top;
			object-position: top;
		}

		.image[data-position="top right"] img {
			-moz-object-position: top right;
			-webkit-object-position: top right;
			-ms-object-position: top right;
			object-position: top right;
		}

		.image[data-position="right"] img {
			-moz-object-position: right;
			-webkit-object-position: right;
			-ms-object-position: right;
			object-position: right;
		}

		.image[data-position="bottom right"] img {
			-moz-object-position: bottom right;
			-webkit-object-position: bottom right;
			-ms-object-position: bottom right;
			object-position: bottom right;
		}

		.image[data-position="bottom"] img {
			-moz-object-position: bottom;
			-webkit-object-position: bottom;
			-ms-object-position: bottom;
			object-position: bottom;
		}

		.image[data-position="bottom left"] img {
			-moz-object-position: bottom left;
			-webkit-object-position: bottom left;
			-ms-object-position: bottom left;
			object-position: bottom left;
		}

		.image[data-position="left"] img {
			-moz-object-position: left;
			-webkit-object-position: left;
			-ms-object-position: left;
			object-position: left;
		}

		.image[data-position="center"] img {
			-moz-object-position: center;
			-webkit-object-position: center;
			-ms-object-position: center;
			object-position: center;
		}

		.image[data-position="25% 25%"] img {
			-moz-object-position: 25% 25%;
			-webkit-object-position: 25% 25%;
			-ms-object-position: 25% 25%;
			object-position: 25% 25%;
		}

		.image[data-position="75% 25%"] img {
			-moz-object-position: 75% 25%;
			-webkit-object-position: 75% 25%;
			-ms-object-position: 75% 25%;
			object-position: 75% 25%;
		}

		.image[data-position="75% 75%"] img {
			-moz-object-position: 75% 75%;
			-webkit-object-position: 75% 75%;
			-ms-object-position: 75% 75%;
			object-position: 75% 75%;
		}

		.image[data-position="25% 75%"] img {
			-moz-object-position: 25% 75%;
			-webkit-object-position: 25% 75%;
			-ms-object-position: 25% 75%;
			object-position: 25% 75%;
		}

		.image img {
			border-radius: 5px;
			display: block;
		}

		.image.left {
			float: left;
			margin: 0 2.5em 2em 0;
			top: 0.25em;
		}

		.image.right {
			float: right;
			margin: 0 0 2em 2.5em;
			top: 0.25em;
		}

		.image.fit {
			display: block;
			margin: 0 0 2.25em 0;
			width: 100%;
		}

			.image.fit img {
				display: block;
				width: 100%;
			}

		.image.avatar {
			border-radius: 100%;
			overflow: hidden;
		}

			.image.avatar img {
				border-radius: 100%;
				display: block;
				width: 100%;
			}

		.image.main {
			display: block;
			height: 20em;
			border-radius: 0;
		}

			.image.main img {
				border-radius: 0;
			}

/* List */

	ol {
		list-style: decimal;
		margin: 0 0 2.25em 0;
		padding-left: 1.25em;
	}

		ol li {
			padding-left: 0.25em;
		}

	ul {
		list-style: disc;
		margin: 0 0 2.25em 0;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
		}

		ul.alt {
			list-style: none;
			padding-left: 0;
		}

			ul.alt li {
				border-top: solid 2px #f4f4f4;
				padding: 0.5em 0;
			}

				ul.alt li:first-child {
					border-top: 0;
					padding-top: 0;
				}

	dl {
		margin: 0 0 2.25em 0;
	}

/* Actions */

	ul.actions {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		cursor: default;
		list-style: none;
		margin-left: -1.125em;
		padding-left: 0;
	}

		ul.actions li {
			padding: 0 0 0 1.125em;
			vertical-align: middle;
		}

		ul.actions.special {
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 100%;
			margin-left: 0;
		}

			ul.actions.special li:first-child {
				padding-left: 0;
			}

		ul.actions.stacked {
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			margin-left: 0;
		}

			ul.actions.stacked li {
				padding: 1.125em 0 0 0;
			}

				ul.actions.stacked li:first-child {
					padding-top: 0;
				}

		ul.actions.fit {
			width: calc(100% + 1.125em);
		}

			ul.actions.fit li {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				width: 100%;
			}

				ul.actions.fit li > * {
					width: 100%;
				}

			ul.actions.fit.stacked {
				width: 100%;
			}

		@media screen and (max-width: 480px) {

			ul.actions:not(.fixed) {
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
				margin-left: 0;
				width: 100% !important;
			}

				ul.actions:not(.fixed) li {
					-moz-flex-grow: 1;
					-webkit-flex-grow: 1;
					-ms-flex-grow: 1;
					flex-grow: 1;
					-moz-flex-shrink: 1;
					-webkit-flex-shrink: 1;
					-ms-flex-shrink: 1;
					flex-shrink: 1;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions:not(.fixed) li > * {
						width: 100%;
					}

					ul.actions:not(.fixed) li:first-child {
						padding-top: 0;
					}

					ul.actions:not(.fixed) li input[type="submit"],
					ul.actions:not(.fixed) li input[type="reset"],
					ul.actions:not(.fixed) li input[type="button"],
					ul.actions:not(.fixed) li button,
					ul.actions:not(.fixed) li .button {
						width: 100%;
					}

						ul.actions:not(.fixed) li input[type="submit"].icon:before,
						ul.actions:not(.fixed) li input[type="reset"].icon:before,
						ul.actions:not(.fixed) li input[type="button"].icon:before,
						ul.actions:not(.fixed) li button.icon:before,
						ul.actions:not(.fixed) li .button.icon:before {
							margin-left: -0.5rem;
						}

		}

/* Feature Icons */

	ul.feature-icons {
		list-style: none;
		padding-left: 0;
	}

		ul.feature-icons li {
			text-decoration: none;
			display: inline-block;
			margin: 0 0 1.6875em 0;
			padding: 0.35em 0 0 3.5em;
			position: relative;
			vertical-align: top;
			width: 48%;
		}

			ul.feature-icons li:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 400;
			}

			ul.feature-icons li:before {
				background: #379777;
				border-radius: 100%;
				color: #ffffff;
				display: block;
				height: 2.5em;
				left: 0;
				line-height: 2.5em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.5em;
			}

/* Icons */

	ul.icons {
		cursor: default;
		list-style: none;
		padding-left: 0;
	}

		ul.icons li {
			display: inline-block;
			padding: 0 1em 0 0;
		}

			ul.icons li:last-child {
				padding-right: 0 !important;
			}

			ul.icons li .icon:before {
				font-size: 1.25em;
			}

/* Table */

	.table-wrapper {
		-webkit-overflow-scrolling: touch;
		overflow-x: auto;
	}

	table {
		margin: 0 0 2.25em 0;
		width: 100%;
	}

		table tbody tr {
			border: solid 2px #f4f4f4;
			border-left: 0;
			border-right: 0;
		}

			table tbody tr:nth-child(2n + 1) {
				background-color: #fafafa;
			}

		table td {
			padding: 0.75em 0.75em;
		}

		table th {
			color: #777;
			font-size: 0.9em;
			font-weight: 700;
			padding: 0 0.75em 0.75em 0.75em;
			text-align: left;
		}

		table thead {
			border-bottom: solid 4px #e4e4e4;
		}

		table tfoot {
			border-top: solid 4px #e4e4e4;
		}

		table.alt {
			border-collapse: separate;
		}

			table.alt tbody tr td {
				border: solid 2px #e4e4e4;
				border-left-width: 0;
				border-top-width: 0;
			}

				table.alt tbody tr td:first-child {
					border-left-width: 2px;
				}

			table.alt tbody tr:first-child td {
				border-top-width: 2px;
			}

			table.alt thead {
				border-bottom: 0;
			}

			table.alt tfoot {
				border-top: 0;
			}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		background-color: #989898;
		border-radius: 5px;
		border: 0;
		color: #ffffff !important;
		cursor: pointer;
		display: inline-block;
		font-weight: 700;
		height: 2.75em;
		line-height: 2.75em;
		padding: 0 1.5em;
		text-align: center;
		text-decoration: none;
		white-space: nowrap;
	}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		.button:hover {
			background-color: #a5a5a5;
			color: #ffffff !important;
		}

		input[type="submit"]:active,
		input[type="reset"]:active,
		input[type="button"]:active,
		.button:active {
			background-color: #8b8b8b;
		}

		input[type="submit"].icon,
		input[type="reset"].icon,
		input[type="button"].icon,
		.button.icon {
			padding-left: 1.35em;
		}

			input[type="submit"].icon:before,
			input[type="reset"].icon:before,
			input[type="button"].icon:before,
			.button.icon:before {
				margin-right: 0.5em;
			}

		input[type="submit"].fit,
		input[type="reset"].fit,
		input[type="button"].fit,
		.button.fit {
			width: 100%;
		}

		input[type="submit"].small,
		input[type="reset"].small,
		input[type="button"].small,
		.button.small {
			font-size: 0.8em;
		}

		input[type="submit"].large,
		input[type="reset"].large,
		input[type="button"].large,
		.button.large {
			font-size: 1.35em;
		}

		input[type="submit"].alt,
		input[type="reset"].alt,
		input[type="button"].alt,
		.button.alt {
			background-color: transparent;
			box-shadow: inset 0 0 0 2px #e4e4e4;
			color: #777 !important;
		}

			input[type="submit"].alt:hover,
			input[type="reset"].alt:hover,
			input[type="button"].alt:hover,
			.button.alt:hover {
				background-color: #f4f4f4;
				color: #777 !important;
			}

			input[type="submit"].alt:active,
			input[type="reset"].alt:active,
			input[type="button"].alt:active,
			.button.alt:active {
				background-color: #eaeaea;
			}

			input[type="submit"].alt.icon:before,
			input[type="reset"].alt.icon:before,
			input[type="button"].alt.icon:before,
			.button.alt.icon:before {
				color: #aaa;
			}

		input[type="submit"].primary,
		input[type="reset"].primary,
		input[type="button"].primary,
		.button.primary {
			background-color: #379777;
			color: #ffffff !important;
		}

			input[type="submit"].primary:hover,
			input[type="reset"].primary:hover,
			input[type="button"].primary:hover,
			.button.primary:hover {
				background-color: #5ed0b1;
			}

			input[type="submit"].primary:active,
			input[type="reset"].primary:active,
			input[type="button"].primary:active,
			.button.primary:active {
				background-color: #39c29d;
			}

		input[type="submit"].disabled, input[type="submit"]:disabled,
		input[type="reset"].disabled,
		input[type="reset"]:disabled,
		input[type="button"].disabled,
		input[type="button"]:disabled,
		.button.disabled,
		.button:disabled {
			background-color: #888 !important;
			box-shadow: inset 0 -0.15em 0 0 rgba(0, 0, 0, 0.15);
			color: #fff !important;
			cursor: default;
			opacity: 0.25;
		}

/* Features */

	.features article {
		border-top: solid 3px #f4f4f4;
		margin-bottom: 2.25em;
		padding-top: 2.25em;
	}

		.features article:first-child {
			border-top: 0;
			padding-top: 0;
		}

		.features article .image {
			display: inline-block;
			padding-right: 2.5em;
			vertical-align: middle;
			width: 48%;
		}

			.features article .image img {
				display: block;
				width: 100%;
			}

		.features article .inner {
			display: inline-block;
			vertical-align: middle;
			width: 50%;
		}

			.features article .inner > :last-child {
				margin-bottom: 0;
			}

/* Header */

	#header {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: column;
		-webkit-flex-direction: column;
		-ms-flex-direction: column;
		flex-direction: column;
		-moz-justify-content: space-between;
		-webkit-justify-content: space-between;
		-ms-justify-content: space-between;
		justify-content: space-between;
		background: #379777;
		color: #d2f2e9;
		height: 100%;
		overflow-y: auto;
		position: fixed;
		text-align: center;
		top: 0;
		width: 23em;
		right: 0;
	}

		#header h1, #header h2, #header h3, #header h4, #header h5, #header h6 {
			color: #ffffff;
		}

			#header h1 a, #header h2 a, #header h3 a, #header h4 a, #header h5 a, #header h6 a {
				color: #ffffff;
			}

		#header header p {
			color: #45474B;
		}

		#header a {
			color: #d2f2e9;
		}

			#header a:hover {
				color: #ffffff !important;
			}

		#header > header {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			padding: 3em;
		}

			#header > header .avatar {
				display: block;
				margin: 0 auto 2.25em auto;
				width: 8em;
			}

			#header > header h1 {
				font-size: 1.75em;
				margin: 0;
			}

			#header > header p {
				color: #d2f2e9;
				font-style: italic;
				margin: 1em 0 0 0;
			}

		#header > footer {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			bottom: 0;
			left: 0;
			padding: 2em;
			width: 100%;
		}

			#header > footer .icons {
				margin: 0;
			}

				#header > footer .icons li a {
					color: #45474B;
				}

		#header > nav {
			-moz-flex-grow: 1;
			-webkit-flex-grow: 1;
			-ms-flex-grow: 1;
			flex-grow: 1;
		}

			#header > nav ul {
				list-style: none;
				margin: 0;
				padding: 0;
			}

				#header > nav ul li {
					border-top: solid 2px #5ccfb1;
					display: block;
					padding: 0;
				}

					#header > nav ul li a {
						-moz-transition: none;
						-webkit-transition: none;
						-ms-transition: none;
						transition: none;
						border: 0;
						color: #ffffff !important;
						display: block;
						padding: 0.85em 0;
						text-decoration: none;
					}

						#header > nav ul li a.active {
							background: #fff;
							color: #379777 !important;
						}

					#header > nav ul li:first-child {
						border-top: 0;
					}

/* Wrapper */

	#wrapper {
		background: #fff;
		padding-right: 23em;
	}

/* Main */

	#main > section {
		border-top: solid 6px #f4f4f4;
	}

		#main > section > .container {
			padding: 6em 0 4em 0;
		}

		#main > section:first-child {
			border-top: 0;
		}

/* Footer */

	#footer {
		background: #fafafa;
		border-top: 0;
		color: #c0c0c0;
		overflow: hidden;
		padding: 4em 0 2em 0;
	}

		#footer .copyright {
			line-height: 1em;
			list-style: none;
			padding: 0;
		}

			#footer .copyright li {
				border-left: solid 1px #d4d4d4;
				display: inline-block;
				font-size: 0.8em;
				margin-left: 1em;
				padding-left: 1em;
			}

				#footer .copyright li:first-child {
					border-left: 0;
					margin-left: 0;
					padding-left: 0;
				}

				#footer .copyright li a {
					color: inherit;
				}

/* XLarge */

	@media screen and (max-width: 1680px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 13pt;
			}

		/* Header */

			#header {
				width: 21em;
			}

				#header > header {
					padding: 2em;
				}

				#header > footer {
					padding: 1.5em;
				}

		/* Wrapper */

			#wrapper {
				padding-right: 21em;
			}

		/* Main */

			#main > section > .container {
				padding: 4em 0 2em 0;
			}

	}

/* Large */

	@media screen and (max-width: 1280px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 11pt;
			}

		/* Header */

			#header {
				width: 20em;
			}

		/* Wrapper */

			#wrapper {
				padding-right: 20em;
			}

	}

/* Medium */

	#titleBar {
		display: none;
	}

	@media screen and (max-width: 1024px) {

		/* Basic */

			html, body {
				overflow-x: hidden;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* Image */

			.image.left, .image.right {
				max-width: 40%;
			}

				.image.left img, .image.right img {
					width: 100%;
				}

			.image.main {
				height: 20em;
			}

		/* Header */

			#header {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 100%;
				overflow-y: auto;
				position: fixed;
				top: 0;
				width: 23em;
				z-index: 10002;
				-moz-transform: translateX(23em);
				-webkit-transform: translateX(23em);
				-ms-transform: translateX(23em);
				transform: translateX(23em);
				right: 0;
			}

				#header > footer {
					bottom: auto;
					left: auto;
					margin: 0.5em 0 0 0;
					position: relative;
					right: auto;
					top: auto;
				}

		/* Wrapper */

			#wrapper {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				padding: 44px 0 1px 0;
			}

		/* Header Panel */

			#titleBar {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 44px;
				left: 0;
				position: fixed;
				top: 0;
				width: 100%;
				z-index: 10001;
				background: #222;
				color: #fff;
				min-width: 320px;
			}

				#titleBar .title {
					color: #fff;
					display: block;
					font-weight: 700;
					height: 44px;
					line-height: 44px;
					padding: 0 1em;
					width: 100%;
					text-align: left;
				}

					#titleBar .title a {
						border: 0;
						text-decoration: none;
					}

				#titleBar .toggle {
					text-decoration: none;
					height: 4em;
					position: absolute;
					top: 0;
					width: 6em;
					border: 0;
					outline: 0;
					right: 0;
				}

					#titleBar .toggle:before {
						-moz-osx-font-smoothing: grayscale;
						-webkit-font-smoothing: antialiased;
						display: inline-block;
						font-style: normal;
						font-variant: normal;
						text-rendering: auto;
						line-height: 1;
						text-transform: none !important;
						font-family: 'Font Awesome 5 Free';
						font-weight: 900;
					}

					#titleBar .toggle:before {
						background: #379777;
						color: #ffffff;
						content: '\\f0c9';
						display: block;
						font-size: 18px;
						height: 44px;
						line-height: 44px;
						position: absolute;
						text-align: center;
						top: 0;
						width: 64px;
						right: 0;
					}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-23em);
				-webkit-transform: translateX(-23em);
				-ms-transform: translateX(-23em);
				transform: translateX(-23em);
			}

			body.header-visible #header {
				-moz-transform: translateX(0);
				-webkit-transform: translateX(0);
				-ms-transform: translateX(0);
				transform: translateX(0);
			}

	}

/* Small */

	@media screen and (max-width: 736px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 12pt;
			}

			h1 br, h2 br, h3 br, h4 br, h5 br, h6 br {
				display: none;
			}

			h2 {
				font-size: 1.75em;
			}

			h3 {
				font-size: 1.5em;
			}

			h4 {
				font-size: 1em;
			}

		/* Image */

			.image.left {
				margin: 0 1.5em 1em 0;
			}

			.image.right {
				margin: 0 0 1em 1.5em;
			}

			.image.main {
				height: 12em;
			}

		/* Section/Article */

			header br {
				display: none;
			}

			header.major h2 {
				font-size: 2.5em;
			}

				header.major h2 + p {
					font-size: 1.5em;
				}

		/* Features */

			.features article .image {
				display: block;
				margin: 0 0 2.25em 0;
				padding-right: 0;
				width: 100%;
			}

			.features article .inner {
				display: block;
				width: 100%;
			}

		/* Header */

			#header {
				width: 17em;
				-moz-transform: translateX(17em);
				-webkit-transform: translateX(17em);
				-ms-transform: translateX(17em);
				transform: translateX(17em);
				right: 0;
			}

				#header > header {
					padding: 2em;
				}

					#header > header .avatar {
						margin: 0 auto 1.6875em auto;
						width: 6em;
					}

					#header > header h1 {
						font-size: 1.5em;
					}

					#header > header p {
						margin: 1em 0 0 0;
					}

				#header > footer {
					padding: 1.5em;
				}

		/* Main */

			#main > section > .container {
				padding: 2em 0 0 0;
			}

		/* Footer */

			#footer {
				text-align: center;
			}

				#footer .copyright li {
					border-left: 0;
					display: block;
					line-height: 1.75em;
					margin: 0.75em 0 0 0;
					padding-left: 0;
				}

					#footer .copyright li:first-child {
						margin-top: 0;
					}

		/* Header Panel */

			#titleBar .toggle {
				height: 4em;
				width: 6em;
			}

				#titleBar .toggle:before {
					font-size: 14px;
					width: 44px;
				}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-17em);
				-webkit-transform: translateX(-17em);
				-ms-transform: translateX(-17em);
				transform: translateX(-17em);
			}

	}

/* XSmall */

	@media screen and (max-width: 480px) {

		/* Basic */

			html, body {
				min-width: 320px;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* List */

			ul.actions {
				margin: 0 0 2.25em 0;
			}

				ul.actions li {
					display: block;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions li:first-child {
						padding-top: 0;
					}

					ul.actions li > * {
						width: 100%;
						margin: 0 !important;
					}

						ul.actions li > *.icon:before {
							margin-left: -2em;
						}

				ul.actions.small li {
					padding: 0.5625em 0 0 0;
				}

					ul.actions.small li:first-child {
						padding-top: 0;
					}

			ul.feature-icons li {
				display: block;
				width: 100%;
			}

		/* Button */

			input[type="submit"],
			input[type="reset"],
			input[type="button"],
			.button {
				padding: 0;
			}

	}
	/* Define the colors */
:root {
    --color-primary: #45474B;
    --color-secondary: #45474B;
    --color-tertiary: #379777;
    --color-quaternary: #379777;
}

/* Example usage of the colors */
body {
    background-color: var(--color-primary);
    color: var(--color-quaternary);
	background-color:#F6E96B;
}
section
{
	background-color:#F6E96B;
}
.header {
    background-color: var(--color-secondary);
    color: var(--color-primary);
}

.button {
    background-color: var(--color-tertiary);
    color: var(--color-primary);
}

.footer {
    background-color: var(--color-quaternary);
    color: var(--color-secondary);
}

#main {
    background-color: #45474B;
}
#header {
    background-color: #45474B;
}
#header {
    background-color: #45474B;
}
#footer , h1, h2, h3, h4{
	color: #379777;
}
#wrapper {
	   border-top: solid 6px #45474B;
}
header.major h2 {
    color: #379777;
    font-size: 3.5em;
}
header.major h2 + p {
    color: #677D6A;
    /* font-size: 1.75em; */
    /* font-weight: 700; */
    /* margin-top: -0.75em; */
}
p , a{
	color: #379777;
    margin: 0 0 2.25em 0;
}	
header.major h2 + p {
    color: #379777;
    /* font-size: 1.75em; */
    /* font-weight: 700; */
    /* margin-top: -0.75em; */
}""", "sakura":"""@import url("fontawesome-all.min.css");
@import url("https://fonts.googleapis.com/css?family=Lato:400,400italic,700,700italic|Source+Code+Pro:400");


html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #fff;
	}

		body.is-preload *, body.is-preload *:before, body.is-preload *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

	body, input, select, textarea {
		color: #888;
		font-family: "Lato", sans-serif;
		font-size: 16pt;
		font-weight: 400;
		line-height: 1.75em;
	}

	a {
		-moz-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-webkit-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-ms-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		border-bottom: solid 1px #e4e4e4;
		color: inherit;
		text-decoration: none;
	}

		a:hover {
			border-bottom-color: transparent;
			color: #F0A8D0 !important;
		}

	strong, b {
		color: #777;
		font-weight: 700;
	}

	em, i {
		font-style: italic;
	}

	p {
		margin: 0 0 2.25em 0;
	}

	h1, h2, h3, h4, h5, h6 {
		color: #777;
		font-weight: 700;
		line-height: 1em;
		margin: 0 0 0.5625em 0;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			border: 0;
			color: inherit;
			text-decoration: none;
		}

	h2 {
		font-size: 2em;
		line-height: 1.5em;
	}

	h3 {
		font-size: 1.75em;
		line-height: 1.5em;
	}

	h4 {
		font-size: 1.25em;
		line-height: 1.5em;
	}

	h5 {
		font-size: 0.9em;
		line-height: 1.5em;
	}

	h6 {
		font-size: 0.7em;
		line-height: 1.5em;
	}

	sub {
		font-size: 0.8em;
		position: relative;
		top: 0.5em;
	}

	sup {
		font-size: 0.8em;
		position: relative;
		top: -0.5em;
	}

	hr {
		border: 0;
		border-bottom: solid 2px #f4f4f4;
		margin: 2.25em 0;
	}

		hr.major {
			margin: 3.375em 0;
		}

	blockquote {
		border-left: solid 8px #e4e4e4;
		font-style: italic;
		margin: 0 0 2.25em 0;
		padding: 0.5em 0 0.5em 2em;
	}

	code {
		background: #555;
		border-radius: 5px;
		color: #fff;
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0.25em;
		padding: 0.25em 0.65em;
	}

	pre {
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0 2.25em 0;
	}

		pre code {
			-webkit-overflow-scrolling: touch;
			display: block;
			line-height: 1.5em;
			overflow-x: auto;
			padding: 1em 1.5em;
		}

	.align-left {
		text-align: left;
	}

	.align-center {
		text-align: center;
	}

	.align-right {
		text-align: right;
	}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0;
			margin-left: 0em;
		}

			.row.gtr-0 > * {
				padding: 0 0 0 0em;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0em;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0em;
				}

		.row.gtr-25 {
			margin-top: 0;
			margin-left: -0.5em;
		}

			.row.gtr-25 > * {
				padding: 0 0 0 0.5em;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -0.5em;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 0.5em;
				}

		.row.gtr-50 {
			margin-top: 0;
			margin-left: -1em;
		}

			.row.gtr-50 > * {
				padding: 0 0 0 1em;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -1em;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 1em;
				}

		.row {
			margin-top: 0;
			margin-left: -2em;
		}

			.row > * {
				padding: 0 0 0 2em;
			}

			.row.gtr-uniform {
				margin-top: -2em;
			}

				.row.gtr-uniform > * {
					padding-top: 2em;
				}

		.row.gtr-150 {
			margin-top: 0;
			margin-left: -3em;
		}

			.row.gtr-150 > * {
				padding: 0 0 0 3em;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -3em;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 3em;
				}

		.row.gtr-200 {
			margin-top: 0;
			margin-left: -4em;
		}

			.row.gtr-200 > * {
				padding: 0 0 0 4em;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -4em;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 4em;
				}

		@media screen and (max-width: 1680px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xlarge {
					order: -1;
				}

				.row > .col-1-xlarge {
					width: 8.33333%;
				}

				.row > .off-1-xlarge {
					margin-left: 8.33333%;
				}

				.row > .col-2-xlarge {
					width: 16.66667%;
				}

				.row > .off-2-xlarge {
					margin-left: 16.66667%;
				}

				.row > .col-3-xlarge {
					width: 25%;
				}

				.row > .off-3-xlarge {
					margin-left: 25%;
				}

				.row > .col-4-xlarge {
					width: 33.33333%;
				}

				.row > .off-4-xlarge {
					margin-left: 33.33333%;
				}

				.row > .col-5-xlarge {
					width: 41.66667%;
				}

				.row > .off-5-xlarge {
					margin-left: 41.66667%;
				}

				.row > .col-6-xlarge {
					width: 50%;
				}

				.row > .off-6-xlarge {
					margin-left: 50%;
				}

				.row > .col-7-xlarge {
					width: 58.33333%;
				}

				.row > .off-7-xlarge {
					margin-left: 58.33333%;
				}

				.row > .col-8-xlarge {
					width: 66.66667%;
				}

				.row > .off-8-xlarge {
					margin-left: 66.66667%;
				}

				.row > .col-9-xlarge {
					width: 75%;
				}

				.row > .off-9-xlarge {
					margin-left: 75%;
				}

				.row > .col-10-xlarge {
					width: 83.33333%;
				}

				.row > .off-10-xlarge {
					margin-left: 83.33333%;
				}

				.row > .col-11-xlarge {
					width: 91.66667%;
				}

				.row > .off-11-xlarge {
					margin-left: 91.66667%;
				}

				.row > .col-12-xlarge {
					width: 100%;
				}

				.row > .off-12-xlarge {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -1em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 1em;
						}

				.row {
					margin-top: 0;
					margin-left: -2em;
				}

					.row > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-uniform > * {
							padding-top: 2em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 3em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -4em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 4em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -4em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 4em;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-large {
					order: -1;
				}

				.row > .col-1-large {
					width: 8.33333%;
				}

				.row > .off-1-large {
					margin-left: 8.33333%;
				}

				.row > .col-2-large {
					width: 16.66667%;
				}

				.row > .off-2-large {
					margin-left: 16.66667%;
				}

				.row > .col-3-large {
					width: 25%;
				}

				.row > .off-3-large {
					margin-left: 25%;
				}

				.row > .col-4-large {
					width: 33.33333%;
				}

				.row > .off-4-large {
					margin-left: 33.33333%;
				}

				.row > .col-5-large {
					width: 41.66667%;
				}

				.row > .off-5-large {
					margin-left: 41.66667%;
				}

				.row > .col-6-large {
					width: 50%;
				}

				.row > .off-6-large {
					margin-left: 50%;
				}

				.row > .col-7-large {
					width: 58.33333%;
				}

				.row > .off-7-large {
					margin-left: 58.33333%;
				}

				.row > .col-8-large {
					width: 66.66667%;
				}

				.row > .off-8-large {
					margin-left: 66.66667%;
				}

				.row > .col-9-large {
					width: 75%;
				}

				.row > .off-9-large {
					margin-left: 75%;
				}

				.row > .col-10-large {
					width: 83.33333%;
				}

				.row > .off-10-large {
					margin-left: 83.33333%;
				}

				.row > .col-11-large {
					width: 91.66667%;
				}

				.row > .off-11-large {
					margin-left: 91.66667%;
				}

				.row > .col-12-large {
					width: 100%;
				}

				.row > .off-12-large {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 1024px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-medium {
					order: -1;
				}

				.row > .col-1-medium {
					width: 8.33333%;
				}

				.row > .off-1-medium {
					margin-left: 8.33333%;
				}

				.row > .col-2-medium {
					width: 16.66667%;
				}

				.row > .off-2-medium {
					margin-left: 16.66667%;
				}

				.row > .col-3-medium {
					width: 25%;
				}

				.row > .off-3-medium {
					margin-left: 25%;
				}

				.row > .col-4-medium {
					width: 33.33333%;
				}

				.row > .off-4-medium {
					margin-left: 33.33333%;
				}

				.row > .col-5-medium {
					width: 41.66667%;
				}

				.row > .off-5-medium {
					margin-left: 41.66667%;
				}

				.row > .col-6-medium {
					width: 50%;
				}

				.row > .off-6-medium {
					margin-left: 50%;
				}

				.row > .col-7-medium {
					width: 58.33333%;
				}

				.row > .off-7-medium {
					margin-left: 58.33333%;
				}

				.row > .col-8-medium {
					width: 66.66667%;
				}

				.row > .off-8-medium {
					margin-left: 66.66667%;
				}

				.row > .col-9-medium {
					width: 75%;
				}

				.row > .off-9-medium {
					margin-left: 75%;
				}

				.row > .col-10-medium {
					width: 83.33333%;
				}

				.row > .off-10-medium {
					margin-left: 83.33333%;
				}

				.row > .col-11-medium {
					width: 91.66667%;
				}

				.row > .off-11-medium {
					margin-left: 91.66667%;
				}

				.row > .col-12-medium {
					width: 100%;
				}

				.row > .off-12-medium {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-small {
					order: -1;
				}

				.row > .col-1-small {
					width: 8.33333%;
				}

				.row > .off-1-small {
					margin-left: 8.33333%;
				}

				.row > .col-2-small {
					width: 16.66667%;
				}

				.row > .off-2-small {
					margin-left: 16.66667%;
				}

				.row > .col-3-small {
					width: 25%;
				}

				.row > .off-3-small {
					margin-left: 25%;
				}

				.row > .col-4-small {
					width: 33.33333%;
				}

				.row > .off-4-small {
					margin-left: 33.33333%;
				}

				.row > .col-5-small {
					width: 41.66667%;
				}

				.row > .off-5-small {
					margin-left: 41.66667%;
				}

				.row > .col-6-small {
					width: 50%;
				}

				.row > .off-6-small {
					margin-left: 50%;
				}

				.row > .col-7-small {
					width: 58.33333%;
				}

				.row > .off-7-small {
					margin-left: 58.33333%;
				}

				.row > .col-8-small {
					width: 66.66667%;
				}

				.row > .off-8-small {
					margin-left: 66.66667%;
				}

				.row > .col-9-small {
					width: 75%;
				}

				.row > .off-9-small {
					margin-left: 75%;
				}

				.row > .col-10-small {
					width: 83.33333%;
				}

				.row > .off-10-small {
					margin-left: 83.33333%;
				}

				.row > .col-11-small {
					width: 91.66667%;
				}

				.row > .off-11-small {
					margin-left: 91.66667%;
				}

				.row > .col-12-small {
					width: 100%;
				}

				.row > .off-12-small {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

		@media screen and (max-width: 480px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xsmall {
					order: -1;
				}

				.row > .col-1-xsmall {
					width: 8.33333%;
				}

				.row > .off-1-xsmall {
					margin-left: 8.33333%;
				}

				.row > .col-2-xsmall {
					width: 16.66667%;
				}

				.row > .off-2-xsmall {
					margin-left: 16.66667%;
				}

				.row > .col-3-xsmall {
					width: 25%;
				}

				.row > .off-3-xsmall {
					margin-left: 25%;
				}

				.row > .col-4-xsmall {
					width: 33.33333%;
				}

				.row > .off-4-xsmall {
					margin-left: 33.33333%;
				}

				.row > .col-5-xsmall {
					width: 41.66667%;
				}

				.row > .off-5-xsmall {
					margin-left: 41.66667%;
				}

				.row > .col-6-xsmall {
					width: 50%;
				}

				.row > .off-6-xsmall {
					margin-left: 50%;
				}

				.row > .col-7-xsmall {
					width: 58.33333%;
				}

				.row > .off-7-xsmall {
					margin-left: 58.33333%;
				}

				.row > .col-8-xsmall {
					width: 66.66667%;
				}

				.row > .off-8-xsmall {
					margin-left: 66.66667%;
				}

				.row > .col-9-xsmall {
					width: 75%;
				}

				.row > .off-9-xsmall {
					margin-left: 75%;
				}

				.row > .col-10-xsmall {
					width: 83.33333%;
				}

				.row > .off-10-xsmall {
					margin-left: 83.33333%;
				}

				.row > .col-11-xsmall {
					width: 91.66667%;
				}

				.row > .off-11-xsmall {
					margin-left: 91.66667%;
				}

				.row > .col-12-xsmall {
					width: 100%;
				}

				.row > .off-12-xsmall {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

/* Container */

	.container {
		margin: 0 auto;
		max-width: calc(100% - 4.5em);
		width: 45em;
	}

		.container.xsmall {
			width: 11.25em;
		}

		.container.small {
			width: 22.5em;
		}

		.container.medium {
			width: 33.75em;
		}

		.container.large {
			width: 56.25em;
		}

		.container.xlarge {
			width: 67.5em;
		}

		.container.max {
			width: 100%;
		}

		@media screen and (max-width: 1024px) {

			.container {
				width: 100% !important;
			}

		}

		@media screen and (max-width: 480px) {

			.container {
				max-width: calc(100% - 3.375em);
			}

		}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header p {
		color: #aaa;
		position: relative;
		margin: 0 0 1.6875em 0;
	}

	header h2 + p {
		font-size: 1.25em;
		margin-top: -0.5em;
		line-height: 1.5em;
	}

	header h3 + p {
		font-size: 1.1em;
		margin-top: -0.35em;
		line-height: 1.5em;
	}

	header h4 + p,
	header h5 + p,
	header h6 + p {
		font-size: 0.9em;
		margin-top: -0.25em;
		line-height: 1.5em;
	}

	header.major h2 {
		color: #F0A8D0;
		font-size: 3.5em;
	}

		header.major h2 + p {
			color: #777;
			font-size: 1.75em;
			font-weight: 700;
			margin-top: -0.75em;
		}

/* Form */

	form {
		margin: 0 0 2.25em 0;
	}

	label {
		color: #777;
		display: block;
		font-size: 0.9em;
		font-weight: 700;
		margin: 0 0 1.125em 0;
	}

	input::-moz-focus-inner {
		border: 0;
		padding: 0;
	}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select,
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		border-radius: 5px;
		border: none;
		border: solid 2px #e4e4e4;
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 1em;
		text-decoration: none;
		width: 100%;
	}

		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		select:focus,
		textarea:focus {
			border-color: #F0A8D0;
		}

	select {
		background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' preserveAspectRatio='none' viewBox='0 0 40 40'%3E%3Cpath d='M9.4,12.3l10.4,10.4l10.4-10.4c0.2-0.2,0.5-0.4,0.9-0.4c0.3,0,0.6,0.1,0.9,0.4l3.3,3.3c0.2,0.2,0.4,0.5,0.4,0.9 c0,0.4-0.1,0.6-0.4,0.9L20.7,31.9c-0.2,0.2-0.5,0.4-0.9,0.4c-0.3,0-0.6-0.1-0.9-0.4L4.3,17.3c-0.2-0.2-0.4-0.5-0.4-0.9 c0-0.4,0.1-0.6,0.4-0.9l3.3-3.3c0.2-0.2,0.5-0.4,0.9-0.4S9.1,12.1,9.4,12.3z' fill='%23e4e4e4' /%3E%3C/svg%3E");
		background-size: 1.25em;
		background-repeat: no-repeat;
		background-position: calc(100% - 1em) center;
		height: 2.75em;
		padding-right: 2.75em;
		text-overflow: ellipsis;
	}

		select option {
			color: #777;
			background: #fff;
		}

		select:focus::-ms-value {
			background-color: transparent;
		}

		select::-ms-expand {
			display: none;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 2.75em;
	}

	textarea {
		padding: 0.75em 1em;
	}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2em;
		opacity: 0;
		width: 1em;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			color: #888;
			cursor: pointer;
			display: inline-block;
			font-size: 1em;
			font-weight: 400;
			padding-left: 2.4em;
			padding-right: 0.75em;
			position: relative;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				background: #fafafa;
				border-radius: 5px;
				border: solid 2px #e4e4e4;
				content: '';
				display: inline-block;
				font-size: 0.8em;
				height: 2.0625em;
				left: 0;
				line-height: 2.0625em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.0625em;
			}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			background: #989898;
			border-color: #989898;
			color: #FFEBD4;
			content: '\\f00c';
		}

		input[type="checkbox"]:focus + label:before,
		input[type="radio"]:focus + label:before {
			border-color: #F0A8D0;
		}

	input[type="checkbox"] + label:before {
		border-radius: 5px;
	}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	::-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

/* Box */

	.box {
		border-radius: 5px;
		border: solid 2px #e4e4e4;
		margin-bottom: 2.25em;
		padding: 1.5em;
	}

		.box > :last-child,
		.box > :last-child > :last-child,
		.box > :last-child > :last-child > :last-child {
			margin-bottom: 0;
		}

		.box.alt {
			border: 0;
			border-radius: 0;
			padding: 0;
		}

/* Icon */

	.icon {
		text-decoration: none;
		border-bottom: none;
		position: relative;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 400;
		}

		.icon > .label {
			display: none;
		}

		.icon:before {
			line-height: inherit;
		}

		.icon.solid:before {
			font-weight: 900;
		}

		.icon.brands:before {
			font-family: 'Font Awesome 5 Brands';
		}

/* Image */

	.image {
		border-radius: 5px;
		border: 0;
		display: inline-block;
		position: relative;
	}

		.image[data-position] img {
			-moz-object-fit: cover;
			-webkit-object-fit: cover;
			-ms-object-fit: cover;
			object-fit: cover;
			display: block;
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
		}

		.image[data-position="top left"] img {
			-moz-object-position: top left;
			-webkit-object-position: top left;
			-ms-object-position: top left;
			object-position: top left;
		}

		.image[data-position="top"] img {
			-moz-object-position: top;
			-webkit-object-position: top;
			-ms-object-position: top;
			object-position: top;
		}

		.image[data-position="top right"] img {
			-moz-object-position: top right;
			-webkit-object-position: top right;
			-ms-object-position: top right;
			object-position: top right;
		}

		.image[data-position="right"] img {
			-moz-object-position: right;
			-webkit-object-position: right;
			-ms-object-position: right;
			object-position: right;
		}

		.image[data-position="bottom right"] img {
			-moz-object-position: bottom right;
			-webkit-object-position: bottom right;
			-ms-object-position: bottom right;
			object-position: bottom right;
		}

		.image[data-position="bottom"] img {
			-moz-object-position: bottom;
			-webkit-object-position: bottom;
			-ms-object-position: bottom;
			object-position: bottom;
		}

		.image[data-position="bottom left"] img {
			-moz-object-position: bottom left;
			-webkit-object-position: bottom left;
			-ms-object-position: bottom left;
			object-position: bottom left;
		}

		.image[data-position="left"] img {
			-moz-object-position: left;
			-webkit-object-position: left;
			-ms-object-position: left;
			object-position: left;
		}

		.image[data-position="center"] img {
			-moz-object-position: center;
			-webkit-object-position: center;
			-ms-object-position: center;
			object-position: center;
		}

		.image[data-position="25% 25%"] img {
			-moz-object-position: 25% 25%;
			-webkit-object-position: 25% 25%;
			-ms-object-position: 25% 25%;
			object-position: 25% 25%;
		}

		.image[data-position="75% 25%"] img {
			-moz-object-position: 75% 25%;
			-webkit-object-position: 75% 25%;
			-ms-object-position: 75% 25%;
			object-position: 75% 25%;
		}

		.image[data-position="75% 75%"] img {
			-moz-object-position: 75% 75%;
			-webkit-object-position: 75% 75%;
			-ms-object-position: 75% 75%;
			object-position: 75% 75%;
		}

		.image[data-position="25% 75%"] img {
			-moz-object-position: 25% 75%;
			-webkit-object-position: 25% 75%;
			-ms-object-position: 25% 75%;
			object-position: 25% 75%;
		}

		.image img {
			border-radius: 5px;
			display: block;
		}

		.image.left {
			float: left;
			margin: 0 2.5em 2em 0;
			top: 0.25em;
		}

		.image.right {
			float: right;
			margin: 0 0 2em 2.5em;
			top: 0.25em;
		}

		.image.fit {
			display: block;
			margin: 0 0 2.25em 0;
			width: 100%;
		}

			.image.fit img {
				display: block;
				width: 100%;
			}

		.image.avatar {
			border-radius: 100%;
			overflow: hidden;
		}

			.image.avatar img {
				border-radius: 100%;
				display: block;
				width: 100%;
			}

		.image.main {
			display: block;
			height: 20em;
			border-radius: 0;
		}

			.image.main img {
				border-radius: 0;
			}

/* List */

	ol {
		list-style: decimal;
		margin: 0 0 2.25em 0;
		padding-left: 1.25em;
	}

		ol li {
			padding-left: 0.25em;
		}

	ul {
		list-style: disc;
		margin: 0 0 2.25em 0;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
		}

		ul.alt {
			list-style: none;
			padding-left: 0;
		}

			ul.alt li {
				border-top: solid 2px #f4f4f4;
				padding: 0.5em 0;
			}

				ul.alt li:first-child {
					border-top: 0;
					padding-top: 0;
				}

	dl {
		margin: 0 0 2.25em 0;
	}

/* Actions */

	ul.actions {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		cursor: default;
		list-style: none;
		margin-left: -1.125em;
		padding-left: 0;
	}

		ul.actions li {
			padding: 0 0 0 1.125em;
			vertical-align: middle;
		}

		ul.actions.special {
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 100%;
			margin-left: 0;
		}

			ul.actions.special li:first-child {
				padding-left: 0;
			}

		ul.actions.stacked {
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			margin-left: 0;
		}

			ul.actions.stacked li {
				padding: 1.125em 0 0 0;
			}

				ul.actions.stacked li:first-child {
					padding-top: 0;
				}

		ul.actions.fit {
			width: calc(100% + 1.125em);
		}

			ul.actions.fit li {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				width: 100%;
			}

				ul.actions.fit li > * {
					width: 100%;
				}

			ul.actions.fit.stacked {
				width: 100%;
			}

		@media screen and (max-width: 480px) {

			ul.actions:not(.fixed) {
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
				margin-left: 0;
				width: 100% !important;
			}

				ul.actions:not(.fixed) li {
					-moz-flex-grow: 1;
					-webkit-flex-grow: 1;
					-ms-flex-grow: 1;
					flex-grow: 1;
					-moz-flex-shrink: 1;
					-webkit-flex-shrink: 1;
					-ms-flex-shrink: 1;
					flex-shrink: 1;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions:not(.fixed) li > * {
						width: 100%;
					}

					ul.actions:not(.fixed) li:first-child {
						padding-top: 0;
					}

					ul.actions:not(.fixed) li input[type="submit"],
					ul.actions:not(.fixed) li input[type="reset"],
					ul.actions:not(.fixed) li input[type="button"],
					ul.actions:not(.fixed) li button,
					ul.actions:not(.fixed) li .button {
						width: 100%;
					}

						ul.actions:not(.fixed) li input[type="submit"].icon:before,
						ul.actions:not(.fixed) li input[type="reset"].icon:before,
						ul.actions:not(.fixed) li input[type="button"].icon:before,
						ul.actions:not(.fixed) li button.icon:before,
						ul.actions:not(.fixed) li .button.icon:before {
							margin-left: -0.5rem;
						}

		}

/* Feature Icons */

	ul.feature-icons {
		list-style: none;
		padding-left: 0;
	}

		ul.feature-icons li {
			text-decoration: none;
			display: inline-block;
			margin: 0 0 1.6875em 0;
			padding: 0.35em 0 0 3.5em;
			position: relative;
			vertical-align: top;
			width: 48%;
		}

			ul.feature-icons li:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 400;
			}

			ul.feature-icons li:before {
				background: #F0A8D0;
				border-radius: 100%;
				color: #ffffff;
				display: block;
				height: 2.5em;
				left: 0;
				line-height: 2.5em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.5em;
			}

/* Icons */

	ul.icons {
		cursor: default;
		list-style: none;
		padding-left: 0;
	}

		ul.icons li {
			display: inline-block;
			padding: 0 1em 0 0;
		}

			ul.icons li:last-child {
				padding-right: 0 !important;
			}

			ul.icons li .icon:before {
				font-size: 1.25em;
			}

/* Table */

	.table-wrapper {
		-webkit-overflow-scrolling: touch;
		overflow-x: auto;
	}

	table {
		margin: 0 0 2.25em 0;
		width: 100%;
	}

		table tbody tr {
			border: solid 2px #f4f4f4;
			border-left: 0;
			border-right: 0;
		}

			table tbody tr:nth-child(2n + 1) {
				background-color: #fafafa;
			}

		table td {
			padding: 0.75em 0.75em;
		}

		table th {
			color: #777;
			font-size: 0.9em;
			font-weight: 700;
			padding: 0 0.75em 0.75em 0.75em;
			text-align: left;
		}

		table thead {
			border-bottom: solid 4px #e4e4e4;
		}

		table tfoot {
			border-top: solid 4px #e4e4e4;
		}

		table.alt {
			border-collapse: separate;
		}

			table.alt tbody tr td {
				border: solid 2px #e4e4e4;
				border-left-width: 0;
				border-top-width: 0;
			}

				table.alt tbody tr td:first-child {
					border-left-width: 2px;
				}

			table.alt tbody tr:first-child td {
				border-top-width: 2px;
			}

			table.alt thead {
				border-bottom: 0;
			}

			table.alt tfoot {
				border-top: 0;
			}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		background-color: #989898;
		border-radius: 5px;
		border: 0;
		color: #ffffff !important;
		cursor: pointer;
		display: inline-block;
		font-weight: 700;
		height: 2.75em;
		line-height: 2.75em;
		padding: 0 1.5em;
		text-align: center;
		text-decoration: none;
		white-space: nowrap;
	}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		.button:hover {
			background-color: #a5a5a5;
			color: #ffffff !important;
		}

		input[type="submit"]:active,
		input[type="reset"]:active,
		input[type="button"]:active,
		.button:active {
			background-color: #8b8b8b;
		}

		input[type="submit"].icon,
		input[type="reset"].icon,
		input[type="button"].icon,
		.button.icon {
			padding-left: 1.35em;
		}

			input[type="submit"].icon:before,
			input[type="reset"].icon:before,
			input[type="button"].icon:before,
			.button.icon:before {
				margin-right: 0.5em;
			}

		input[type="submit"].fit,
		input[type="reset"].fit,
		input[type="button"].fit,
		.button.fit {
			width: 100%;
		}

		input[type="submit"].small,
		input[type="reset"].small,
		input[type="button"].small,
		.button.small {
			font-size: 0.8em;
		}

		input[type="submit"].large,
		input[type="reset"].large,
		input[type="button"].large,
		.button.large {
			font-size: 1.35em;
		}

		input[type="submit"].alt,
		input[type="reset"].alt,
		input[type="button"].alt,
		.button.alt {
			background-color: transparent;
			box-shadow: inset 0 0 0 2px #e4e4e4;
			color: #777 !important;
		}

			input[type="submit"].alt:hover,
			input[type="reset"].alt:hover,
			input[type="button"].alt:hover,
			.button.alt:hover {
				background-color: #f4f4f4;
				color: #777 !important;
			}

			input[type="submit"].alt:active,
			input[type="reset"].alt:active,
			input[type="button"].alt:active,
			.button.alt:active {
				background-color: #eaeaea;
			}

			input[type="submit"].alt.icon:before,
			input[type="reset"].alt.icon:before,
			input[type="button"].alt.icon:before,
			.button.alt.icon:before {
				color: #aaa;
			}

		input[type="submit"].primary,
		input[type="reset"].primary,
		input[type="button"].primary,
		.button.primary {
			background-color: #F0A8D0;
			color: #ffffff !important;
		}

			input[type="submit"].primary:hover,
			input[type="reset"].primary:hover,
			input[type="button"].primary:hover,
			.button.primary:hover {
				background-color: #5ed0b1;
			}

			input[type="submit"].primary:active,
			input[type="reset"].primary:active,
			input[type="button"].primary:active,
			.button.primary:active {
				background-color: #39c29d;
			}

		input[type="submit"].disabled, input[type="submit"]:disabled,
		input[type="reset"].disabled,
		input[type="reset"]:disabled,
		input[type="button"].disabled,
		input[type="button"]:disabled,
		.button.disabled,
		.button:disabled {
			background-color: #888 !important;
			box-shadow: inset 0 -0.15em 0 0 rgba(0, 0, 0, 0.15);
			color: #fff !important;
			cursor: default;
			opacity: 0.25;
		}

/* Features */

	.features article {
		border-top: solid 3px #f4f4f4;
		margin-bottom: 2.25em;
		padding-top: 2.25em;
	}

		.features article:first-child {
			border-top: 0;
			padding-top: 0;
		}

		.features article .image {
			display: inline-block;
			padding-right: 2.5em;
			vertical-align: middle;
			width: 48%;
		}

			.features article .image img {
				display: block;
				width: 100%;
			}

		.features article .inner {
			display: inline-block;
			vertical-align: middle;
			width: 50%;
		}

			.features article .inner > :last-child {
				margin-bottom: 0;
			}

/* Header */

	#header {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: column;
		-webkit-flex-direction: column;
		-ms-flex-direction: column;
		flex-direction: column;
		-moz-justify-content: space-between;
		-webkit-justify-content: space-between;
		-ms-justify-content: space-between;
		justify-content: space-between;
		background: #F0A8D0;
		color: #d2f2e9;
		height: 100%;
		overflow-y: auto;
		position: fixed;
		text-align: center;
		top: 0;
		width: 23em;
		right: 0;
	}

		#header h1, #header h2, #header h3, #header h4, #header h5, #header h6 {
			color: #ffffff;
		}

			#header h1 a, #header h2 a, #header h3 a, #header h4 a, #header h5 a, #header h6 a {
				color: #ffffff;
			}

		#header header p {
			color: #FFEBD4;
		}

		#header a {
			color: #d2f2e9;
		}

			#header a:hover {
				color: #ffffff !important;
			}

		#header > header {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			padding: 3em;
		}

			#header > header .avatar {
				display: block;
				margin: 0 auto 2.25em auto;
				width: 8em;
			}

			#header > header h1 {
				font-size: 1.75em;
				margin: 0;
			}

			#header > header p {
				color: #d2f2e9;
				font-style: italic;
				margin: 1em 0 0 0;
			}

		#header > footer {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			bottom: 0;
			left: 0;
			padding: 2em;
			width: 100%;
		}

			#header > footer .icons {
				margin: 0;
			}

				#header > footer .icons li a {
					color: #FFEBD4;
				}

		#header > nav {
			-moz-flex-grow: 1;
			-webkit-flex-grow: 1;
			-ms-flex-grow: 1;
			flex-grow: 1;
		}

			#header > nav ul {
				list-style: none;
				margin: 0;
				padding: 0;
			}

				#header > nav ul li {
					border-top: solid 2px #5ccfb1;
					display: block;
					padding: 0;
				}

					#header > nav ul li a {
						-moz-transition: none;
						-webkit-transition: none;
						-ms-transition: none;
						transition: none;
						border: 0;
						color: #ffffff !important;
						display: block;
						padding: 0.85em 0;
						text-decoration: none;
					}

						#header > nav ul li a.active {
							background: #fff;
							color: #F0A8D0 !important;
						}

					#header > nav ul li:first-child {
						border-top: 0;
					}

/* Wrapper */

	#wrapper {
		background: #fff;
		padding-right: 23em;
	}

/* Main */

	#main > section {
		border-top: solid 6px #f4f4f4;
	}

		#main > section > .container {
			padding: 6em 0 4em 0;
		}

		#main > section:first-child {
			border-top: 0;
		}

/* Footer */

	#footer {
		background: #fafafa;
		border-top: 0;
		color: #c0c0c0;
		overflow: hidden;
		padding: 4em 0 2em 0;
	}

		#footer .copyright {
			line-height: 1em;
			list-style: none;
			padding: 0;
		}

			#footer .copyright li {
				border-left: solid 1px #d4d4d4;
				display: inline-block;
				font-size: 0.8em;
				margin-left: 1em;
				padding-left: 1em;
			}

				#footer .copyright li:first-child {
					border-left: 0;
					margin-left: 0;
					padding-left: 0;
				}

				#footer .copyright li a {
					color: inherit;
				}

/* XLarge */

	@media screen and (max-width: 1680px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 13pt;
			}

		/* Header */

			#header {
				width: 21em;
			}

				#header > header {
					padding: 2em;
				}

				#header > footer {
					padding: 1.5em;
				}

		/* Wrapper */

			#wrapper {
				padding-right: 21em;
			}

		/* Main */

			#main > section > .container {
				padding: 4em 0 2em 0;
			}

	}

/* Large */

	@media screen and (max-width: 1280px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 11pt;
			}

		/* Header */

			#header {
				width: 20em;
			}

		/* Wrapper */

			#wrapper {
				padding-right: 20em;
			}

	}

/* Medium */

	#titleBar {
		display: none;
	}

	@media screen and (max-width: 1024px) {

		/* Basic */

			html, body {
				overflow-x: hidden;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* Image */

			.image.left, .image.right {
				max-width: 40%;
			}

				.image.left img, .image.right img {
					width: 100%;
				}

			.image.main {
				height: 20em;
			}

		/* Header */

			#header {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 100%;
				overflow-y: auto;
				position: fixed;
				top: 0;
				width: 23em;
				z-index: 10002;
				-moz-transform: translateX(23em);
				-webkit-transform: translateX(23em);
				-ms-transform: translateX(23em);
				transform: translateX(23em);
				right: 0;
			}

				#header > footer {
					bottom: auto;
					left: auto;
					margin: 0.5em 0 0 0;
					position: relative;
					right: auto;
					top: auto;
				}

		/* Wrapper */

			#wrapper {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				padding: 44px 0 1px 0;
			}

		/* Header Panel */

			#titleBar {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 44px;
				left: 0;
				position: fixed;
				top: 0;
				width: 100%;
				z-index: 10001;
				background: #222;
				color: #fff;
				min-width: 320px;
			}

				#titleBar .title {
					color: #fff;
					display: block;
					font-weight: 700;
					height: 44px;
					line-height: 44px;
					padding: 0 1em;
					width: 100%;
					text-align: left;
				}

					#titleBar .title a {
						border: 0;
						text-decoration: none;
					}

				#titleBar .toggle {
					text-decoration: none;
					height: 4em;
					position: absolute;
					top: 0;
					width: 6em;
					border: 0;
					outline: 0;
					right: 0;
				}

					#titleBar .toggle:before {
						-moz-osx-font-smoothing: grayscale;
						-webkit-font-smoothing: antialiased;
						display: inline-block;
						font-style: normal;
						font-variant: normal;
						text-rendering: auto;
						line-height: 1;
						text-transform: none !important;
						font-family: 'Font Awesome 5 Free';
						font-weight: 900;
					}

					#titleBar .toggle:before {
						background: #F0A8D0;
						color: #ffffff;
						content: '\\f0c9';
						display: block;
						font-size: 18px;
						height: 44px;
						line-height: 44px;
						position: absolute;
						text-align: center;
						top: 0;
						width: 64px;
						right: 0;
					}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-23em);
				-webkit-transform: translateX(-23em);
				-ms-transform: translateX(-23em);
				transform: translateX(-23em);
			}

			body.header-visible #header {
				-moz-transform: translateX(0);
				-webkit-transform: translateX(0);
				-ms-transform: translateX(0);
				transform: translateX(0);
			}

	}

/* Small */

	@media screen and (max-width: 736px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 12pt;
			}

			h1 br, h2 br, h3 br, h4 br, h5 br, h6 br {
				display: none;
			}

			h2 {
				font-size: 1.75em;
			}

			h3 {
				font-size: 1.5em;
			}

			h4 {
				font-size: 1em;
			}

		/* Image */

			.image.left {
				margin: 0 1.5em 1em 0;
			}

			.image.right {
				margin: 0 0 1em 1.5em;
			}

			.image.main {
				height: 12em;
			}

		/* Section/Article */

			header br {
				display: none;
			}

			header.major h2 {
				font-size: 2.5em;
			}

				header.major h2 + p {
					font-size: 1.5em;
				}

		/* Features */

			.features article .image {
				display: block;
				margin: 0 0 2.25em 0;
				padding-right: 0;
				width: 100%;
			}

			.features article .inner {
				display: block;
				width: 100%;
			}

		/* Header */

			#header {
				width: 17em;
				-moz-transform: translateX(17em);
				-webkit-transform: translateX(17em);
				-ms-transform: translateX(17em);
				transform: translateX(17em);
				right: 0;
			}

				#header > header {
					padding: 2em;
				}

					#header > header .avatar {
						margin: 0 auto 1.6875em auto;
						width: 6em;
					}

					#header > header h1 {
						font-size: 1.5em;
					}

					#header > header p {
						margin: 1em 0 0 0;
					}

				#header > footer {
					padding: 1.5em;
				}

		/* Main */

			#main > section > .container {
				padding: 2em 0 0 0;
			}

		/* Footer */

			#footer {
				text-align: center;
			}

				#footer .copyright li {
					border-left: 0;
					display: block;
					line-height: 1.75em;
					margin: 0.75em 0 0 0;
					padding-left: 0;
				}

					#footer .copyright li:first-child {
						margin-top: 0;
					}

		/* Header Panel */

			#titleBar .toggle {
				height: 4em;
				width: 6em;
			}

				#titleBar .toggle:before {
					font-size: 14px;
					width: 44px;
				}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-17em);
				-webkit-transform: translateX(-17em);
				-ms-transform: translateX(-17em);
				transform: translateX(-17em);
			}

	}

/* XSmall */

	@media screen and (max-width: 480px) {

		/* Basic */

			html, body {
				min-width: 320px;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* List */

			ul.actions {
				margin: 0 0 2.25em 0;
			}

				ul.actions li {
					display: block;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions li:first-child {
						padding-top: 0;
					}

					ul.actions li > * {
						width: 100%;
						margin: 0 !important;
					}

						ul.actions li > *.icon:before {
							margin-left: -2em;
						}

				ul.actions.small li {
					padding: 0.5625em 0 0 0;
				}

					ul.actions.small li:first-child {
						padding-top: 0;
					}

			ul.feature-icons li {
				display: block;
				width: 100%;
			}

		/* Button */

			input[type="submit"],
			input[type="reset"],
			input[type="button"],
			.button {
				padding: 0;
			}

	}
	/* Define the colors */
:root {
    --color-primary: #FFEBD4;
    --color-secondary: #F7B5CA;
    --color-tertiary: #F7B5CA;
    --color-quaternary: #F0A8D0;
}

/* Example usage of the colors */
body {
    background-color: var(--color-primary);
    color: var(--color-quaternary);
}

.header {
    background-color: var(--color-secondary);
    color: var(--color-primary);
}

.button {
    background-color: var(--color-tertiary);
    color: var(--color-primary);
}

.footer {
    background-color: var(--color-quaternary);
    color: var(--color-secondary);
}

#main {
    background-color: #FFEBD4;
}
#header {
    background-color: #F7B5CA;
}
#header {
    background-color: #F7B5CA;
}
#footer , h1, h2, h3, h4{
	color: #F0A8D0;
}
#wrapper {
	   border-top: solid 6px #FFEBD4;
}
header.major h2 {
    color: #F0A8D0;
    font-size: 3.5em;
}
header.major h2 + p {
    color: #c96190;
    /* font-size: 1.75em; */
    /* font-weight: 700; */
    /* margin-top: -0.75em; */
}
#header > header p {
    color: #91163d;
    /* font-style: italic; */
    /* margin: 1em 0 0 0; */
}""", 
"valley":"""@import url("fontawesome-all.min.css");
@import url("https://fonts.googleapis.com/css?family=Lato:400,400italic,700,700italic|Source+Code+Pro:400");
html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #fff;
	}

		body.is-preload *, body.is-preload *:before, body.is-preload *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

	body, input, select, textarea {
		color: #888;
		font-family: "Lato", sans-serif;
		font-size: 16pt;
		font-weight: 400;
		line-height: 1.75em;
	}

	a {
		-moz-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-webkit-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-ms-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		border-bottom: solid 1px #e4e4e4;
		color: inherit;
		text-decoration: none;
	}

		a:hover {
			border-bottom-color: transparent;
			color: #D6BD98 !important;
		}

	strong, b {
		color: #777;
		font-weight: 700;
	}

	em, i {
		font-style: italic;
	}

	p {
		margin: 0 0 2.25em 0;
	}

	h1, h2, h3, h4, h5, h6 {
		color: #777;
		font-weight: 700;
		line-height: 1em;
		margin: 0 0 0.5625em 0;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			border: 0;
			color: inherit;
			text-decoration: none;
		}

	h2 {
		font-size: 2em;
		line-height: 1.5em;
	}

	h3 {
		font-size: 1.75em;
		line-height: 1.5em;
	}

	h4 {
		font-size: 1.25em;
		line-height: 1.5em;
	}

	h5 {
		font-size: 0.9em;
		line-height: 1.5em;
	}

	h6 {
		font-size: 0.7em;
		line-height: 1.5em;
	}

	sub {
		font-size: 0.8em;
		position: relative;
		top: 0.5em;
	}

	sup {
		font-size: 0.8em;
		position: relative;
		top: -0.5em;
	}

	hr {
		border: 0;
		border-bottom: solid 2px #f4f4f4;
		margin: 2.25em 0;
	}

		hr.major {
			margin: 3.375em 0;
		}

	blockquote {
		border-left: solid 8px #e4e4e4;
		font-style: italic;
		margin: 0 0 2.25em 0;
		padding: 0.5em 0 0.5em 2em;
	}

	code {
		background: #555;
		border-radius: 5px;
		color: #fff;
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0.25em;
		padding: 0.25em 0.65em;
	}

	pre {
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0 2.25em 0;
	}

		pre code {
			-webkit-overflow-scrolling: touch;
			display: block;
			line-height: 1.5em;
			overflow-x: auto;
			padding: 1em 1.5em;
		}

	.align-left {
		text-align: left;
	}

	.align-center {
		text-align: center;
	}

	.align-right {
		text-align: right;
	}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0;
			margin-left: 0em;
		}

			.row.gtr-0 > * {
				padding: 0 0 0 0em;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0em;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0em;
				}

		.row.gtr-25 {
			margin-top: 0;
			margin-left: -0.5em;
		}

			.row.gtr-25 > * {
				padding: 0 0 0 0.5em;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -0.5em;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 0.5em;
				}

		.row.gtr-50 {
			margin-top: 0;
			margin-left: -1em;
		}

			.row.gtr-50 > * {
				padding: 0 0 0 1em;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -1em;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 1em;
				}

		.row {
			margin-top: 0;
			margin-left: -2em;
		}

			.row > * {
				padding: 0 0 0 2em;
			}

			.row.gtr-uniform {
				margin-top: -2em;
			}

				.row.gtr-uniform > * {
					padding-top: 2em;
				}

		.row.gtr-150 {
			margin-top: 0;
			margin-left: -3em;
		}

			.row.gtr-150 > * {
				padding: 0 0 0 3em;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -3em;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 3em;
				}

		.row.gtr-200 {
			margin-top: 0;
			margin-left: -4em;
		}

			.row.gtr-200 > * {
				padding: 0 0 0 4em;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -4em;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 4em;
				}

		@media screen and (max-width: 1680px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xlarge {
					order: -1;
				}

				.row > .col-1-xlarge {
					width: 8.33333%;
				}

				.row > .off-1-xlarge {
					margin-left: 8.33333%;
				}

				.row > .col-2-xlarge {
					width: 16.66667%;
				}

				.row > .off-2-xlarge {
					margin-left: 16.66667%;
				}

				.row > .col-3-xlarge {
					width: 25%;
				}

				.row > .off-3-xlarge {
					margin-left: 25%;
				}

				.row > .col-4-xlarge {
					width: 33.33333%;
				}

				.row > .off-4-xlarge {
					margin-left: 33.33333%;
				}

				.row > .col-5-xlarge {
					width: 41.66667%;
				}

				.row > .off-5-xlarge {
					margin-left: 41.66667%;
				}

				.row > .col-6-xlarge {
					width: 50%;
				}

				.row > .off-6-xlarge {
					margin-left: 50%;
				}

				.row > .col-7-xlarge {
					width: 58.33333%;
				}

				.row > .off-7-xlarge {
					margin-left: 58.33333%;
				}

				.row > .col-8-xlarge {
					width: 66.66667%;
				}

				.row > .off-8-xlarge {
					margin-left: 66.66667%;
				}

				.row > .col-9-xlarge {
					width: 75%;
				}

				.row > .off-9-xlarge {
					margin-left: 75%;
				}

				.row > .col-10-xlarge {
					width: 83.33333%;
				}

				.row > .off-10-xlarge {
					margin-left: 83.33333%;
				}

				.row > .col-11-xlarge {
					width: 91.66667%;
				}

				.row > .off-11-xlarge {
					margin-left: 91.66667%;
				}

				.row > .col-12-xlarge {
					width: 100%;
				}

				.row > .off-12-xlarge {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -1em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 1em;
						}

				.row {
					margin-top: 0;
					margin-left: -2em;
				}

					.row > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-uniform > * {
							padding-top: 2em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 3em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -4em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 4em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -4em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 4em;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-large {
					order: -1;
				}

				.row > .col-1-large {
					width: 8.33333%;
				}

				.row > .off-1-large {
					margin-left: 8.33333%;
				}

				.row > .col-2-large {
					width: 16.66667%;
				}

				.row > .off-2-large {
					margin-left: 16.66667%;
				}

				.row > .col-3-large {
					width: 25%;
				}

				.row > .off-3-large {
					margin-left: 25%;
				}

				.row > .col-4-large {
					width: 33.33333%;
				}

				.row > .off-4-large {
					margin-left: 33.33333%;
				}

				.row > .col-5-large {
					width: 41.66667%;
				}

				.row > .off-5-large {
					margin-left: 41.66667%;
				}

				.row > .col-6-large {
					width: 50%;
				}

				.row > .off-6-large {
					margin-left: 50%;
				}

				.row > .col-7-large {
					width: 58.33333%;
				}

				.row > .off-7-large {
					margin-left: 58.33333%;
				}

				.row > .col-8-large {
					width: 66.66667%;
				}

				.row > .off-8-large {
					margin-left: 66.66667%;
				}

				.row > .col-9-large {
					width: 75%;
				}

				.row > .off-9-large {
					margin-left: 75%;
				}

				.row > .col-10-large {
					width: 83.33333%;
				}

				.row > .off-10-large {
					margin-left: 83.33333%;
				}

				.row > .col-11-large {
					width: 91.66667%;
				}

				.row > .off-11-large {
					margin-left: 91.66667%;
				}

				.row > .col-12-large {
					width: 100%;
				}

				.row > .off-12-large {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 1024px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-medium {
					order: -1;
				}

				.row > .col-1-medium {
					width: 8.33333%;
				}

				.row > .off-1-medium {
					margin-left: 8.33333%;
				}

				.row > .col-2-medium {
					width: 16.66667%;
				}

				.row > .off-2-medium {
					margin-left: 16.66667%;
				}

				.row > .col-3-medium {
					width: 25%;
				}

				.row > .off-3-medium {
					margin-left: 25%;
				}

				.row > .col-4-medium {
					width: 33.33333%;
				}

				.row > .off-4-medium {
					margin-left: 33.33333%;
				}

				.row > .col-5-medium {
					width: 41.66667%;
				}

				.row > .off-5-medium {
					margin-left: 41.66667%;
				}

				.row > .col-6-medium {
					width: 50%;
				}

				.row > .off-6-medium {
					margin-left: 50%;
				}

				.row > .col-7-medium {
					width: 58.33333%;
				}

				.row > .off-7-medium {
					margin-left: 58.33333%;
				}

				.row > .col-8-medium {
					width: 66.66667%;
				}

				.row > .off-8-medium {
					margin-left: 66.66667%;
				}

				.row > .col-9-medium {
					width: 75%;
				}

				.row > .off-9-medium {
					margin-left: 75%;
				}

				.row > .col-10-medium {
					width: 83.33333%;
				}

				.row > .off-10-medium {
					margin-left: 83.33333%;
				}

				.row > .col-11-medium {
					width: 91.66667%;
				}

				.row > .off-11-medium {
					margin-left: 91.66667%;
				}

				.row > .col-12-medium {
					width: 100%;
				}

				.row > .off-12-medium {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-small {
					order: -1;
				}

				.row > .col-1-small {
					width: 8.33333%;
				}

				.row > .off-1-small {
					margin-left: 8.33333%;
				}

				.row > .col-2-small {
					width: 16.66667%;
				}

				.row > .off-2-small {
					margin-left: 16.66667%;
				}

				.row > .col-3-small {
					width: 25%;
				}

				.row > .off-3-small {
					margin-left: 25%;
				}

				.row > .col-4-small {
					width: 33.33333%;
				}

				.row > .off-4-small {
					margin-left: 33.33333%;
				}

				.row > .col-5-small {
					width: 41.66667%;
				}

				.row > .off-5-small {
					margin-left: 41.66667%;
				}

				.row > .col-6-small {
					width: 50%;
				}

				.row > .off-6-small {
					margin-left: 50%;
				}

				.row > .col-7-small {
					width: 58.33333%;
				}

				.row > .off-7-small {
					margin-left: 58.33333%;
				}

				.row > .col-8-small {
					width: 66.66667%;
				}

				.row > .off-8-small {
					margin-left: 66.66667%;
				}

				.row > .col-9-small {
					width: 75%;
				}

				.row > .off-9-small {
					margin-left: 75%;
				}

				.row > .col-10-small {
					width: 83.33333%;
				}

				.row > .off-10-small {
					margin-left: 83.33333%;
				}

				.row > .col-11-small {
					width: 91.66667%;
				}

				.row > .off-11-small {
					margin-left: 91.66667%;
				}

				.row > .col-12-small {
					width: 100%;
				}

				.row > .off-12-small {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

		@media screen and (max-width: 480px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xsmall {
					order: -1;
				}

				.row > .col-1-xsmall {
					width: 8.33333%;
				}

				.row > .off-1-xsmall {
					margin-left: 8.33333%;
				}

				.row > .col-2-xsmall {
					width: 16.66667%;
				}

				.row > .off-2-xsmall {
					margin-left: 16.66667%;
				}

				.row > .col-3-xsmall {
					width: 25%;
				}

				.row > .off-3-xsmall {
					margin-left: 25%;
				}

				.row > .col-4-xsmall {
					width: 33.33333%;
				}

				.row > .off-4-xsmall {
					margin-left: 33.33333%;
				}

				.row > .col-5-xsmall {
					width: 41.66667%;
				}

				.row > .off-5-xsmall {
					margin-left: 41.66667%;
				}

				.row > .col-6-xsmall {
					width: 50%;
				}

				.row > .off-6-xsmall {
					margin-left: 50%;
				}

				.row > .col-7-xsmall {
					width: 58.33333%;
				}

				.row > .off-7-xsmall {
					margin-left: 58.33333%;
				}

				.row > .col-8-xsmall {
					width: 66.66667%;
				}

				.row > .off-8-xsmall {
					margin-left: 66.66667%;
				}

				.row > .col-9-xsmall {
					width: 75%;
				}

				.row > .off-9-xsmall {
					margin-left: 75%;
				}

				.row > .col-10-xsmall {
					width: 83.33333%;
				}

				.row > .off-10-xsmall {
					margin-left: 83.33333%;
				}

				.row > .col-11-xsmall {
					width: 91.66667%;
				}

				.row > .off-11-xsmall {
					margin-left: 91.66667%;
				}

				.row > .col-12-xsmall {
					width: 100%;
				}

				.row > .off-12-xsmall {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

/* Container */

	.container {
		margin: 0 auto;
		max-width: calc(100% - 4.5em);
		width: 45em;
	}

		.container.xsmall {
			width: 11.25em;
		}

		.container.small {
			width: 22.5em;
		}

		.container.medium {
			width: 33.75em;
		}

		.container.large {
			width: 56.25em;
		}

		.container.xlarge {
			width: 67.5em;
		}

		.container.max {
			width: 100%;
		}

		@media screen and (max-width: 1024px) {

			.container {
				width: 100% !important;
			}

		}

		@media screen and (max-width: 480px) {

			.container {
				max-width: calc(100% - 3.375em);
			}

		}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header p {
		color: #aaa;
		position: relative;
		margin: 0 0 1.6875em 0;
	}

	header h2 + p {
		font-size: 1.25em;
		margin-top: -0.5em;
		line-height: 1.5em;
	}

	header h3 + p {
		font-size: 1.1em;
		margin-top: -0.35em;
		line-height: 1.5em;
	}

	header h4 + p,
	header h5 + p,
	header h6 + p {
		font-size: 0.9em;
		margin-top: -0.25em;
		line-height: 1.5em;
	}

	header.major h2 {
		color: #D6BD98;
		font-size: 3.5em;
	}

		header.major h2 + p {
			color: #777;
			font-size: 1.75em;
			font-weight: 700;
			margin-top: -0.75em;
		}

/* Form */

	form {
		margin: 0 0 2.25em 0;
	}

	label {
		color: #777;
		display: block;
		font-size: 0.9em;
		font-weight: 700;
		margin: 0 0 1.125em 0;
	}

	input::-moz-focus-inner {
		border: 0;
		padding: 0;
	}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select,
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		border-radius: 5px;
		border: none;
		border: solid 2px #e4e4e4;
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 1em;
		text-decoration: none;
		width: 100%;
	}

		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		select:focus,
		textarea:focus {
			border-color: #D6BD98;
		}

	select {
		background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' preserveAspectRatio='none' viewBox='0 0 40 40'%3E%3Cpath d='M9.4,12.3l10.4,10.4l10.4-10.4c0.2-0.2,0.5-0.4,0.9-0.4c0.3,0,0.6,0.1,0.9,0.4l3.3,3.3c0.2,0.2,0.4,0.5,0.4,0.9 c0,0.4-0.1,0.6-0.4,0.9L20.7,31.9c-0.2,0.2-0.5,0.4-0.9,0.4c-0.3,0-0.6-0.1-0.9-0.4L4.3,17.3c-0.2-0.2-0.4-0.5-0.4-0.9 c0-0.4,0.1-0.6,0.4-0.9l3.3-3.3c0.2-0.2,0.5-0.4,0.9-0.4S9.1,12.1,9.4,12.3z' fill='%23e4e4e4' /%3E%3C/svg%3E");
		background-size: 1.25em;
		background-repeat: no-repeat;
		background-position: calc(100% - 1em) center;
		height: 2.75em;
		padding-right: 2.75em;
		text-overflow: ellipsis;
	}

		select option {
			color: #777;
			background: #fff;
		}

		select:focus::-ms-value {
			background-color: transparent;
		}

		select::-ms-expand {
			display: none;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 2.75em;
	}

	textarea {
		padding: 0.75em 1em;
	}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2em;
		opacity: 0;
		width: 1em;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			color: #888;
			cursor: pointer;
			display: inline-block;
			font-size: 1em;
			font-weight: 400;
			padding-left: 2.4em;
			padding-right: 0.75em;
			position: relative;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				background: #fafafa;
				border-radius: 5px;
				border: solid 2px #e4e4e4;
				content: '';
				display: inline-block;
				font-size: 0.8em;
				height: 2.0625em;
				left: 0;
				line-height: 2.0625em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.0625em;
			}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			background: #989898;
			border-color: #989898;
			color: #1A3636;
			content: '\\f00c';
		}

		input[type="checkbox"]:focus + label:before,
		input[type="radio"]:focus + label:before {
			border-color: #D6BD98;
		}

	input[type="checkbox"] + label:before {
		border-radius: 5px;
	}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	::-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

/* Box */

	.box {
		border-radius: 5px;
		border: solid 2px #e4e4e4;
		margin-bottom: 2.25em;
		padding: 1.5em;
	}

		.box > :last-child,
		.box > :last-child > :last-child,
		.box > :last-child > :last-child > :last-child {
			margin-bottom: 0;
		}

		.box.alt {
			border: 0;
			border-radius: 0;
			padding: 0;
		}

/* Icon */

	.icon {
		text-decoration: none;
		border-bottom: none;
		position: relative;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 400;
		}

		.icon > .label {
			display: none;
		}

		.icon:before {
			line-height: inherit;
		}

		.icon.solid:before {
			font-weight: 900;
		}

		.icon.brands:before {
			font-family: 'Font Awesome 5 Brands';
		}

/* Image */

	.image {
		border-radius: 5px;
		border: 0;
		display: inline-block;
		position: relative;
	}

		.image[data-position] img {
			-moz-object-fit: cover;
			-webkit-object-fit: cover;
			-ms-object-fit: cover;
			object-fit: cover;
			display: block;
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
		}

		.image[data-position="top left"] img {
			-moz-object-position: top left;
			-webkit-object-position: top left;
			-ms-object-position: top left;
			object-position: top left;
		}

		.image[data-position="top"] img {
			-moz-object-position: top;
			-webkit-object-position: top;
			-ms-object-position: top;
			object-position: top;
		}

		.image[data-position="top right"] img {
			-moz-object-position: top right;
			-webkit-object-position: top right;
			-ms-object-position: top right;
			object-position: top right;
		}

		.image[data-position="right"] img {
			-moz-object-position: right;
			-webkit-object-position: right;
			-ms-object-position: right;
			object-position: right;
		}

		.image[data-position="bottom right"] img {
			-moz-object-position: bottom right;
			-webkit-object-position: bottom right;
			-ms-object-position: bottom right;
			object-position: bottom right;
		}

		.image[data-position="bottom"] img {
			-moz-object-position: bottom;
			-webkit-object-position: bottom;
			-ms-object-position: bottom;
			object-position: bottom;
		}

		.image[data-position="bottom left"] img {
			-moz-object-position: bottom left;
			-webkit-object-position: bottom left;
			-ms-object-position: bottom left;
			object-position: bottom left;
		}

		.image[data-position="left"] img {
			-moz-object-position: left;
			-webkit-object-position: left;
			-ms-object-position: left;
			object-position: left;
		}

		.image[data-position="center"] img {
			-moz-object-position: center;
			-webkit-object-position: center;
			-ms-object-position: center;
			object-position: center;
		}

		.image[data-position="25% 25%"] img {
			-moz-object-position: 25% 25%;
			-webkit-object-position: 25% 25%;
			-ms-object-position: 25% 25%;
			object-position: 25% 25%;
		}

		.image[data-position="75% 25%"] img {
			-moz-object-position: 75% 25%;
			-webkit-object-position: 75% 25%;
			-ms-object-position: 75% 25%;
			object-position: 75% 25%;
		}

		.image[data-position="75% 75%"] img {
			-moz-object-position: 75% 75%;
			-webkit-object-position: 75% 75%;
			-ms-object-position: 75% 75%;
			object-position: 75% 75%;
		}

		.image[data-position="25% 75%"] img {
			-moz-object-position: 25% 75%;
			-webkit-object-position: 25% 75%;
			-ms-object-position: 25% 75%;
			object-position: 25% 75%;
		}

		.image img {
			border-radius: 5px;
			display: block;
		}

		.image.left {
			float: left;
			margin: 0 2.5em 2em 0;
			top: 0.25em;
		}

		.image.right {
			float: right;
			margin: 0 0 2em 2.5em;
			top: 0.25em;
		}

		.image.fit {
			display: block;
			margin: 0 0 2.25em 0;
			width: 100%;
		}

			.image.fit img {
				display: block;
				width: 100%;
			}

		.image.avatar {
			border-radius: 100%;
			overflow: hidden;
		}

			.image.avatar img {
				border-radius: 100%;
				display: block;
				width: 100%;
			}

		.image.main {
			display: block;
			height: 20em;
			border-radius: 0;
		}

			.image.main img {
				border-radius: 0;
			}

/* List */

	ol {
		list-style: decimal;
		margin: 0 0 2.25em 0;
		padding-left: 1.25em;
	}

		ol li {
			padding-left: 0.25em;
		}

	ul {
		list-style: disc;
		margin: 0 0 2.25em 0;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
		}

		ul.alt {
			list-style: none;
			padding-left: 0;
		}

			ul.alt li {
				border-top: solid 2px #f4f4f4;
				padding: 0.5em 0;
			}

				ul.alt li:first-child {
					border-top: 0;
					padding-top: 0;
				}

	dl {
		margin: 0 0 2.25em 0;
	}

/* Actions */

	ul.actions {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		cursor: default;
		list-style: none;
		margin-left: -1.125em;
		padding-left: 0;
	}

		ul.actions li {
			padding: 0 0 0 1.125em;
			vertical-align: middle;
		}

		ul.actions.special {
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 100%;
			margin-left: 0;
		}

			ul.actions.special li:first-child {
				padding-left: 0;
			}

		ul.actions.stacked {
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			margin-left: 0;
		}

			ul.actions.stacked li {
				padding: 1.125em 0 0 0;
			}

				ul.actions.stacked li:first-child {
					padding-top: 0;
				}

		ul.actions.fit {
			width: calc(100% + 1.125em);
		}

			ul.actions.fit li {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				width: 100%;
			}

				ul.actions.fit li > * {
					width: 100%;
				}

			ul.actions.fit.stacked {
				width: 100%;
			}

		@media screen and (max-width: 480px) {

			ul.actions:not(.fixed) {
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
				margin-left: 0;
				width: 100% !important;
			}

				ul.actions:not(.fixed) li {
					-moz-flex-grow: 1;
					-webkit-flex-grow: 1;
					-ms-flex-grow: 1;
					flex-grow: 1;
					-moz-flex-shrink: 1;
					-webkit-flex-shrink: 1;
					-ms-flex-shrink: 1;
					flex-shrink: 1;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions:not(.fixed) li > * {
						width: 100%;
					}

					ul.actions:not(.fixed) li:first-child {
						padding-top: 0;
					}

					ul.actions:not(.fixed) li input[type="submit"],
					ul.actions:not(.fixed) li input[type="reset"],
					ul.actions:not(.fixed) li input[type="button"],
					ul.actions:not(.fixed) li button,
					ul.actions:not(.fixed) li .button {
						width: 100%;
					}

						ul.actions:not(.fixed) li input[type="submit"].icon:before,
						ul.actions:not(.fixed) li input[type="reset"].icon:before,
						ul.actions:not(.fixed) li input[type="button"].icon:before,
						ul.actions:not(.fixed) li button.icon:before,
						ul.actions:not(.fixed) li .button.icon:before {
							margin-left: -0.5rem;
						}

		}

/* Feature Icons */

	ul.feature-icons {
		list-style: none;
		padding-left: 0;
	}

		ul.feature-icons li {
			text-decoration: none;
			display: inline-block;
			margin: 0 0 1.6875em 0;
			padding: 0.35em 0 0 3.5em;
			position: relative;
			vertical-align: top;
			width: 48%;
		}

			ul.feature-icons li:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 400;
			}

			ul.feature-icons li:before {
				background: #D6BD98;
				border-radius: 100%;
				color: #ffffff;
				display: block;
				height: 2.5em;
				left: 0;
				line-height: 2.5em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.5em;
			}

/* Icons */

	ul.icons {
		cursor: default;
		list-style: none;
		padding-left: 0;
	}

		ul.icons li {
			display: inline-block;
			padding: 0 1em 0 0;
		}

			ul.icons li:last-child {
				padding-right: 0 !important;
			}

			ul.icons li .icon:before {
				font-size: 1.25em;
			}

/* Table */

	.table-wrapper {
		-webkit-overflow-scrolling: touch;
		overflow-x: auto;
	}

	table {
		margin: 0 0 2.25em 0;
		width: 100%;
	}

		table tbody tr {
			border: solid 2px #f4f4f4;
			border-left: 0;
			border-right: 0;
		}

			table tbody tr:nth-child(2n + 1) {
				background-color: #fafafa;
			}

		table td {
			padding: 0.75em 0.75em;
		}

		table th {
			color: #777;
			font-size: 0.9em;
			font-weight: 700;
			padding: 0 0.75em 0.75em 0.75em;
			text-align: left;
		}

		table thead {
			border-bottom: solid 4px #e4e4e4;
		}

		table tfoot {
			border-top: solid 4px #e4e4e4;
		}

		table.alt {
			border-collapse: separate;
		}

			table.alt tbody tr td {
				border: solid 2px #e4e4e4;
				border-left-width: 0;
				border-top-width: 0;
			}

				table.alt tbody tr td:first-child {
					border-left-width: 2px;
				}

			table.alt tbody tr:first-child td {
				border-top-width: 2px;
			}

			table.alt thead {
				border-bottom: 0;
			}

			table.alt tfoot {
				border-top: 0;
			}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		background-color: #989898;
		border-radius: 5px;
		border: 0;
		color: #ffffff !important;
		cursor: pointer;
		display: inline-block;
		font-weight: 700;
		height: 2.75em;
		line-height: 2.75em;
		padding: 0 1.5em;
		text-align: center;
		text-decoration: none;
		white-space: nowrap;
	}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		.button:hover {
			background-color: #a5a5a5;
			color: #ffffff !important;
		}

		input[type="submit"]:active,
		input[type="reset"]:active,
		input[type="button"]:active,
		.button:active {
			background-color: #8b8b8b;
		}

		input[type="submit"].icon,
		input[type="reset"].icon,
		input[type="button"].icon,
		.button.icon {
			padding-left: 1.35em;
		}

			input[type="submit"].icon:before,
			input[type="reset"].icon:before,
			input[type="button"].icon:before,
			.button.icon:before {
				margin-right: 0.5em;
			}

		input[type="submit"].fit,
		input[type="reset"].fit,
		input[type="button"].fit,
		.button.fit {
			width: 100%;
		}

		input[type="submit"].small,
		input[type="reset"].small,
		input[type="button"].small,
		.button.small {
			font-size: 0.8em;
		}

		input[type="submit"].large,
		input[type="reset"].large,
		input[type="button"].large,
		.button.large {
			font-size: 1.35em;
		}

		input[type="submit"].alt,
		input[type="reset"].alt,
		input[type="button"].alt,
		.button.alt {
			background-color: transparent;
			box-shadow: inset 0 0 0 2px #e4e4e4;
			color: #777 !important;
		}

			input[type="submit"].alt:hover,
			input[type="reset"].alt:hover,
			input[type="button"].alt:hover,
			.button.alt:hover {
				background-color: #f4f4f4;
				color: #777 !important;
			}

			input[type="submit"].alt:active,
			input[type="reset"].alt:active,
			input[type="button"].alt:active,
			.button.alt:active {
				background-color: #eaeaea;
			}

			input[type="submit"].alt.icon:before,
			input[type="reset"].alt.icon:before,
			input[type="button"].alt.icon:before,
			.button.alt.icon:before {
				color: #aaa;
			}

		input[type="submit"].primary,
		input[type="reset"].primary,
		input[type="button"].primary,
		.button.primary {
			background-color: #D6BD98;
			color: #ffffff !important;
		}

			input[type="submit"].primary:hover,
			input[type="reset"].primary:hover,
			input[type="button"].primary:hover,
			.button.primary:hover {
				background-color: #5ed0b1;
			}

			input[type="submit"].primary:active,
			input[type="reset"].primary:active,
			input[type="button"].primary:active,
			.button.primary:active {
				background-color: #39c29d;
			}

		input[type="submit"].disabled, input[type="submit"]:disabled,
		input[type="reset"].disabled,
		input[type="reset"]:disabled,
		input[type="button"].disabled,
		input[type="button"]:disabled,
		.button.disabled,
		.button:disabled {
			background-color: #888 !important;
			box-shadow: inset 0 -0.15em 0 0 rgba(0, 0, 0, 0.15);
			color: #fff !important;
			cursor: default;
			opacity: 0.25;
		}

/* Features */

	.features article {
		border-top: solid 3px #f4f4f4;
		margin-bottom: 2.25em;
		padding-top: 2.25em;
	}

		.features article:first-child {
			border-top: 0;
			padding-top: 0;
		}

		.features article .image {
			display: inline-block;
			padding-right: 2.5em;
			vertical-align: middle;
			width: 48%;
		}

			.features article .image img {
				display: block;
				width: 100%;
			}

		.features article .inner {
			display: inline-block;
			vertical-align: middle;
			width: 50%;
		}

			.features article .inner > :last-child {
				margin-bottom: 0;
			}

/* Header */

	#header {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: column;
		-webkit-flex-direction: column;
		-ms-flex-direction: column;
		flex-direction: column;
		-moz-justify-content: space-between;
		-webkit-justify-content: space-between;
		-ms-justify-content: space-between;
		justify-content: space-between;
		background: #D6BD98;
		color: #d2f2e9;
		height: 100%;
		overflow-y: auto;
		position: fixed;
		text-align: center;
		top: 0;
		width: 23em;
		right: 0;
	}

		#header h1, #header h2, #header h3, #header h4, #header h5, #header h6 {
			color: #ffffff;
		}

			#header h1 a, #header h2 a, #header h3 a, #header h4 a, #header h5 a, #header h6 a {
				color: #ffffff;
			}

		#header header p {
			color: #1A3636;
		}

		#header a {
			color: #d2f2e9;
		}

			#header a:hover {
				color: #ffffff !important;
			}

		#header > header {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			padding: 3em;
		}

			#header > header .avatar {
				display: block;
				margin: 0 auto 2.25em auto;
				width: 8em;
			}

			#header > header h1 {
				font-size: 1.75em;
				margin: 0;
			}

			#header > header p {
				color: #d2f2e9;
				font-style: italic;
				margin: 1em 0 0 0;
			}

		#header > footer {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			bottom: 0;
			left: 0;
			padding: 2em;
			width: 100%;
		}

			#header > footer .icons {
				margin: 0;
			}

				#header > footer .icons li a {
					color: #1A3636;
				}

		#header > nav {
			-moz-flex-grow: 1;
			-webkit-flex-grow: 1;
			-ms-flex-grow: 1;
			flex-grow: 1;
		}

			#header > nav ul {
				list-style: none;
				margin: 0;
				padding: 0;
			}

				#header > nav ul li {
					border-top: solid 2px #5ccfb1;
					display: block;
					padding: 0;
				}

					#header > nav ul li a {
						-moz-transition: none;
						-webkit-transition: none;
						-ms-transition: none;
						transition: none;
						border: 0;
						color: #ffffff !important;
						display: block;
						padding: 0.85em 0;
						text-decoration: none;
					}

						#header > nav ul li a.active {
							background: #fff;
							color: #D6BD98 !important;
						}

					#header > nav ul li:first-child {
						border-top: 0;
					}

/* Wrapper */

	#wrapper {
		background: #fff;
		padding-right: 23em;
	}

/* Main */

	#main > section {
		border-top: solid 6px #f4f4f4;
	}

		#main > section > .container {
			padding: 6em 0 4em 0;
		}

		#main > section:first-child {
			border-top: 0;
		}

/* Footer */

	#footer {
		background: #fafafa;
		border-top: 0;
		color: #c0c0c0;
		overflow: hidden;
		padding: 4em 0 2em 0;
	}

		#footer .copyright {
			line-height: 1em;
			list-style: none;
			padding: 0;
		}

			#footer .copyright li {
				border-left: solid 1px #d4d4d4;
				display: inline-block;
				font-size: 0.8em;
				margin-left: 1em;
				padding-left: 1em;
			}

				#footer .copyright li:first-child {
					border-left: 0;
					margin-left: 0;
					padding-left: 0;
				}

				#footer .copyright li a {
					color: inherit;
				}

/* XLarge */

	@media screen and (max-width: 1680px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 13pt;
			}

		/* Header */

			#header {
				width: 21em;
			}

				#header > header {
					padding: 2em;
				}

				#header > footer {
					padding: 1.5em;
				}

		/* Wrapper */

			#wrapper {
				padding-right: 21em;
			}

		/* Main */

			#main > section > .container {
				padding: 4em 0 2em 0;
			}

	}

/* Large */

	@media screen and (max-width: 1280px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 11pt;
			}

		/* Header */

			#header {
				width: 20em;
			}

		/* Wrapper */

			#wrapper {
				padding-right: 20em;
			}

	}

/* Medium */

	#titleBar {
		display: none;
	}

	@media screen and (max-width: 1024px) {

		/* Basic */

			html, body {
				overflow-x: hidden;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* Image */

			.image.left, .image.right {
				max-width: 40%;
			}

				.image.left img, .image.right img {
					width: 100%;
				}

			.image.main {
				height: 20em;
			}

		/* Header */

			#header {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 100%;
				overflow-y: auto;
				position: fixed;
				top: 0;
				width: 23em;
				z-index: 10002;
				-moz-transform: translateX(23em);
				-webkit-transform: translateX(23em);
				-ms-transform: translateX(23em);
				transform: translateX(23em);
				right: 0;
			}

				#header > footer {
					bottom: auto;
					left: auto;
					margin: 0.5em 0 0 0;
					position: relative;
					right: auto;
					top: auto;
				}

		/* Wrapper */

			#wrapper {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				padding: 44px 0 1px 0;
			}

		/* Header Panel */

			#titleBar {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 44px;
				left: 0;
				position: fixed;
				top: 0;
				width: 100%;
				z-index: 10001;
				background: #222;
				color: #fff;
				min-width: 320px;
			}

				#titleBar .title {
					color: #fff;
					display: block;
					font-weight: 700;
					height: 44px;
					line-height: 44px;
					padding: 0 1em;
					width: 100%;
					text-align: left;
				}

					#titleBar .title a {
						border: 0;
						text-decoration: none;
					}

				#titleBar .toggle {
					text-decoration: none;
					height: 4em;
					position: absolute;
					top: 0;
					width: 6em;
					border: 0;
					outline: 0;
					right: 0;
				}

					#titleBar .toggle:before {
						-moz-osx-font-smoothing: grayscale;
						-webkit-font-smoothing: antialiased;
						display: inline-block;
						font-style: normal;
						font-variant: normal;
						text-rendering: auto;
						line-height: 1;
						text-transform: none !important;
						font-family: 'Font Awesome 5 Free';
						font-weight: 900;
					}

					#titleBar .toggle:before {
						background: #D6BD98;
						color: #ffffff;
						content: '\\f0c9';
						display: block;
						font-size: 18px;
						height: 44px;
						line-height: 44px;
						position: absolute;
						text-align: center;
						top: 0;
						width: 64px;
						right: 0;
					}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-23em);
				-webkit-transform: translateX(-23em);
				-ms-transform: translateX(-23em);
				transform: translateX(-23em);
			}

			body.header-visible #header {
				-moz-transform: translateX(0);
				-webkit-transform: translateX(0);
				-ms-transform: translateX(0);
				transform: translateX(0);
			}

	}

/* Small */

	@media screen and (max-width: 736px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 12pt;
			}

			h1 br, h2 br, h3 br, h4 br, h5 br, h6 br {
				display: none;
			}

			h2 {
				font-size: 1.75em;
			}

			h3 {
				font-size: 1.5em;
			}

			h4 {
				font-size: 1em;
			}

		/* Image */

			.image.left {
				margin: 0 1.5em 1em 0;
			}

			.image.right {
				margin: 0 0 1em 1.5em;
			}

			.image.main {
				height: 12em;
			}

		/* Section/Article */

			header br {
				display: none;
			}

			header.major h2 {
				font-size: 2.5em;
			}

				header.major h2 + p {
					font-size: 1.5em;
				}

		/* Features */

			.features article .image {
				display: block;
				margin: 0 0 2.25em 0;
				padding-right: 0;
				width: 100%;
			}

			.features article .inner {
				display: block;
				width: 100%;
			}

		/* Header */

			#header {
				width: 17em;
				-moz-transform: translateX(17em);
				-webkit-transform: translateX(17em);
				-ms-transform: translateX(17em);
				transform: translateX(17em);
				right: 0;
			}

				#header > header {
					padding: 2em;
				}

					#header > header .avatar {
						margin: 0 auto 1.6875em auto;
						width: 6em;
					}

					#header > header h1 {
						font-size: 1.5em;
					}

					#header > header p {
						margin: 1em 0 0 0;
					}

				#header > footer {
					padding: 1.5em;
				}

		/* Main */

			#main > section > .container {
				padding: 2em 0 0 0;
			}

		/* Footer */

			#footer {
				text-align: center;
			}

				#footer .copyright li {
					border-left: 0;
					display: block;
					line-height: 1.75em;
					margin: 0.75em 0 0 0;
					padding-left: 0;
				}

					#footer .copyright li:first-child {
						margin-top: 0;
					}

		/* Header Panel */

			#titleBar .toggle {
				height: 4em;
				width: 6em;
			}

				#titleBar .toggle:before {
					font-size: 14px;
					width: 44px;
				}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-17em);
				-webkit-transform: translateX(-17em);
				-ms-transform: translateX(-17em);
				transform: translateX(-17em);
			}

	}

/* XSmall */

	@media screen and (max-width: 480px) {

		/* Basic */

			html, body {
				min-width: 320px;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* List */

			ul.actions {
				margin: 0 0 2.25em 0;
			}

				ul.actions li {
					display: block;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions li:first-child {
						padding-top: 0;
					}

					ul.actions li > * {
						width: 100%;
						margin: 0 !important;
					}

						ul.actions li > *.icon:before {
							margin-left: -2em;
						}

				ul.actions.small li {
					padding: 0.5625em 0 0 0;
				}

					ul.actions.small li:first-child {
						padding-top: 0;
					}

			ul.feature-icons li {
				display: block;
				width: 100%;
			}

		/* Button */

			input[type="submit"],
			input[type="reset"],
			input[type="button"],
			.button {
				padding: 0;
			}

	}
	/* Define the colors */
:root {
    --color-primary: #1A3636;
    --color-secondary: #40534C;
    --color-tertiary: #40534C;
    --color-quaternary: #D6BD98;
}

/* Example usage of the colors */
body {
    background-color: var(--color-primary);
    color: var(--color-quaternary);
}

.header {
    background-color: var(--color-secondary);
    color: var(--color-primary);
}

.button {
    background-color: var(--color-tertiary);
    color: var(--color-primary);
}

.footer {
    background-color: var(--color-quaternary);
    color: var(--color-secondary);
}

#main {
    background-color: #1A3636;
}
#header {
    background-color: #40534C;
}
#header {
    background-color: #40534C;
}
#footer , h1, h2, h3, h4{
	color: #D6BD98;
}
#wrapper {
	   border-top: solid 6px #1A3636;
}
header.major h2 {
    color: #D6BD98;
    font-size: 3.5em;
}
header.major h2 + p {
    color: #677D6A;
    /* font-size: 1.75em; */
    /* font-weight: 700; */
    /* margin-top: -0.75em; */
}
#header > footer .icons li a {
    color: #d6bd98;
}
""", "elegant":"""@import url("fontawesome-all.min.css");
@import url("https://fonts.googleapis.com/css?family=Lato:400,400italic,700,700italic|Source+Code+Pro:400");
html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #fff;
	}

		body.is-preload *, body.is-preload *:before, body.is-preload *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

	body, input, select, textarea {
		color: #888;
		font-family: "Lato", sans-serif;
		font-size: 16pt;
		font-weight: 400;
		line-height: 1.75em;
	}

	a {
		-moz-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-webkit-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-ms-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		border-bottom: solid 1px #e4e4e4;
		color: inherit;
		text-decoration: none;
	}

		a:hover {
			border-bottom-color: transparent;
			color: #373A40 !important;
		}

	strong, b {
		color: #777;
		font-weight: 700;
	}

	em, i {
		font-style: italic;
	}

	p {
		margin: 0 0 2.25em 0;
	}

	h1, h2, h3, h4, h5, h6 {
		color: #777;
		font-weight: 700;
		line-height: 1em;
		margin: 0 0 0.5625em 0;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			border: 0;
			color: inherit;
			text-decoration: none;
		}

	h2 {
		font-size: 2em;
		line-height: 1.5em;
	}

	h3 {
		font-size: 1.75em;
		line-height: 1.5em;
	}

	h4 {
		font-size: 1.25em;
		line-height: 1.5em;
	}

	h5 {
		font-size: 0.9em;
		line-height: 1.5em;
	}

	h6 {
		font-size: 0.7em;
		line-height: 1.5em;
	}

	sub {
		font-size: 0.8em;
		position: relative;
		top: 0.5em;
	}

	sup {
		font-size: 0.8em;
		position: relative;
		top: -0.5em;
	}

	hr {
		border: 0;
		border-bottom: solid 2px #f4f4f4;
		margin: 2.25em 0;
	}

		hr.major {
			margin: 3.375em 0;
		}

	blockquote {
		border-left: solid 8px #e4e4e4;
		font-style: italic;
		margin: 0 0 2.25em 0;
		padding: 0.5em 0 0.5em 2em;
	}

	code {
		background: #555;
		border-radius: 5px;
		color: #fff;
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0.25em;
		padding: 0.25em 0.65em;
	}

	pre {
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0 2.25em 0;
	}

		pre code {
			-webkit-overflow-scrolling: touch;
			display: block;
			line-height: 1.5em;
			overflow-x: auto;
			padding: 1em 1.5em;
		}

	.align-left {
		text-align: left;
	}

	.align-center {
		text-align: center;
	}

	.align-right {
		text-align: right;
	}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0;
			margin-left: 0em;
		}

			.row.gtr-0 > * {
				padding: 0 0 0 0em;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0em;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0em;
				}

		.row.gtr-25 {
			margin-top: 0;
			margin-left: -0.5em;
		}

			.row.gtr-25 > * {
				padding: 0 0 0 0.5em;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -0.5em;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 0.5em;
				}

		.row.gtr-50 {
			margin-top: 0;
			margin-left: -1em;
		}

			.row.gtr-50 > * {
				padding: 0 0 0 1em;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -1em;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 1em;
				}

		.row {
			margin-top: 0;
			margin-left: -2em;
		}

			.row > * {
				padding: 0 0 0 2em;
			}

			.row.gtr-uniform {
				margin-top: -2em;
			}

				.row.gtr-uniform > * {
					padding-top: 2em;
				}

		.row.gtr-150 {
			margin-top: 0;
			margin-left: -3em;
		}

			.row.gtr-150 > * {
				padding: 0 0 0 3em;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -3em;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 3em;
				}

		.row.gtr-200 {
			margin-top: 0;
			margin-left: -4em;
		}

			.row.gtr-200 > * {
				padding: 0 0 0 4em;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -4em;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 4em;
				}

		@media screen and (max-width: 1680px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xlarge {
					order: -1;
				}

				.row > .col-1-xlarge {
					width: 8.33333%;
				}

				.row > .off-1-xlarge {
					margin-left: 8.33333%;
				}

				.row > .col-2-xlarge {
					width: 16.66667%;
				}

				.row > .off-2-xlarge {
					margin-left: 16.66667%;
				}

				.row > .col-3-xlarge {
					width: 25%;
				}

				.row > .off-3-xlarge {
					margin-left: 25%;
				}

				.row > .col-4-xlarge {
					width: 33.33333%;
				}

				.row > .off-4-xlarge {
					margin-left: 33.33333%;
				}

				.row > .col-5-xlarge {
					width: 41.66667%;
				}

				.row > .off-5-xlarge {
					margin-left: 41.66667%;
				}

				.row > .col-6-xlarge {
					width: 50%;
				}

				.row > .off-6-xlarge {
					margin-left: 50%;
				}

				.row > .col-7-xlarge {
					width: 58.33333%;
				}

				.row > .off-7-xlarge {
					margin-left: 58.33333%;
				}

				.row > .col-8-xlarge {
					width: 66.66667%;
				}

				.row > .off-8-xlarge {
					margin-left: 66.66667%;
				}

				.row > .col-9-xlarge {
					width: 75%;
				}

				.row > .off-9-xlarge {
					margin-left: 75%;
				}

				.row > .col-10-xlarge {
					width: 83.33333%;
				}

				.row > .off-10-xlarge {
					margin-left: 83.33333%;
				}

				.row > .col-11-xlarge {
					width: 91.66667%;
				}

				.row > .off-11-xlarge {
					margin-left: 91.66667%;
				}

				.row > .col-12-xlarge {
					width: 100%;
				}

				.row > .off-12-xlarge {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -1em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 1em;
						}

				.row {
					margin-top: 0;
					margin-left: -2em;
				}

					.row > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-uniform > * {
							padding-top: 2em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 3em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -4em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 4em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -4em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 4em;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-large {
					order: -1;
				}

				.row > .col-1-large {
					width: 8.33333%;
				}

				.row > .off-1-large {
					margin-left: 8.33333%;
				}

				.row > .col-2-large {
					width: 16.66667%;
				}

				.row > .off-2-large {
					margin-left: 16.66667%;
				}

				.row > .col-3-large {
					width: 25%;
				}

				.row > .off-3-large {
					margin-left: 25%;
				}

				.row > .col-4-large {
					width: 33.33333%;
				}

				.row > .off-4-large {
					margin-left: 33.33333%;
				}

				.row > .col-5-large {
					width: 41.66667%;
				}

				.row > .off-5-large {
					margin-left: 41.66667%;
				}

				.row > .col-6-large {
					width: 50%;
				}

				.row > .off-6-large {
					margin-left: 50%;
				}

				.row > .col-7-large {
					width: 58.33333%;
				}

				.row > .off-7-large {
					margin-left: 58.33333%;
				}

				.row > .col-8-large {
					width: 66.66667%;
				}

				.row > .off-8-large {
					margin-left: 66.66667%;
				}

				.row > .col-9-large {
					width: 75%;
				}

				.row > .off-9-large {
					margin-left: 75%;
				}

				.row > .col-10-large {
					width: 83.33333%;
				}

				.row > .off-10-large {
					margin-left: 83.33333%;
				}

				.row > .col-11-large {
					width: 91.66667%;
				}

				.row > .off-11-large {
					margin-left: 91.66667%;
				}

				.row > .col-12-large {
					width: 100%;
				}

				.row > .off-12-large {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 1024px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-medium {
					order: -1;
				}

				.row > .col-1-medium {
					width: 8.33333%;
				}

				.row > .off-1-medium {
					margin-left: 8.33333%;
				}

				.row > .col-2-medium {
					width: 16.66667%;
				}

				.row > .off-2-medium {
					margin-left: 16.66667%;
				}

				.row > .col-3-medium {
					width: 25%;
				}

				.row > .off-3-medium {
					margin-left: 25%;
				}

				.row > .col-4-medium {
					width: 33.33333%;
				}

				.row > .off-4-medium {
					margin-left: 33.33333%;
				}

				.row > .col-5-medium {
					width: 41.66667%;
				}

				.row > .off-5-medium {
					margin-left: 41.66667%;
				}

				.row > .col-6-medium {
					width: 50%;
				}

				.row > .off-6-medium {
					margin-left: 50%;
				}

				.row > .col-7-medium {
					width: 58.33333%;
				}

				.row > .off-7-medium {
					margin-left: 58.33333%;
				}

				.row > .col-8-medium {
					width: 66.66667%;
				}

				.row > .off-8-medium {
					margin-left: 66.66667%;
				}

				.row > .col-9-medium {
					width: 75%;
				}

				.row > .off-9-medium {
					margin-left: 75%;
				}

				.row > .col-10-medium {
					width: 83.33333%;
				}

				.row > .off-10-medium {
					margin-left: 83.33333%;
				}

				.row > .col-11-medium {
					width: 91.66667%;
				}

				.row > .off-11-medium {
					margin-left: 91.66667%;
				}

				.row > .col-12-medium {
					width: 100%;
				}

				.row > .off-12-medium {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-small {
					order: -1;
				}

				.row > .col-1-small {
					width: 8.33333%;
				}

				.row > .off-1-small {
					margin-left: 8.33333%;
				}

				.row > .col-2-small {
					width: 16.66667%;
				}

				.row > .off-2-small {
					margin-left: 16.66667%;
				}

				.row > .col-3-small {
					width: 25%;
				}

				.row > .off-3-small {
					margin-left: 25%;
				}

				.row > .col-4-small {
					width: 33.33333%;
				}

				.row > .off-4-small {
					margin-left: 33.33333%;
				}

				.row > .col-5-small {
					width: 41.66667%;
				}

				.row > .off-5-small {
					margin-left: 41.66667%;
				}

				.row > .col-6-small {
					width: 50%;
				}

				.row > .off-6-small {
					margin-left: 50%;
				}

				.row > .col-7-small {
					width: 58.33333%;
				}

				.row > .off-7-small {
					margin-left: 58.33333%;
				}

				.row > .col-8-small {
					width: 66.66667%;
				}

				.row > .off-8-small {
					margin-left: 66.66667%;
				}

				.row > .col-9-small {
					width: 75%;
				}

				.row > .off-9-small {
					margin-left: 75%;
				}

				.row > .col-10-small {
					width: 83.33333%;
				}

				.row > .off-10-small {
					margin-left: 83.33333%;
				}

				.row > .col-11-small {
					width: 91.66667%;
				}

				.row > .off-11-small {
					margin-left: 91.66667%;
				}

				.row > .col-12-small {
					width: 100%;
				}

				.row > .off-12-small {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

		@media screen and (max-width: 480px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xsmall {
					order: -1;
				}

				.row > .col-1-xsmall {
					width: 8.33333%;
				}

				.row > .off-1-xsmall {
					margin-left: 8.33333%;
				}

				.row > .col-2-xsmall {
					width: 16.66667%;
				}

				.row > .off-2-xsmall {
					margin-left: 16.66667%;
				}

				.row > .col-3-xsmall {
					width: 25%;
				}

				.row > .off-3-xsmall {
					margin-left: 25%;
				}

				.row > .col-4-xsmall {
					width: 33.33333%;
				}

				.row > .off-4-xsmall {
					margin-left: 33.33333%;
				}

				.row > .col-5-xsmall {
					width: 41.66667%;
				}

				.row > .off-5-xsmall {
					margin-left: 41.66667%;
				}

				.row > .col-6-xsmall {
					width: 50%;
				}

				.row > .off-6-xsmall {
					margin-left: 50%;
				}

				.row > .col-7-xsmall {
					width: 58.33333%;
				}

				.row > .off-7-xsmall {
					margin-left: 58.33333%;
				}

				.row > .col-8-xsmall {
					width: 66.66667%;
				}

				.row > .off-8-xsmall {
					margin-left: 66.66667%;
				}

				.row > .col-9-xsmall {
					width: 75%;
				}

				.row > .off-9-xsmall {
					margin-left: 75%;
				}

				.row > .col-10-xsmall {
					width: 83.33333%;
				}

				.row > .off-10-xsmall {
					margin-left: 83.33333%;
				}

				.row > .col-11-xsmall {
					width: 91.66667%;
				}

				.row > .off-11-xsmall {
					margin-left: 91.66667%;
				}

				.row > .col-12-xsmall {
					width: 100%;
				}

				.row > .off-12-xsmall {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

/* Container */

	.container {
		margin: 0 auto;
		max-width: calc(100% - 4.5em);
		width: 45em;
	}

		.container.xsmall {
			width: 11.25em;
		}

		.container.small {
			width: 22.5em;
		}

		.container.medium {
			width: 33.75em;
		}

		.container.large {
			width: 56.25em;
		}

		.container.xlarge {
			width: 67.5em;
		}

		.container.max {
			width: 100%;
		}

		@media screen and (max-width: 1024px) {

			.container {
				width: 100% !important;
			}

		}

		@media screen and (max-width: 480px) {

			.container {
				max-width: calc(100% - 3.375em);
			}

		}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header p {
		color: #aaa;
		position: relative;
		margin: 0 0 1.6875em 0;
	}

	header h2 + p {
		font-size: 1.25em;
		margin-top: -0.5em;
		line-height: 1.5em;
	}

	header h3 + p {
		font-size: 1.1em;
		margin-top: -0.35em;
		line-height: 1.5em;
	}

	header h4 + p,
	header h5 + p,
	header h6 + p {
		font-size: 0.9em;
		margin-top: -0.25em;
		line-height: 1.5em;
	}

	header.major h2 {
		color: #373A40;
		font-size: 3.5em;
	}

		header.major h2 + p {
			color: #777;
			font-size: 1.75em;
			font-weight: 700;
			margin-top: -0.75em;
		}

/* Form */

	form {
		margin: 0 0 2.25em 0;
	}

	label {
		color: #777;
		display: block;
		font-size: 0.9em;
		font-weight: 700;
		margin: 0 0 1.125em 0;
	}

	input::-moz-focus-inner {
		border: 0;
		padding: 0;
	}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select,
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		border-radius: 5px;
		border: none;
		border: solid 2px #e4e4e4;
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 1em;
		text-decoration: none;
		width: 100%;
	}

		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		select:focus,
		textarea:focus {
			border-color: #373A40;
		}

	select {
		background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' preserveAspectRatio='none' viewBox='0 0 40 40'%3E%3Cpath d='M9.4,12.3l10.4,10.4l10.4-10.4c0.2-0.2,0.5-0.4,0.9-0.4c0.3,0,0.6,0.1,0.9,0.4l3.3,3.3c0.2,0.2,0.4,0.5,0.4,0.9 c0,0.4-0.1,0.6-0.4,0.9L20.7,31.9c-0.2,0.2-0.5,0.4-0.9,0.4c-0.3,0-0.6-0.1-0.9-0.4L4.3,17.3c-0.2-0.2-0.4-0.5-0.4-0.9 c0-0.4,0.1-0.6,0.4-0.9l3.3-3.3c0.2-0.2,0.5-0.4,0.9-0.4S9.1,12.1,9.4,12.3z' fill='%23e4e4e4' /%3E%3C/svg%3E");
		background-size: 1.25em;
		background-repeat: no-repeat;
		background-position: calc(100% - 1em) center;
		height: 2.75em;
		padding-right: 2.75em;
		text-overflow: ellipsis;
	}

		select option {
			color: #777;
			background: #fff;
		}

		select:focus::-ms-value {
			background-color: transparent;
		}

		select::-ms-expand {
			display: none;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 2.75em;
	}

	textarea {
		padding: 0.75em 1em;
	}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2em;
		opacity: 0;
		width: 1em;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			color: #888;
			cursor: pointer;
			display: inline-block;
			font-size: 1em;
			font-weight: 400;
			padding-left: 2.4em;
			padding-right: 0.75em;
			position: relative;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				background: #fafafa;
				border-radius: 5px;
				border: solid 2px #e4e4e4;
				content: '';
				display: inline-block;
				font-size: 0.8em;
				height: 2.0625em;
				left: 0;
				line-height: 2.0625em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.0625em;
			}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			background: #989898;
			border-color: #989898;
			color: #EEEEEE;
			content: '\\f00c';
		}

		input[type="checkbox"]:focus + label:before,
		input[type="radio"]:focus + label:before {
			border-color: #373A40;
		}

	input[type="checkbox"] + label:before {
		border-radius: 5px;
	}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	::-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

/* Box */

	.box {
		border-radius: 5px;
		border: solid 2px #e4e4e4;
		margin-bottom: 2.25em;
		padding: 1.5em;
	}

		.box > :last-child,
		.box > :last-child > :last-child,
		.box > :last-child > :last-child > :last-child {
			margin-bottom: 0;
		}

		.box.alt {
			border: 0;
			border-radius: 0;
			padding: 0;
		}

/* Icon */

	.icon {
		text-decoration: none;
		border-bottom: none;
		position: relative;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 400;
		}

		.icon > .label {
			display: none;
		}

		.icon:before {
			line-height: inherit;
		}

		.icon.solid:before {
			font-weight: 900;
		}

		.icon.brands:before {
			font-family: 'Font Awesome 5 Brands';
		}

/* Image */

	.image {
		border-radius: 5px;
		border: 0;
		display: inline-block;
		position: relative;
	}

		.image[data-position] img {
			-moz-object-fit: cover;
			-webkit-object-fit: cover;
			-ms-object-fit: cover;
			object-fit: cover;
			display: block;
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
		}

		.image[data-position="top left"] img {
			-moz-object-position: top left;
			-webkit-object-position: top left;
			-ms-object-position: top left;
			object-position: top left;
		}

		.image[data-position="top"] img {
			-moz-object-position: top;
			-webkit-object-position: top;
			-ms-object-position: top;
			object-position: top;
		}

		.image[data-position="top right"] img {
			-moz-object-position: top right;
			-webkit-object-position: top right;
			-ms-object-position: top right;
			object-position: top right;
		}

		.image[data-position="right"] img {
			-moz-object-position: right;
			-webkit-object-position: right;
			-ms-object-position: right;
			object-position: right;
		}

		.image[data-position="bottom right"] img {
			-moz-object-position: bottom right;
			-webkit-object-position: bottom right;
			-ms-object-position: bottom right;
			object-position: bottom right;
		}

		.image[data-position="bottom"] img {
			-moz-object-position: bottom;
			-webkit-object-position: bottom;
			-ms-object-position: bottom;
			object-position: bottom;
		}

		.image[data-position="bottom left"] img {
			-moz-object-position: bottom left;
			-webkit-object-position: bottom left;
			-ms-object-position: bottom left;
			object-position: bottom left;
		}

		.image[data-position="left"] img {
			-moz-object-position: left;
			-webkit-object-position: left;
			-ms-object-position: left;
			object-position: left;
		}

		.image[data-position="center"] img {
			-moz-object-position: center;
			-webkit-object-position: center;
			-ms-object-position: center;
			object-position: center;
		}

		.image[data-position="25% 25%"] img {
			-moz-object-position: 25% 25%;
			-webkit-object-position: 25% 25%;
			-ms-object-position: 25% 25%;
			object-position: 25% 25%;
		}

		.image[data-position="75% 25%"] img {
			-moz-object-position: 75% 25%;
			-webkit-object-position: 75% 25%;
			-ms-object-position: 75% 25%;
			object-position: 75% 25%;
		}

		.image[data-position="75% 75%"] img {
			-moz-object-position: 75% 75%;
			-webkit-object-position: 75% 75%;
			-ms-object-position: 75% 75%;
			object-position: 75% 75%;
		}

		.image[data-position="25% 75%"] img {
			-moz-object-position: 25% 75%;
			-webkit-object-position: 25% 75%;
			-ms-object-position: 25% 75%;
			object-position: 25% 75%;
		}

		.image img {
			border-radius: 5px;
			display: block;
		}

		.image.left {
			float: left;
			margin: 0 2.5em 2em 0;
			top: 0.25em;
		}

		.image.right {
			float: right;
			margin: 0 0 2em 2.5em;
			top: 0.25em;
		}

		.image.fit {
			display: block;
			margin: 0 0 2.25em 0;
			width: 100%;
		}

			.image.fit img {
				display: block;
				width: 100%;
			}

		.image.avatar {
			border-radius: 100%;
			overflow: hidden;
		}

			.image.avatar img {
				border-radius: 100%;
				display: block;
				width: 100%;
			}

		.image.main {
			display: block;
			height: 20em;
			border-radius: 0;
		}

			.image.main img {
				border-radius: 0;
			}

/* List */

	ol {
		list-style: decimal;
		margin: 0 0 2.25em 0;
		padding-left: 1.25em;
	}

		ol li {
			padding-left: 0.25em;
		}

	ul {
		list-style: disc;
		margin: 0 0 2.25em 0;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
		}

		ul.alt {
			list-style: none;
			padding-left: 0;
		}

			ul.alt li {
				border-top: solid 2px #f4f4f4;
				padding: 0.5em 0;
			}

				ul.alt li:first-child {
					border-top: 0;
					padding-top: 0;
				}

	dl {
		margin: 0 0 2.25em 0;
	}

/* Actions */

	ul.actions {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		cursor: default;
		list-style: none;
		margin-left: -1.125em;
		padding-left: 0;
	}

		ul.actions li {
			padding: 0 0 0 1.125em;
			vertical-align: middle;
		}

		ul.actions.special {
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 100%;
			margin-left: 0;
		}

			ul.actions.special li:first-child {
				padding-left: 0;
			}

		ul.actions.stacked {
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			margin-left: 0;
		}

			ul.actions.stacked li {
				padding: 1.125em 0 0 0;
			}

				ul.actions.stacked li:first-child {
					padding-top: 0;
				}

		ul.actions.fit {
			width: calc(100% + 1.125em);
		}

			ul.actions.fit li {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				width: 100%;
			}

				ul.actions.fit li > * {
					width: 100%;
				}

			ul.actions.fit.stacked {
				width: 100%;
			}

		@media screen and (max-width: 480px) {

			ul.actions:not(.fixed) {
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
				margin-left: 0;
				width: 100% !important;
			}

				ul.actions:not(.fixed) li {
					-moz-flex-grow: 1;
					-webkit-flex-grow: 1;
					-ms-flex-grow: 1;
					flex-grow: 1;
					-moz-flex-shrink: 1;
					-webkit-flex-shrink: 1;
					-ms-flex-shrink: 1;
					flex-shrink: 1;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions:not(.fixed) li > * {
						width: 100%;
					}

					ul.actions:not(.fixed) li:first-child {
						padding-top: 0;
					}

					ul.actions:not(.fixed) li input[type="submit"],
					ul.actions:not(.fixed) li input[type="reset"],
					ul.actions:not(.fixed) li input[type="button"],
					ul.actions:not(.fixed) li button,
					ul.actions:not(.fixed) li .button {
						width: 100%;
					}

						ul.actions:not(.fixed) li input[type="submit"].icon:before,
						ul.actions:not(.fixed) li input[type="reset"].icon:before,
						ul.actions:not(.fixed) li input[type="button"].icon:before,
						ul.actions:not(.fixed) li button.icon:before,
						ul.actions:not(.fixed) li .button.icon:before {
							margin-left: -0.5rem;
						}

		}

/* Feature Icons */

	ul.feature-icons {
		list-style: none;
		padding-left: 0;
	}

		ul.feature-icons li {
			text-decoration: none;
			display: inline-block;
			margin: 0 0 1.6875em 0;
			padding: 0.35em 0 0 3.5em;
			position: relative;
			vertical-align: top;
			width: 48%;
		}

			ul.feature-icons li:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 400;
			}

			ul.feature-icons li:before {
				background: #373A40;
				border-radius: 100%;
				color: #ffffff;
				display: block;
				height: 2.5em;
				left: 0;
				line-height: 2.5em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.5em;
			}

/* Icons */

	ul.icons {
		cursor: default;
		list-style: none;
		padding-left: 0;
	}

		ul.icons li {
			display: inline-block;
			padding: 0 1em 0 0;
		}

			ul.icons li:last-child {
				padding-right: 0 !important;
			}

			ul.icons li .icon:before {
				font-size: 1.25em;
			}

/* Table */

	.table-wrapper {
		-webkit-overflow-scrolling: touch;
		overflow-x: auto;
	}

	table {
		margin: 0 0 2.25em 0;
		width: 100%;
	}

		table tbody tr {
			border: solid 2px #f4f4f4;
			border-left: 0;
			border-right: 0;
		}

			table tbody tr:nth-child(2n + 1) {
				background-color: #fafafa;
			}

		table td {
			padding: 0.75em 0.75em;
		}

		table th {
			color: #777;
			font-size: 0.9em;
			font-weight: 700;
			padding: 0 0.75em 0.75em 0.75em;
			text-align: left;
		}

		table thead {
			border-bottom: solid 4px #e4e4e4;
		}

		table tfoot {
			border-top: solid 4px #e4e4e4;
		}

		table.alt {
			border-collapse: separate;
		}

			table.alt tbody tr td {
				border: solid 2px #e4e4e4;
				border-left-width: 0;
				border-top-width: 0;
			}

				table.alt tbody tr td:first-child {
					border-left-width: 2px;
				}

			table.alt tbody tr:first-child td {
				border-top-width: 2px;
			}

			table.alt thead {
				border-bottom: 0;
			}

			table.alt tfoot {
				border-top: 0;
			}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		background-color: #989898;
		border-radius: 5px;
		border: 0;
		color: #ffffff !important;
		cursor: pointer;
		display: inline-block;
		font-weight: 700;
		height: 2.75em;
		line-height: 2.75em;
		padding: 0 1.5em;
		text-align: center;
		text-decoration: none;
		white-space: nowrap;
	}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		.button:hover {
			background-color: #a5a5a5;
			color: #ffffff !important;
		}

		input[type="submit"]:active,
		input[type="reset"]:active,
		input[type="button"]:active,
		.button:active {
			background-color: #8b8b8b;
		}

		input[type="submit"].icon,
		input[type="reset"].icon,
		input[type="button"].icon,
		.button.icon {
			padding-left: 1.35em;
		}

			input[type="submit"].icon:before,
			input[type="reset"].icon:before,
			input[type="button"].icon:before,
			.button.icon:before {
				margin-right: 0.5em;
			}

		input[type="submit"].fit,
		input[type="reset"].fit,
		input[type="button"].fit,
		.button.fit {
			width: 100%;
		}

		input[type="submit"].small,
		input[type="reset"].small,
		input[type="button"].small,
		.button.small {
			font-size: 0.8em;
		}

		input[type="submit"].large,
		input[type="reset"].large,
		input[type="button"].large,
		.button.large {
			font-size: 1.35em;
		}

		input[type="submit"].alt,
		input[type="reset"].alt,
		input[type="button"].alt,
		.button.alt {
			background-color: transparent;
			box-shadow: inset 0 0 0 2px #e4e4e4;
			color: #777 !important;
		}

			input[type="submit"].alt:hover,
			input[type="reset"].alt:hover,
			input[type="button"].alt:hover,
			.button.alt:hover {
				background-color: #f4f4f4;
				color: #777 !important;
			}

			input[type="submit"].alt:active,
			input[type="reset"].alt:active,
			input[type="button"].alt:active,
			.button.alt:active {
				background-color: #eaeaea;
			}

			input[type="submit"].alt.icon:before,
			input[type="reset"].alt.icon:before,
			input[type="button"].alt.icon:before,
			.button.alt.icon:before {
				color: #aaa;
			}

		input[type="submit"].primary,
		input[type="reset"].primary,
		input[type="button"].primary,
		.button.primary {
			background-color: #373A40;
			color: #ffffff !important;
		}

			input[type="submit"].primary:hover,
			input[type="reset"].primary:hover,
			input[type="button"].primary:hover,
			.button.primary:hover {
				background-color: #5ed0b1;
			}

			input[type="submit"].primary:active,
			input[type="reset"].primary:active,
			input[type="button"].primary:active,
			.button.primary:active {
				background-color: #39c29d;
			}

		input[type="submit"].disabled, input[type="submit"]:disabled,
		input[type="reset"].disabled,
		input[type="reset"]:disabled,
		input[type="button"].disabled,
		input[type="button"]:disabled,
		.button.disabled,
		.button:disabled {
			background-color: #888 !important;
			box-shadow: inset 0 -0.15em 0 0 rgba(0, 0, 0, 0.15);
			color: #fff !important;
			cursor: default;
			opacity: 0.25;
		}

/* Features */

	.features article {
		border-top: solid 3px #f4f4f4;
		margin-bottom: 2.25em;
		padding-top: 2.25em;
	}

		.features article:first-child {
			border-top: 0;
			padding-top: 0;
		}

		.features article .image {
			display: inline-block;
			padding-right: 2.5em;
			vertical-align: middle;
			width: 48%;
		}

			.features article .image img {
				display: block;
				width: 100%;
			}

		.features article .inner {
			display: inline-block;
			vertical-align: middle;
			width: 50%;
		}

			.features article .inner > :last-child {
				margin-bottom: 0;
			}

/* Header */

	#header {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: column;
		-webkit-flex-direction: column;
		-ms-flex-direction: column;
		flex-direction: column;
		-moz-justify-content: space-between;
		-webkit-justify-content: space-between;
		-ms-justify-content: space-between;
		justify-content: space-between;
		background: #373A40;
		color: #d2f2e9;
		height: 100%;
		overflow-y: auto;
		position: fixed;
		text-align: center;
		top: 0;
		width: 23em;
		right: 0;
	}

		#header h1, #header h2, #header h3, #header h4, #header h5, #header h6 {
			color: #ffffff;
		}

			#header h1 a, #header h2 a, #header h3 a, #header h4 a, #header h5 a, #header h6 a {
				color: #ffffff;
			}

		#header header p {
			color: #EEEEEE;
		}

		#header a {
			color: #d2f2e9;
		}

			#header a:hover {
				color: #ffffff !important;
			}

		#header > header {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			padding: 3em;
		}

			#header > header .avatar {
				display: block;
				margin: 0 auto 2.25em auto;
				width: 8em;
			}

			#header > header h1 {
				font-size: 1.75em;
				margin: 0;
			}

			#header > header p {
				color: #d2f2e9;
				font-style: italic;
				margin: 1em 0 0 0;
			}

		#header > footer {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			bottom: 0;
			left: 0;
			padding: 2em;
			width: 100%;
		}

			#header > footer .icons {
				margin: 0;
			}

				#header > footer .icons li a {
					color: #EEEEEE;
				}

		#header > nav {
			-moz-flex-grow: 1;
			-webkit-flex-grow: 1;
			-ms-flex-grow: 1;
			flex-grow: 1;
		}

			#header > nav ul {
				list-style: none;
				margin: 0;
				padding: 0;
			}

				#header > nav ul li {
					border-top: solid 2px #5ccfb1;
					display: block;
					padding: 0;
				}

					#header > nav ul li a {
						-moz-transition: none;
						-webkit-transition: none;
						-ms-transition: none;
						transition: none;
						border: 0;
						color: #ffffff !important;
						display: block;
						padding: 0.85em 0;
						text-decoration: none;
					}

						#header > nav ul li a.active {
							background: #fff;
							color: #373A40 !important;
						}

					#header > nav ul li:first-child {
						border-top: 0;
					}

/* Wrapper */

	#wrapper {
		background: #fff;
		padding-right: 23em;
	}

/* Main */

	#main > section {
		border-top: solid 6px #f4f4f4;
	}

		#main > section > .container {
			padding: 6em 0 4em 0;
		}

		#main > section:first-child {
			border-top: 0;
		}

/* Footer */

	#footer {
		background: #fafafa;
		border-top: 0;
		color: #c0c0c0;
		overflow: hidden;
		padding: 4em 0 2em 0;
	}

		#footer .copyright {
			line-height: 1em;
			list-style: none;
			padding: 0;
		}

			#footer .copyright li {
				border-left: solid 1px #d4d4d4;
				display: inline-block;
				font-size: 0.8em;
				margin-left: 1em;
				padding-left: 1em;
			}

				#footer .copyright li:first-child {
					border-left: 0;
					margin-left: 0;
					padding-left: 0;
				}

				#footer .copyright li a {
					color: inherit;
				}

/* XLarge */

	@media screen and (max-width: 1680px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 13pt;
			}

		/* Header */

			#header {
				width: 21em;
			}

				#header > header {
					padding: 2em;
				}

				#header > footer {
					padding: 1.5em;
				}

		/* Wrapper */

			#wrapper {
				padding-right: 21em;
			}

		/* Main */

			#main > section > .container {
				padding: 4em 0 2em 0;
			}

	}

/* Large */

	@media screen and (max-width: 1280px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 11pt;
			}

		/* Header */

			#header {
				width: 20em;
			}

		/* Wrapper */

			#wrapper {
				padding-right: 20em;
			}

	}

/* Medium */

	#titleBar {
		display: none;
	}

	@media screen and (max-width: 1024px) {

		/* Basic */

			html, body {
				overflow-x: hidden;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* Image */

			.image.left, .image.right {
				max-width: 40%;
			}

				.image.left img, .image.right img {
					width: 100%;
				}

			.image.main {
				height: 20em;
			}

		/* Header */

			#header {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 100%;
				overflow-y: auto;
				position: fixed;
				top: 0;
				width: 23em;
				z-index: 10002;
				-moz-transform: translateX(23em);
				-webkit-transform: translateX(23em);
				-ms-transform: translateX(23em);
				transform: translateX(23em);
				right: 0;
			}

				#header > footer {
					bottom: auto;
					left: auto;
					margin: 0.5em 0 0 0;
					position: relative;
					right: auto;
					top: auto;
				}

		/* Wrapper */

			#wrapper {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				padding: 44px 0 1px 0;
			}

		/* Header Panel */

			#titleBar {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 44px;
				left: 0;
				position: fixed;
				top: 0;
				width: 100%;
				z-index: 10001;
				background: #222;
				color: #fff;
				min-width: 320px;
			}

				#titleBar .title {
					color: #fff;
					display: block;
					font-weight: 700;
					height: 44px;
					line-height: 44px;
					padding: 0 1em;
					width: 100%;
					text-align: left;
				}

					#titleBar .title a {
						border: 0;
						text-decoration: none;
					}

				#titleBar .toggle {
					text-decoration: none;
					height: 4em;
					position: absolute;
					top: 0;
					width: 6em;
					border: 0;
					outline: 0;
					right: 0;
				}

					#titleBar .toggle:before {
						-moz-osx-font-smoothing: grayscale;
						-webkit-font-smoothing: antialiased;
						display: inline-block;
						font-style: normal;
						font-variant: normal;
						text-rendering: auto;
						line-height: 1;
						text-transform: none !important;
						font-family: 'Font Awesome 5 Free';
						font-weight: 900;
					}

					#titleBar .toggle:before {
						background: #373A40;
						color: #ffffff;
						content: '\\f0c9';
						display: block;
						font-size: 18px;
						height: 44px;
						line-height: 44px;
						position: absolute;
						text-align: center;
						top: 0;
						width: 64px;
						right: 0;
					}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-23em);
				-webkit-transform: translateX(-23em);
				-ms-transform: translateX(-23em);
				transform: translateX(-23em);
			}

			body.header-visible #header {
				-moz-transform: translateX(0);
				-webkit-transform: translateX(0);
				-ms-transform: translateX(0);
				transform: translateX(0);
			}

	}

/* Small */

	@media screen and (max-width: 736px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 12pt;
			}

			h1 br, h2 br, h3 br, h4 br, h5 br, h6 br {
				display: none;
			}

			h2 {
				font-size: 1.75em;
			}

			h3 {
				font-size: 1.5em;
			}

			h4 {
				font-size: 1em;
			}

		/* Image */

			.image.left {
				margin: 0 1.5em 1em 0;
			}

			.image.right {
				margin: 0 0 1em 1.5em;
			}

			.image.main {
				height: 12em;
			}

		/* Section/Article */

			header br {
				display: none;
			}

			header.major h2 {
				font-size: 2.5em;
			}

				header.major h2 + p {
					font-size: 1.5em;
				}

		/* Features */

			.features article .image {
				display: block;
				margin: 0 0 2.25em 0;
				padding-right: 0;
				width: 100%;
			}

			.features article .inner {
				display: block;
				width: 100%;
			}

		/* Header */

			#header {
				width: 17em;
				-moz-transform: translateX(17em);
				-webkit-transform: translateX(17em);
				-ms-transform: translateX(17em);
				transform: translateX(17em);
				right: 0;
			}

				#header > header {
					padding: 2em;
				}

					#header > header .avatar {
						margin: 0 auto 1.6875em auto;
						width: 6em;
					}

					#header > header h1 {
						font-size: 1.5em;
					}

					#header > header p {
						margin: 1em 0 0 0;
					}

				#header > footer {
					padding: 1.5em;
				}

		/* Main */

			#main > section > .container {
				padding: 2em 0 0 0;
			}

		/* Footer */

			#footer {
				text-align: center;
			}

				#footer .copyright li {
					border-left: 0;
					display: block;
					line-height: 1.75em;
					margin: 0.75em 0 0 0;
					padding-left: 0;
				}

					#footer .copyright li:first-child {
						margin-top: 0;
					}

		/* Header Panel */

			#titleBar .toggle {
				height: 4em;
				width: 6em;
			}

				#titleBar .toggle:before {
					font-size: 14px;
					width: 44px;
				}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-17em);
				-webkit-transform: translateX(-17em);
				-ms-transform: translateX(-17em);
				transform: translateX(-17em);
			}

	}

/* XSmall */

	@media screen and (max-width: 480px) {

		/* Basic */

			html, body {
				min-width: 320px;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* List */

			ul.actions {
				margin: 0 0 2.25em 0;
			}

				ul.actions li {
					display: block;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions li:first-child {
						padding-top: 0;
					}

					ul.actions li > * {
						width: 100%;
						margin: 0 !important;
					}

						ul.actions li > *.icon:before {
							margin-left: -2em;
						}

				ul.actions.small li {
					padding: 0.5625em 0 0 0;
				}

					ul.actions.small li:first-child {
						padding-top: 0;
					}

			ul.feature-icons li {
				display: block;
				width: 100%;
			}

		/* Button */

			input[type="submit"],
			input[type="reset"],
			input[type="button"],
			.button {
				padding: 0;
			}

	}
	/* Define the colors */
:root {
    --color-primary: #EEEEEE;
    --color-secondary: #686D76;
    --color-tertiary: #DC5F00;
    --color-quaternary: #373A40;
}

/* Example usage of the colors */
body {
    background-color: var(--color-primary);
    color: var(--color-quaternary);
}

.header {
    background-color: var(--color-secondary);
    color: var(--color-primary);
}

.button {
    background-color: var(--color-tertiary);
    color: var(--color-primary);
}

.footer {
    background-color: var(--color-quaternary);
    color: var(--color-secondary);
}

#main {
    background-color: #EEEEEE;
}
#header {
    background-color: #686D76;
}
#header {
    background-color: #686D76;
}
#footer , h1, h2, h3, h4{
	color: #373A40;
}
#wrapper {
	   border-top: solid 6px #EEEEEE;
}
header.major h2 {
    color: #373A40;
    font-size: 3.5em;
}
header.major h2 + p {
    color: #677D6A;
    /* font-size: 1.75em; */
    /* font-weight: 700; */
    /* margin-top: -0.75em; */
}""", 
"phantom":"""@import url("fontawesome-all.min.css");
@import url("https://fonts.googleapis.com/css?family=Lato:400,400italic,700,700italic|Source+Code+Pro:400");

/*
	Read Only by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #fff;
	}

		body.is-preload *, body.is-preload *:before, body.is-preload *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

	body, input, select, textarea {
		color: #888;
		font-family: "Lato", sans-serif;
		font-size: 16pt;
		font-weight: 400;
		line-height: 1.75em;
	}

	a {
		-moz-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-webkit-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-ms-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		border-bottom: solid 1px #e4e4e4;
		color: inherit;
		text-decoration: none;
	}

		a:hover {
			border-bottom-color: transparent;
			color: #3DC2EC !important;
		}

	strong, b {
		color: #777;
		font-weight: 700;
	}

	em, i {
		font-style: italic;
	}

	p {
		margin: 0 0 2.25em 0;
	}

	h1, h2, h3, h4, h5, h6 {
		color: #777;
		font-weight: 700;
		line-height: 1em;
		margin: 0 0 0.5625em 0;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			border: 0;
			color: inherit;
			text-decoration: none;
		}

	h2 {
		font-size: 2em;
		line-height: 1.5em;
	}

	h3 {
		font-size: 1.75em;
		line-height: 1.5em;
	}

	h4 {
		font-size: 1.25em;
		line-height: 1.5em;
	}

	h5 {
		font-size: 0.9em;
		line-height: 1.5em;
	}

	h6 {
		font-size: 0.7em;
		line-height: 1.5em;
	}

	sub {
		font-size: 0.8em;
		position: relative;
		top: 0.5em;
	}

	sup {
		font-size: 0.8em;
		position: relative;
		top: -0.5em;
	}

	hr {
		border: 0;
		border-bottom: solid 2px #f4f4f4;
		margin: 2.25em 0;
	}

		hr.major {
			margin: 3.375em 0;
		}

	blockquote {
		border-left: solid 8px #e4e4e4;
		font-style: italic;
		margin: 0 0 2.25em 0;
		padding: 0.5em 0 0.5em 2em;
	}

	code {
		background: #555;
		border-radius: 5px;
		color: #fff;
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0.25em;
		padding: 0.25em 0.65em;
	}

	pre {
		font-family: "Source Code Pro", monospace;
		font-size: 0.9em;
		margin: 0 0 2.25em 0;
	}

		pre code {
			-webkit-overflow-scrolling: touch;
			display: block;
			line-height: 1.5em;
			overflow-x: auto;
			padding: 1em 1.5em;
		}

	.align-left {
		text-align: left;
	}

	.align-center {
		text-align: center;
	}

	.align-right {
		text-align: right;
	}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0;
			margin-left: 0em;
		}

			.row.gtr-0 > * {
				padding: 0 0 0 0em;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0em;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0em;
				}

		.row.gtr-25 {
			margin-top: 0;
			margin-left: -0.5em;
		}

			.row.gtr-25 > * {
				padding: 0 0 0 0.5em;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -0.5em;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 0.5em;
				}

		.row.gtr-50 {
			margin-top: 0;
			margin-left: -1em;
		}

			.row.gtr-50 > * {
				padding: 0 0 0 1em;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -1em;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 1em;
				}

		.row {
			margin-top: 0;
			margin-left: -2em;
		}

			.row > * {
				padding: 0 0 0 2em;
			}

			.row.gtr-uniform {
				margin-top: -2em;
			}

				.row.gtr-uniform > * {
					padding-top: 2em;
				}

		.row.gtr-150 {
			margin-top: 0;
			margin-left: -3em;
		}

			.row.gtr-150 > * {
				padding: 0 0 0 3em;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -3em;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 3em;
				}

		.row.gtr-200 {
			margin-top: 0;
			margin-left: -4em;
		}

			.row.gtr-200 > * {
				padding: 0 0 0 4em;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -4em;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 4em;
				}

		@media screen and (max-width: 1680px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xlarge {
					order: -1;
				}

				.row > .col-1-xlarge {
					width: 8.33333%;
				}

				.row > .off-1-xlarge {
					margin-left: 8.33333%;
				}

				.row > .col-2-xlarge {
					width: 16.66667%;
				}

				.row > .off-2-xlarge {
					margin-left: 16.66667%;
				}

				.row > .col-3-xlarge {
					width: 25%;
				}

				.row > .off-3-xlarge {
					margin-left: 25%;
				}

				.row > .col-4-xlarge {
					width: 33.33333%;
				}

				.row > .off-4-xlarge {
					margin-left: 33.33333%;
				}

				.row > .col-5-xlarge {
					width: 41.66667%;
				}

				.row > .off-5-xlarge {
					margin-left: 41.66667%;
				}

				.row > .col-6-xlarge {
					width: 50%;
				}

				.row > .off-6-xlarge {
					margin-left: 50%;
				}

				.row > .col-7-xlarge {
					width: 58.33333%;
				}

				.row > .off-7-xlarge {
					margin-left: 58.33333%;
				}

				.row > .col-8-xlarge {
					width: 66.66667%;
				}

				.row > .off-8-xlarge {
					margin-left: 66.66667%;
				}

				.row > .col-9-xlarge {
					width: 75%;
				}

				.row > .off-9-xlarge {
					margin-left: 75%;
				}

				.row > .col-10-xlarge {
					width: 83.33333%;
				}

				.row > .off-10-xlarge {
					margin-left: 83.33333%;
				}

				.row > .col-11-xlarge {
					width: 91.66667%;
				}

				.row > .off-11-xlarge {
					margin-left: 91.66667%;
				}

				.row > .col-12-xlarge {
					width: 100%;
				}

				.row > .off-12-xlarge {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -1em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 1em;
						}

				.row {
					margin-top: 0;
					margin-left: -2em;
				}

					.row > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-uniform > * {
							padding-top: 2em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 3em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -4em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 4em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -4em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 4em;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-large {
					order: -1;
				}

				.row > .col-1-large {
					width: 8.33333%;
				}

				.row > .off-1-large {
					margin-left: 8.33333%;
				}

				.row > .col-2-large {
					width: 16.66667%;
				}

				.row > .off-2-large {
					margin-left: 16.66667%;
				}

				.row > .col-3-large {
					width: 25%;
				}

				.row > .off-3-large {
					margin-left: 25%;
				}

				.row > .col-4-large {
					width: 33.33333%;
				}

				.row > .off-4-large {
					margin-left: 33.33333%;
				}

				.row > .col-5-large {
					width: 41.66667%;
				}

				.row > .off-5-large {
					margin-left: 41.66667%;
				}

				.row > .col-6-large {
					width: 50%;
				}

				.row > .off-6-large {
					margin-left: 50%;
				}

				.row > .col-7-large {
					width: 58.33333%;
				}

				.row > .off-7-large {
					margin-left: 58.33333%;
				}

				.row > .col-8-large {
					width: 66.66667%;
				}

				.row > .off-8-large {
					margin-left: 66.66667%;
				}

				.row > .col-9-large {
					width: 75%;
				}

				.row > .off-9-large {
					margin-left: 75%;
				}

				.row > .col-10-large {
					width: 83.33333%;
				}

				.row > .off-10-large {
					margin-left: 83.33333%;
				}

				.row > .col-11-large {
					width: 91.66667%;
				}

				.row > .off-11-large {
					margin-left: 91.66667%;
				}

				.row > .col-12-large {
					width: 100%;
				}

				.row > .off-12-large {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 1024px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-medium {
					order: -1;
				}

				.row > .col-1-medium {
					width: 8.33333%;
				}

				.row > .off-1-medium {
					margin-left: 8.33333%;
				}

				.row > .col-2-medium {
					width: 16.66667%;
				}

				.row > .off-2-medium {
					margin-left: 16.66667%;
				}

				.row > .col-3-medium {
					width: 25%;
				}

				.row > .off-3-medium {
					margin-left: 25%;
				}

				.row > .col-4-medium {
					width: 33.33333%;
				}

				.row > .off-4-medium {
					margin-left: 33.33333%;
				}

				.row > .col-5-medium {
					width: 41.66667%;
				}

				.row > .off-5-medium {
					margin-left: 41.66667%;
				}

				.row > .col-6-medium {
					width: 50%;
				}

				.row > .off-6-medium {
					margin-left: 50%;
				}

				.row > .col-7-medium {
					width: 58.33333%;
				}

				.row > .off-7-medium {
					margin-left: 58.33333%;
				}

				.row > .col-8-medium {
					width: 66.66667%;
				}

				.row > .off-8-medium {
					margin-left: 66.66667%;
				}

				.row > .col-9-medium {
					width: 75%;
				}

				.row > .off-9-medium {
					margin-left: 75%;
				}

				.row > .col-10-medium {
					width: 83.33333%;
				}

				.row > .off-10-medium {
					margin-left: 83.33333%;
				}

				.row > .col-11-medium {
					width: 91.66667%;
				}

				.row > .off-11-medium {
					margin-left: 91.66667%;
				}

				.row > .col-12-medium {
					width: 100%;
				}

				.row > .off-12-medium {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-small {
					order: -1;
				}

				.row > .col-1-small {
					width: 8.33333%;
				}

				.row > .off-1-small {
					margin-left: 8.33333%;
				}

				.row > .col-2-small {
					width: 16.66667%;
				}

				.row > .off-2-small {
					margin-left: 16.66667%;
				}

				.row > .col-3-small {
					width: 25%;
				}

				.row > .off-3-small {
					margin-left: 25%;
				}

				.row > .col-4-small {
					width: 33.33333%;
				}

				.row > .off-4-small {
					margin-left: 33.33333%;
				}

				.row > .col-5-small {
					width: 41.66667%;
				}

				.row > .off-5-small {
					margin-left: 41.66667%;
				}

				.row > .col-6-small {
					width: 50%;
				}

				.row > .off-6-small {
					margin-left: 50%;
				}

				.row > .col-7-small {
					width: 58.33333%;
				}

				.row > .off-7-small {
					margin-left: 58.33333%;
				}

				.row > .col-8-small {
					width: 66.66667%;
				}

				.row > .off-8-small {
					margin-left: 66.66667%;
				}

				.row > .col-9-small {
					width: 75%;
				}

				.row > .off-9-small {
					margin-left: 75%;
				}

				.row > .col-10-small {
					width: 83.33333%;
				}

				.row > .off-10-small {
					margin-left: 83.33333%;
				}

				.row > .col-11-small {
					width: 91.66667%;
				}

				.row > .off-11-small {
					margin-left: 91.66667%;
				}

				.row > .col-12-small {
					width: 100%;
				}

				.row > .off-12-small {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

		@media screen and (max-width: 480px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xsmall {
					order: -1;
				}

				.row > .col-1-xsmall {
					width: 8.33333%;
				}

				.row > .off-1-xsmall {
					margin-left: 8.33333%;
				}

				.row > .col-2-xsmall {
					width: 16.66667%;
				}

				.row > .off-2-xsmall {
					margin-left: 16.66667%;
				}

				.row > .col-3-xsmall {
					width: 25%;
				}

				.row > .off-3-xsmall {
					margin-left: 25%;
				}

				.row > .col-4-xsmall {
					width: 33.33333%;
				}

				.row > .off-4-xsmall {
					margin-left: 33.33333%;
				}

				.row > .col-5-xsmall {
					width: 41.66667%;
				}

				.row > .off-5-xsmall {
					margin-left: 41.66667%;
				}

				.row > .col-6-xsmall {
					width: 50%;
				}

				.row > .off-6-xsmall {
					margin-left: 50%;
				}

				.row > .col-7-xsmall {
					width: 58.33333%;
				}

				.row > .off-7-xsmall {
					margin-left: 58.33333%;
				}

				.row > .col-8-xsmall {
					width: 66.66667%;
				}

				.row > .off-8-xsmall {
					margin-left: 66.66667%;
				}

				.row > .col-9-xsmall {
					width: 75%;
				}

				.row > .off-9-xsmall {
					margin-left: 75%;
				}

				.row > .col-10-xsmall {
					width: 83.33333%;
				}

				.row > .off-10-xsmall {
					margin-left: 83.33333%;
				}

				.row > .col-11-xsmall {
					width: 91.66667%;
				}

				.row > .off-11-xsmall {
					margin-left: 91.66667%;
				}

				.row > .col-12-xsmall {
					width: 100%;
				}

				.row > .off-12-xsmall {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.3125em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.3125em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.3125em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.3125em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -1.875em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 1.875em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -1.875em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 1.875em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 2.5em;
						}

		}

/* Container */

	.container {
		margin: 0 auto;
		max-width: calc(100% - 4.5em);
		width: 45em;
	}

		.container.xsmall {
			width: 11.25em;
		}

		.container.small {
			width: 22.5em;
		}

		.container.medium {
			width: 33.75em;
		}

		.container.large {
			width: 56.25em;
		}

		.container.xlarge {
			width: 67.5em;
		}

		.container.max {
			width: 100%;
		}

		@media screen and (max-width: 1024px) {

			.container {
				width: 100% !important;
			}

		}

		@media screen and (max-width: 480px) {

			.container {
				max-width: calc(100% - 3.375em);
			}

		}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header p {
		color: #aaa;
		position: relative;
		margin: 0 0 1.6875em 0;
	}

	header h2 + p {
		font-size: 1.25em;
		margin-top: -0.5em;
		line-height: 1.5em;
	}

	header h3 + p {
		font-size: 1.1em;
		margin-top: -0.35em;
		line-height: 1.5em;
	}

	header h4 + p,
	header h5 + p,
	header h6 + p {
		font-size: 0.9em;
		margin-top: -0.25em;
		line-height: 1.5em;
	}

	header.major h2 {
		color: #3DC2EC;
		font-size: 3.5em;
	}

		header.major h2 + p {
			color: #777;
			font-size: 1.75em;
			font-weight: 700;
			margin-top: -0.75em;
		}

/* Form */

	form {
		margin: 0 0 2.25em 0;
	}

	label {
		color: #777;
		display: block;
		font-size: 0.9em;
		font-weight: 700;
		margin: 0 0 1.125em 0;
	}

	input::-moz-focus-inner {
		border: 0;
		padding: 0;
	}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select,
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		border-radius: 5px;
		border: none;
		border: solid 2px #e4e4e4;
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 1em;
		text-decoration: none;
		width: 100%;
	}

		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		select:focus,
		textarea:focus {
			border-color: #3DC2EC;
		}

	select {
		background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' preserveAspectRatio='none' viewBox='0 0 40 40'%3E%3Cpath d='M9.4,12.3l10.4,10.4l10.4-10.4c0.2-0.2,0.5-0.4,0.9-0.4c0.3,0,0.6,0.1,0.9,0.4l3.3,3.3c0.2,0.2,0.4,0.5,0.4,0.9 c0,0.4-0.1,0.6-0.4,0.9L20.7,31.9c-0.2,0.2-0.5,0.4-0.9,0.4c-0.3,0-0.6-0.1-0.9-0.4L4.3,17.3c-0.2-0.2-0.4-0.5-0.4-0.9 c0-0.4,0.1-0.6,0.4-0.9l3.3-3.3c0.2-0.2,0.5-0.4,0.9-0.4S9.1,12.1,9.4,12.3z' fill='%23e4e4e4' /%3E%3C/svg%3E");
		background-size: 1.25em;
		background-repeat: no-repeat;
		background-position: calc(100% - 1em) center;
		height: 2.75em;
		padding-right: 2.75em;
		text-overflow: ellipsis;
	}

		select option {
			color: #777;
			background: #fff;
		}

		select:focus::-ms-value {
			background-color: transparent;
		}

		select::-ms-expand {
			display: none;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 2.75em;
	}

	textarea {
		padding: 0.75em 1em;
	}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2em;
		opacity: 0;
		width: 1em;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			color: #888;
			cursor: pointer;
			display: inline-block;
			font-size: 1em;
			font-weight: 400;
			padding-left: 2.4em;
			padding-right: 0.75em;
			position: relative;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				background: #fafafa;
				border-radius: 5px;
				border: solid 2px #e4e4e4;
				content: '';
				display: inline-block;
				font-size: 0.8em;
				height: 2.0625em;
				left: 0;
				line-height: 2.0625em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.0625em;
			}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			background: #989898;
			border-color: #989898;
			color: #402E7A;
			content: '\\f00c';
		}

		input[type="checkbox"]:focus + label:before,
		input[type="radio"]:focus + label:before {
			border-color: #3DC2EC;
		}

	input[type="checkbox"] + label:before {
		border-radius: 5px;
	}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	::-moz-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		color: #aaa !important;
		font-style: italic;
		opacity: 1.0;
	}

/* Box */

	.box {
		border-radius: 5px;
		border: solid 2px #e4e4e4;
		margin-bottom: 2.25em;
		padding: 1.5em;
	}

		.box > :last-child,
		.box > :last-child > :last-child,
		.box > :last-child > :last-child > :last-child {
			margin-bottom: 0;
		}

		.box.alt {
			border: 0;
			border-radius: 0;
			padding: 0;
		}

/* Icon */

	.icon {
		text-decoration: none;
		border-bottom: none;
		position: relative;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 400;
		}

		.icon > .label {
			display: none;
		}

		.icon:before {
			line-height: inherit;
		}

		.icon.solid:before {
			font-weight: 900;
		}

		.icon.brands:before {
			font-family: 'Font Awesome 5 Brands';
		}

/* Image */

	.image {
		border-radius: 5px;
		border: 0;
		display: inline-block;
		position: relative;
	}

		.image[data-position] img {
			-moz-object-fit: cover;
			-webkit-object-fit: cover;
			-ms-object-fit: cover;
			object-fit: cover;
			display: block;
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
		}

		.image[data-position="top left"] img {
			-moz-object-position: top left;
			-webkit-object-position: top left;
			-ms-object-position: top left;
			object-position: top left;
		}

		.image[data-position="top"] img {
			-moz-object-position: top;
			-webkit-object-position: top;
			-ms-object-position: top;
			object-position: top;
		}

		.image[data-position="top right"] img {
			-moz-object-position: top right;
			-webkit-object-position: top right;
			-ms-object-position: top right;
			object-position: top right;
		}

		.image[data-position="right"] img {
			-moz-object-position: right;
			-webkit-object-position: right;
			-ms-object-position: right;
			object-position: right;
		}

		.image[data-position="bottom right"] img {
			-moz-object-position: bottom right;
			-webkit-object-position: bottom right;
			-ms-object-position: bottom right;
			object-position: bottom right;
		}

		.image[data-position="bottom"] img {
			-moz-object-position: bottom;
			-webkit-object-position: bottom;
			-ms-object-position: bottom;
			object-position: bottom;
		}

		.image[data-position="bottom left"] img {
			-moz-object-position: bottom left;
			-webkit-object-position: bottom left;
			-ms-object-position: bottom left;
			object-position: bottom left;
		}

		.image[data-position="left"] img {
			-moz-object-position: left;
			-webkit-object-position: left;
			-ms-object-position: left;
			object-position: left;
		}

		.image[data-position="center"] img {
			-moz-object-position: center;
			-webkit-object-position: center;
			-ms-object-position: center;
			object-position: center;
		}

		.image[data-position="25% 25%"] img {
			-moz-object-position: 25% 25%;
			-webkit-object-position: 25% 25%;
			-ms-object-position: 25% 25%;
			object-position: 25% 25%;
		}

		.image[data-position="75% 25%"] img {
			-moz-object-position: 75% 25%;
			-webkit-object-position: 75% 25%;
			-ms-object-position: 75% 25%;
			object-position: 75% 25%;
		}

		.image[data-position="75% 75%"] img {
			-moz-object-position: 75% 75%;
			-webkit-object-position: 75% 75%;
			-ms-object-position: 75% 75%;
			object-position: 75% 75%;
		}

		.image[data-position="25% 75%"] img {
			-moz-object-position: 25% 75%;
			-webkit-object-position: 25% 75%;
			-ms-object-position: 25% 75%;
			object-position: 25% 75%;
		}

		.image img {
			border-radius: 5px;
			display: block;
		}

		.image.left {
			float: left;
			margin: 0 2.5em 2em 0;
			top: 0.25em;
		}

		.image.right {
			float: right;
			margin: 0 0 2em 2.5em;
			top: 0.25em;
		}

		.image.fit {
			display: block;
			margin: 0 0 2.25em 0;
			width: 100%;
		}

			.image.fit img {
				display: block;
				width: 100%;
			}

		.image.avatar {
			border-radius: 100%;
			overflow: hidden;
		}

			.image.avatar img {
				border-radius: 100%;
				display: block;
				width: 100%;
			}

		.image.main {
			display: block;
			height: 20em;
			border-radius: 0;
		}

			.image.main img {
				border-radius: 0;
			}

/* List */

	ol {
		list-style: decimal;
		margin: 0 0 2.25em 0;
		padding-left: 1.25em;
	}

		ol li {
			padding-left: 0.25em;
		}

	ul {
		list-style: disc;
		margin: 0 0 2.25em 0;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
		}

		ul.alt {
			list-style: none;
			padding-left: 0;
		}

			ul.alt li {
				border-top: solid 2px #f4f4f4;
				padding: 0.5em 0;
			}

				ul.alt li:first-child {
					border-top: 0;
					padding-top: 0;
				}

	dl {
		margin: 0 0 2.25em 0;
	}

/* Actions */

	ul.actions {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		cursor: default;
		list-style: none;
		margin-left: -1.125em;
		padding-left: 0;
	}

		ul.actions li {
			padding: 0 0 0 1.125em;
			vertical-align: middle;
		}

		ul.actions.special {
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 100%;
			margin-left: 0;
		}

			ul.actions.special li:first-child {
				padding-left: 0;
			}

		ul.actions.stacked {
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			margin-left: 0;
		}

			ul.actions.stacked li {
				padding: 1.125em 0 0 0;
			}

				ul.actions.stacked li:first-child {
					padding-top: 0;
				}

		ul.actions.fit {
			width: calc(100% + 1.125em);
		}

			ul.actions.fit li {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				width: 100%;
			}

				ul.actions.fit li > * {
					width: 100%;
				}

			ul.actions.fit.stacked {
				width: 100%;
			}

		@media screen and (max-width: 480px) {

			ul.actions:not(.fixed) {
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
				margin-left: 0;
				width: 100% !important;
			}

				ul.actions:not(.fixed) li {
					-moz-flex-grow: 1;
					-webkit-flex-grow: 1;
					-ms-flex-grow: 1;
					flex-grow: 1;
					-moz-flex-shrink: 1;
					-webkit-flex-shrink: 1;
					-ms-flex-shrink: 1;
					flex-shrink: 1;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions:not(.fixed) li > * {
						width: 100%;
					}

					ul.actions:not(.fixed) li:first-child {
						padding-top: 0;
					}

					ul.actions:not(.fixed) li input[type="submit"],
					ul.actions:not(.fixed) li input[type="reset"],
					ul.actions:not(.fixed) li input[type="button"],
					ul.actions:not(.fixed) li button,
					ul.actions:not(.fixed) li .button {
						width: 100%;
					}

						ul.actions:not(.fixed) li input[type="submit"].icon:before,
						ul.actions:not(.fixed) li input[type="reset"].icon:before,
						ul.actions:not(.fixed) li input[type="button"].icon:before,
						ul.actions:not(.fixed) li button.icon:before,
						ul.actions:not(.fixed) li .button.icon:before {
							margin-left: -0.5rem;
						}

		}

/* Feature Icons */

	ul.feature-icons {
		list-style: none;
		padding-left: 0;
	}

		ul.feature-icons li {
			text-decoration: none;
			display: inline-block;
			margin: 0 0 1.6875em 0;
			padding: 0.35em 0 0 3.5em;
			position: relative;
			vertical-align: top;
			width: 48%;
		}

			ul.feature-icons li:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 400;
			}

			ul.feature-icons li:before {
				background: #3DC2EC;
				border-radius: 100%;
				color: #ffffff;
				display: block;
				height: 2.5em;
				left: 0;
				line-height: 2.5em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.5em;
			}

/* Icons */

	ul.icons {
		cursor: default;
		list-style: none;
		padding-left: 0;
	}

		ul.icons li {
			display: inline-block;
			padding: 0 1em 0 0;
		}

			ul.icons li:last-child {
				padding-right: 0 !important;
			}

			ul.icons li .icon:before {
				font-size: 1.25em;
			}

/* Table */

	.table-wrapper {
		-webkit-overflow-scrolling: touch;
		overflow-x: auto;
	}

	table {
		margin: 0 0 2.25em 0;
		width: 100%;
	}

		table tbody tr {
			border: solid 2px #f4f4f4;
			border-left: 0;
			border-right: 0;
		}

			table tbody tr:nth-child(2n + 1) {
				background-color: #fafafa;
			}

		table td {
			padding: 0.75em 0.75em;
		}

		table th {
			color: #777;
			font-size: 0.9em;
			font-weight: 700;
			padding: 0 0.75em 0.75em 0.75em;
			text-align: left;
		}

		table thead {
			border-bottom: solid 4px #e4e4e4;
		}

		table tfoot {
			border-top: solid 4px #e4e4e4;
		}

		table.alt {
			border-collapse: separate;
		}

			table.alt tbody tr td {
				border: solid 2px #e4e4e4;
				border-left-width: 0;
				border-top-width: 0;
			}

				table.alt tbody tr td:first-child {
					border-left-width: 2px;
				}

			table.alt tbody tr:first-child td {
				border-top-width: 2px;
			}

			table.alt thead {
				border-bottom: 0;
			}

			table.alt tfoot {
				border-top: 0;
			}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
		background-color: #989898;
		border-radius: 5px;
		border: 0;
		color: #ffffff !important;
		cursor: pointer;
		display: inline-block;
		font-weight: 700;
		height: 2.75em;
		line-height: 2.75em;
		padding: 0 1.5em;
		text-align: center;
		text-decoration: none;
		white-space: nowrap;
	}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		.button:hover {
			background-color: #a5a5a5;
			color: #ffffff !important;
		}

		input[type="submit"]:active,
		input[type="reset"]:active,
		input[type="button"]:active,
		.button:active {
			background-color: #8b8b8b;
		}

		input[type="submit"].icon,
		input[type="reset"].icon,
		input[type="button"].icon,
		.button.icon {
			padding-left: 1.35em;
		}

			input[type="submit"].icon:before,
			input[type="reset"].icon:before,
			input[type="button"].icon:before,
			.button.icon:before {
				margin-right: 0.5em;
			}

		input[type="submit"].fit,
		input[type="reset"].fit,
		input[type="button"].fit,
		.button.fit {
			width: 100%;
		}

		input[type="submit"].small,
		input[type="reset"].small,
		input[type="button"].small,
		.button.small {
			font-size: 0.8em;
		}

		input[type="submit"].large,
		input[type="reset"].large,
		input[type="button"].large,
		.button.large {
			font-size: 1.35em;
		}

		input[type="submit"].alt,
		input[type="reset"].alt,
		input[type="button"].alt,
		.button.alt {
			background-color: transparent;
			box-shadow: inset 0 0 0 2px #e4e4e4;
			color: #777 !important;
		}

			input[type="submit"].alt:hover,
			input[type="reset"].alt:hover,
			input[type="button"].alt:hover,
			.button.alt:hover {
				background-color: #f4f4f4;
				color: #777 !important;
			}

			input[type="submit"].alt:active,
			input[type="reset"].alt:active,
			input[type="button"].alt:active,
			.button.alt:active {
				background-color: #eaeaea;
			}

			input[type="submit"].alt.icon:before,
			input[type="reset"].alt.icon:before,
			input[type="button"].alt.icon:before,
			.button.alt.icon:before {
				color: #aaa;
			}

		input[type="submit"].primary,
		input[type="reset"].primary,
		input[type="button"].primary,
		.button.primary {
			background-color: #3DC2EC;
			color: #ffffff !important;
		}

			input[type="submit"].primary:hover,
			input[type="reset"].primary:hover,
			input[type="button"].primary:hover,
			.button.primary:hover {
				background-color: #5ed0b1;
			}

			input[type="submit"].primary:active,
			input[type="reset"].primary:active,
			input[type="button"].primary:active,
			.button.primary:active {
				background-color: #39c29d;
			}

		input[type="submit"].disabled, input[type="submit"]:disabled,
		input[type="reset"].disabled,
		input[type="reset"]:disabled,
		input[type="button"].disabled,
		input[type="button"]:disabled,
		.button.disabled,
		.button:disabled {
			background-color: #888 !important;
			box-shadow: inset 0 -0.15em 0 0 rgba(0, 0, 0, 0.15);
			color: #fff !important;
			cursor: default;
			opacity: 0.25;
		}

/* Features */

	.features article {
		border-top: solid 3px #f4f4f4;
		margin-bottom: 2.25em;
		padding-top: 2.25em;
	}

		.features article:first-child {
			border-top: 0;
			padding-top: 0;
		}

		.features article .image {
			display: inline-block;
			padding-right: 2.5em;
			vertical-align: middle;
			width: 48%;
		}

			.features article .image img {
				display: block;
				width: 100%;
			}

		.features article .inner {
			display: inline-block;
			vertical-align: middle;
			width: 50%;
		}

			.features article .inner > :last-child {
				margin-bottom: 0;
			}

/* Header */

	#header {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: column;
		-webkit-flex-direction: column;
		-ms-flex-direction: column;
		flex-direction: column;
		-moz-justify-content: space-between;
		-webkit-justify-content: space-between;
		-ms-justify-content: space-between;
		justify-content: space-between;
		background: #3DC2EC;
		color: #d2f2e9;
		height: 100%;
		overflow-y: auto;
		position: fixed;
		text-align: center;
		top: 0;
		width: 23em;
		right: 0;
	}

		#header h1, #header h2, #header h3, #header h4, #header h5, #header h6 {
			color: #ffffff;
		}

			#header h1 a, #header h2 a, #header h3 a, #header h4 a, #header h5 a, #header h6 a {
				color: #ffffff;
			}

		#header header p {
			color: #402E7A;
		}

		#header a {
			color: #d2f2e9;
		}

			#header a:hover {
				color: #ffffff !important;
			}

		#header > header {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			padding: 3em;
		}

			#header > header .avatar {
				display: block;
				margin: 0 auto 2.25em auto;
				width: 8em;
			}

			#header > header h1 {
				font-size: 1.75em;
				margin: 0;
			}

			#header > header p {
				color: #d2f2e9;
				font-style: italic;
				margin: 1em 0 0 0;
			}

		#header > footer {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			bottom: 0;
			left: 0;
			padding: 2em;
			width: 100%;
		}

			#header > footer .icons {
				margin: 0;
			}

				#header > footer .icons li a {
					color: #402E7A;
				}

		#header > nav {
			-moz-flex-grow: 1;
			-webkit-flex-grow: 1;
			-ms-flex-grow: 1;
			flex-grow: 1;
		}

			#header > nav ul {
				list-style: none;
				margin: 0;
				padding: 0;
			}

				#header > nav ul li {
					border-top: solid 2px #5ccfb1;
					display: block;
					padding: 0;
				}

					#header > nav ul li a {
						-moz-transition: none;
						-webkit-transition: none;
						-ms-transition: none;
						transition: none;
						border: 0;
						color: #ffffff !important;
						display: block;
						padding: 0.85em 0;
						text-decoration: none;
					}

						#header > nav ul li a.active {
							background: #fff;
							color: #3DC2EC !important;
						}

					#header > nav ul li:first-child {
						border-top: 0;
					}

/* Wrapper */

	#wrapper {
		background: #fff;
		padding-right: 23em;
	}

/* Main */

	#main > section {
		border-top: solid 6px #f4f4f4;
	}

		#main > section > .container {
			padding: 6em 0 4em 0;
		}

		#main > section:first-child {
			border-top: 0;
		}

/* Footer */

	#footer {
		background: #fafafa;
		border-top: 0;
		color: #c0c0c0;
		overflow: hidden;
		padding: 4em 0 2em 0;
	}

		#footer .copyright {
			line-height: 1em;
			list-style: none;
			padding: 0;
		}

			#footer .copyright li {
				border-left: solid 1px #d4d4d4;
				display: inline-block;
				font-size: 0.8em;
				margin-left: 1em;
				padding-left: 1em;
			}

				#footer .copyright li:first-child {
					border-left: 0;
					margin-left: 0;
					padding-left: 0;
				}

				#footer .copyright li a {
					color: inherit;
				}

/* XLarge */

	@media screen and (max-width: 1680px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 13pt;
			}

		/* Header */

			#header {
				width: 21em;
			}

				#header > header {
					padding: 2em;
				}

				#header > footer {
					padding: 1.5em;
				}

		/* Wrapper */

			#wrapper {
				padding-right: 21em;
			}

		/* Main */

			#main > section > .container {
				padding: 4em 0 2em 0;
			}

	}

/* Large */

	@media screen and (max-width: 1280px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 11pt;
			}

		/* Header */

			#header {
				width: 20em;
			}

		/* Wrapper */

			#wrapper {
				padding-right: 20em;
			}

	}

/* Medium */

	#titleBar {
		display: none;
	}

	@media screen and (max-width: 1024px) {

		/* Basic */

			html, body {
				overflow-x: hidden;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* Image */

			.image.left, .image.right {
				max-width: 40%;
			}

				.image.left img, .image.right img {
					width: 100%;
				}

			.image.main {
				height: 20em;
			}

		/* Header */

			#header {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 100%;
				overflow-y: auto;
				position: fixed;
				top: 0;
				width: 23em;
				z-index: 10002;
				-moz-transform: translateX(23em);
				-webkit-transform: translateX(23em);
				-ms-transform: translateX(23em);
				transform: translateX(23em);
				right: 0;
			}

				#header > footer {
					bottom: auto;
					left: auto;
					margin: 0.5em 0 0 0;
					position: relative;
					right: auto;
					top: auto;
				}

		/* Wrapper */

			#wrapper {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				padding: 44px 0 1px 0;
			}

		/* Header Panel */

			#titleBar {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 44px;
				left: 0;
				position: fixed;
				top: 0;
				width: 100%;
				z-index: 10001;
				background: #222;
				color: #fff;
				min-width: 320px;
			}

				#titleBar .title {
					color: #fff;
					display: block;
					font-weight: 700;
					height: 44px;
					line-height: 44px;
					padding: 0 1em;
					width: 100%;
					text-align: left;
				}

					#titleBar .title a {
						border: 0;
						text-decoration: none;
					}

				#titleBar .toggle {
					text-decoration: none;
					height: 4em;
					position: absolute;
					top: 0;
					width: 6em;
					border: 0;
					outline: 0;
					right: 0;
				}

					#titleBar .toggle:before {
						-moz-osx-font-smoothing: grayscale;
						-webkit-font-smoothing: antialiased;
						display: inline-block;
						font-style: normal;
						font-variant: normal;
						text-rendering: auto;
						line-height: 1;
						text-transform: none !important;
						font-family: 'Font Awesome 5 Free';
						font-weight: 900;
					}

					#titleBar .toggle:before {
						background: #3DC2EC;
						color: #ffffff;
						content: '\\f0c9';
						display: block;
						font-size: 18px;
						height: 44px;
						line-height: 44px;
						position: absolute;
						text-align: center;
						top: 0;
						width: 64px;
						right: 0;
					}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-23em);
				-webkit-transform: translateX(-23em);
				-ms-transform: translateX(-23em);
				transform: translateX(-23em);
			}

			body.header-visible #header {
				-moz-transform: translateX(0);
				-webkit-transform: translateX(0);
				-ms-transform: translateX(0);
				transform: translateX(0);
			}

	}

/* Small */

	@media screen and (max-width: 736px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 12pt;
			}

			h1 br, h2 br, h3 br, h4 br, h5 br, h6 br {
				display: none;
			}

			h2 {
				font-size: 1.75em;
			}

			h3 {
				font-size: 1.5em;
			}

			h4 {
				font-size: 1em;
			}

		/* Image */

			.image.left {
				margin: 0 1.5em 1em 0;
			}

			.image.right {
				margin: 0 0 1em 1.5em;
			}

			.image.main {
				height: 12em;
			}

		/* Section/Article */

			header br {
				display: none;
			}

			header.major h2 {
				font-size: 2.5em;
			}

				header.major h2 + p {
					font-size: 1.5em;
				}

		/* Features */

			.features article .image {
				display: block;
				margin: 0 0 2.25em 0;
				padding-right: 0;
				width: 100%;
			}

			.features article .inner {
				display: block;
				width: 100%;
			}

		/* Header */

			#header {
				width: 17em;
				-moz-transform: translateX(17em);
				-webkit-transform: translateX(17em);
				-ms-transform: translateX(17em);
				transform: translateX(17em);
				right: 0;
			}

				#header > header {
					padding: 2em;
				}

					#header > header .avatar {
						margin: 0 auto 1.6875em auto;
						width: 6em;
					}

					#header > header h1 {
						font-size: 1.5em;
					}

					#header > header p {
						margin: 1em 0 0 0;
					}

				#header > footer {
					padding: 1.5em;
				}

		/* Main */

			#main > section > .container {
				padding: 2em 0 0 0;
			}

		/* Footer */

			#footer {
				text-align: center;
			}

				#footer .copyright li {
					border-left: 0;
					display: block;
					line-height: 1.75em;
					margin: 0.75em 0 0 0;
					padding-left: 0;
				}

					#footer .copyright li:first-child {
						margin-top: 0;
					}

		/* Header Panel */

			#titleBar .toggle {
				height: 4em;
				width: 6em;
			}

				#titleBar .toggle:before {
					font-size: 14px;
					width: 44px;
				}

			body.header-visible #wrapper, body.header-visible #titleBar {
				-moz-transform: translateX(-17em);
				-webkit-transform: translateX(-17em);
				-ms-transform: translateX(-17em);
				transform: translateX(-17em);
			}

	}

/* XSmall */

	@media screen and (max-width: 480px) {

		/* Basic */

			html, body {
				min-width: 320px;
			}

			body, input, select, textarea {
				font-size: 12pt;
			}

		/* List */

			ul.actions {
				margin: 0 0 2.25em 0;
			}

				ul.actions li {
					display: block;
					padding: 1.125em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions li:first-child {
						padding-top: 0;
					}

					ul.actions li > * {
						width: 100%;
						margin: 0 !important;
					}

						ul.actions li > *.icon:before {
							margin-left: -2em;
						}

				ul.actions.small li {
					padding: 0.5625em 0 0 0;
				}

					ul.actions.small li:first-child {
						padding-top: 0;
					}

			ul.feature-icons li {
				display: block;
				width: 100%;
			}

		/* Button */

			input[type="submit"],
			input[type="reset"],
			input[type="button"],
			.button {
				padding: 0;
			}

	}
	/* Define the colors */
:root {
    --color-primary: #402E7A;
    --color-secondary: #4C3BCF;
    --color-tertiary: #4B70F5;
    --color-quaternary: #3DC2EC;
}

/* Example usage of the colors */
body {
    background-color: var(--color-primary);
    color: var(--color-quaternary);
}

.header {
    background-color: var(--color-secondary);
    color: var(--color-primary);
}

.button {
    background-color: var(--color-tertiary);
    color: var(--color-primary);
}

.footer {
    background-color: var(--color-quaternary);
    color: var(--color-secondary);
}

#main {
    background-color: #402E7A;
}
#header {
    background-color: #4C3BCF;
}
#header {
    background-color: #4C3BCF;
}
#footer , h1, h2, h3, h4{
	color: #3DC2EC;
}
#wrapper {
	   border-top: solid 6px #402E7A;
}
header.major h2 {
    color: #3DC2EC;
    font-size: 3.5em;
}
header.major h2 + p {
    color: #677D6A;
    /* font-size: 1.75em; */
    /* font-weight: 700; */
    /* margin-top: -0.75em; */
}
p , a{
	color: #3DC2EC;
    margin: 0 0 2.25em 0;
}
header.major h2 + p {
    color: #98e7ff;
    /* font-size: 1.75em; */
    /* font-weight: 700; */
    /* margin-top: -0.75em; */
}
"""

}, "arcana":
{
	"default":"""@import url("fontawesome-all.min.css");
@import url("https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,300italic,600,600italic");

/*
	Arcana by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #f7f7f7 url("ambient.png");
	}

		body.is-preload *, body.is-preload *:before, body.is-preload *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

	body, input, select, textarea {
		color: #474747;
		font-family: 'Source Sans Pro', sans-serif;
		font-size: 16pt;
		font-weight: 300;
		line-height: 1.65em;
	}

	a {
		-moz-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out, opacity 0.2s ease-in-out;
		-webkit-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out, opacity 0.2s ease-in-out;
		-ms-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out, opacity 0.2s ease-in-out;
		transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out, opacity 0.2s ease-in-out;
		color: #37c0fb;
		text-decoration: none;
		border-bottom: dotted 1px;
	}

		a:hover {
			color: #37c0fb;
			border-bottom-color: transparent;
		}

	strong, b {
		font-weight: 600;
	}

	em, i {
		font-style: italic;
	}

	p, ul, ol, dl, table, blockquote {
		margin: 0 0 2em 0;
	}

	h1, h2, h3, h4, h5, h6 {
		color: inherit;
		font-weight: 600;
		line-height: 1.75em;
		margin-bottom: 1em;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			color: inherit;
			text-decoration: none;
		}

		h1 em, h2 em, h3 em, h4 em, h5 em, h6 em {
			font-style: normal;
			font-weight: 300;
		}

	h2 {
		font-size: 1.75em;
		letter-spacing: -0.025em;
	}

	h3 {
		font-size: 1.2em;
		letter-spacing: -0.025em;
	}

	sub {
		font-size: 0.8em;
		position: relative;
		top: 0.5em;
	}

	sup {
		font-size: 0.8em;
		position: relative;
		top: -0.5em;
	}

	hr {
		border-top: solid 1px #e0e0e0;
		border: 0;
		margin-bottom: 1.5em;
	}

	blockquote {
		border-left: solid 0.5em #e0e0e0;
		font-style: italic;
		padding: 1em 0 1em 2em;
	}

/* Container */

	.container {
		margin: 0 auto;
		max-width: 100%;
		width: 1400px;
	}

		@media screen and (max-width: 1680px) {

			.container {
				width: 1200px;
			}

		}

		@media screen and (max-width: 1280px) {

			.container {
				width: 960px;
			}

		}

		@media screen and (max-width: 980px) {

			.container {
				width: 95%;
			}

		}

		@media screen and (max-width: 840px) {

			.container {
				width: 95%;
			}

		}

		@media screen and (max-width: 736px) {

			.container {
				width: 90%;
			}

		}

		@media screen and (max-width: 480px) {

			.container {
				width: 100%;
			}

		}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0px;
			margin-left: 0px;
		}

			.row.gtr-0 > * {
				padding: 0px 0 0 0px;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0px;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0px;
				}

		.row.gtr-25 {
			margin-top: -12.5px;
			margin-left: -12.5px;
		}

			.row.gtr-25 > * {
				padding: 12.5px 0 0 12.5px;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -12.5px;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 12.5px;
				}

		.row.gtr-50 {
			margin-top: -25px;
			margin-left: -25px;
		}

			.row.gtr-50 > * {
				padding: 25px 0 0 25px;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -25px;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 25px;
				}

		.row {
			margin-top: -50px;
			margin-left: -50px;
		}

			.row > * {
				padding: 50px 0 0 50px;
			}

			.row.gtr-uniform {
				margin-top: -50px;
			}

				.row.gtr-uniform > * {
					padding-top: 50px;
				}

		.row.gtr-150 {
			margin-top: -75px;
			margin-left: -75px;
		}

			.row.gtr-150 > * {
				padding: 75px 0 0 75px;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -75px;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 75px;
				}

		.row.gtr-200 {
			margin-top: -100px;
			margin-left: -100px;
		}

			.row.gtr-200 > * {
				padding: 100px 0 0 100px;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -100px;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 100px;
				}

		@media screen and (max-width: 1680px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-wide {
					order: -1;
				}

				.row > .col-1-wide {
					width: 8.33333%;
				}

				.row > .off-1-wide {
					margin-left: 8.33333%;
				}

				.row > .col-2-wide {
					width: 16.66667%;
				}

				.row > .off-2-wide {
					margin-left: 16.66667%;
				}

				.row > .col-3-wide {
					width: 25%;
				}

				.row > .off-3-wide {
					margin-left: 25%;
				}

				.row > .col-4-wide {
					width: 33.33333%;
				}

				.row > .off-4-wide {
					margin-left: 33.33333%;
				}

				.row > .col-5-wide {
					width: 41.66667%;
				}

				.row > .off-5-wide {
					margin-left: 41.66667%;
				}

				.row > .col-6-wide {
					width: 50%;
				}

				.row > .off-6-wide {
					margin-left: 50%;
				}

				.row > .col-7-wide {
					width: 58.33333%;
				}

				.row > .off-7-wide {
					margin-left: 58.33333%;
				}

				.row > .col-8-wide {
					width: 66.66667%;
				}

				.row > .off-8-wide {
					margin-left: 66.66667%;
				}

				.row > .col-9-wide {
					width: 75%;
				}

				.row > .off-9-wide {
					margin-left: 75%;
				}

				.row > .col-10-wide {
					width: 83.33333%;
				}

				.row > .off-10-wide {
					margin-left: 83.33333%;
				}

				.row > .col-11-wide {
					width: 91.66667%;
				}

				.row > .off-11-wide {
					margin-left: 91.66667%;
				}

				.row > .col-12-wide {
					width: 100%;
				}

				.row > .off-12-wide {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -10px;
					margin-left: -10px;
				}

					.row.gtr-25 > * {
						padding: 10px 0 0 10px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -10px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 10px;
						}

				.row.gtr-50 {
					margin-top: -20px;
					margin-left: -20px;
				}

					.row.gtr-50 > * {
						padding: 20px 0 0 20px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -20px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 20px;
						}

				.row {
					margin-top: -40px;
					margin-left: -40px;
				}

					.row > * {
						padding: 40px 0 0 40px;
					}

					.row.gtr-uniform {
						margin-top: -40px;
					}

						.row.gtr-uniform > * {
							padding-top: 40px;
						}

				.row.gtr-150 {
					margin-top: -60px;
					margin-left: -60px;
				}

					.row.gtr-150 > * {
						padding: 60px 0 0 60px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -60px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 60px;
						}

				.row.gtr-200 {
					margin-top: -80px;
					margin-left: -80px;
				}

					.row.gtr-200 > * {
						padding: 80px 0 0 80px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -80px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 80px;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-normal {
					order: -1;
				}

				.row > .col-1-normal {
					width: 8.33333%;
				}

				.row > .off-1-normal {
					margin-left: 8.33333%;
				}

				.row > .col-2-normal {
					width: 16.66667%;
				}

				.row > .off-2-normal {
					margin-left: 16.66667%;
				}

				.row > .col-3-normal {
					width: 25%;
				}

				.row > .off-3-normal {
					margin-left: 25%;
				}

				.row > .col-4-normal {
					width: 33.33333%;
				}

				.row > .off-4-normal {
					margin-left: 33.33333%;
				}

				.row > .col-5-normal {
					width: 41.66667%;
				}

				.row > .off-5-normal {
					margin-left: 41.66667%;
				}

				.row > .col-6-normal {
					width: 50%;
				}

				.row > .off-6-normal {
					margin-left: 50%;
				}

				.row > .col-7-normal {
					width: 58.33333%;
				}

				.row > .off-7-normal {
					margin-left: 58.33333%;
				}

				.row > .col-8-normal {
					width: 66.66667%;
				}

				.row > .off-8-normal {
					margin-left: 66.66667%;
				}

				.row > .col-9-normal {
					width: 75%;
				}

				.row > .off-9-normal {
					margin-left: 75%;
				}

				.row > .col-10-normal {
					width: 83.33333%;
				}

				.row > .off-10-normal {
					margin-left: 83.33333%;
				}

				.row > .col-11-normal {
					width: 91.66667%;
				}

				.row > .off-11-normal {
					margin-left: 91.66667%;
				}

				.row > .col-12-normal {
					width: 100%;
				}

				.row > .off-12-normal {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -7.5px;
					margin-left: -7.5px;
				}

					.row.gtr-25 > * {
						padding: 7.5px 0 0 7.5px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -7.5px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 7.5px;
						}

				.row.gtr-50 {
					margin-top: -15px;
					margin-left: -15px;
				}

					.row.gtr-50 > * {
						padding: 15px 0 0 15px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -15px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 15px;
						}

				.row {
					margin-top: -30px;
					margin-left: -30px;
				}

					.row > * {
						padding: 30px 0 0 30px;
					}

					.row.gtr-uniform {
						margin-top: -30px;
					}

						.row.gtr-uniform > * {
							padding-top: 30px;
						}

				.row.gtr-150 {
					margin-top: -45px;
					margin-left: -45px;
				}

					.row.gtr-150 > * {
						padding: 45px 0 0 45px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -45px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 45px;
						}

				.row.gtr-200 {
					margin-top: -60px;
					margin-left: -60px;
				}

					.row.gtr-200 > * {
						padding: 60px 0 0 60px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -60px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 60px;
						}

		}

		@media screen and (max-width: 980px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-narrow {
					order: -1;
				}

				.row > .col-1-narrow {
					width: 8.33333%;
				}

				.row > .off-1-narrow {
					margin-left: 8.33333%;
				}

				.row > .col-2-narrow {
					width: 16.66667%;
				}

				.row > .off-2-narrow {
					margin-left: 16.66667%;
				}

				.row > .col-3-narrow {
					width: 25%;
				}

				.row > .off-3-narrow {
					margin-left: 25%;
				}

				.row > .col-4-narrow {
					width: 33.33333%;
				}

				.row > .off-4-narrow {
					margin-left: 33.33333%;
				}

				.row > .col-5-narrow {
					width: 41.66667%;
				}

				.row > .off-5-narrow {
					margin-left: 41.66667%;
				}

				.row > .col-6-narrow {
					width: 50%;
				}

				.row > .off-6-narrow {
					margin-left: 50%;
				}

				.row > .col-7-narrow {
					width: 58.33333%;
				}

				.row > .off-7-narrow {
					margin-left: 58.33333%;
				}

				.row > .col-8-narrow {
					width: 66.66667%;
				}

				.row > .off-8-narrow {
					margin-left: 66.66667%;
				}

				.row > .col-9-narrow {
					width: 75%;
				}

				.row > .off-9-narrow {
					margin-left: 75%;
				}

				.row > .col-10-narrow {
					width: 83.33333%;
				}

				.row > .off-10-narrow {
					margin-left: 83.33333%;
				}

				.row > .col-11-narrow {
					width: 91.66667%;
				}

				.row > .off-11-narrow {
					margin-left: 91.66667%;
				}

				.row > .col-12-narrow {
					width: 100%;
				}

				.row > .off-12-narrow {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -7.5px;
					margin-left: -7.5px;
				}

					.row.gtr-25 > * {
						padding: 7.5px 0 0 7.5px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -7.5px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 7.5px;
						}

				.row.gtr-50 {
					margin-top: -15px;
					margin-left: -15px;
				}

					.row.gtr-50 > * {
						padding: 15px 0 0 15px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -15px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 15px;
						}

				.row {
					margin-top: -30px;
					margin-left: -30px;
				}

					.row > * {
						padding: 30px 0 0 30px;
					}

					.row.gtr-uniform {
						margin-top: -30px;
					}

						.row.gtr-uniform > * {
							padding-top: 30px;
						}

				.row.gtr-150 {
					margin-top: -45px;
					margin-left: -45px;
				}

					.row.gtr-150 > * {
						padding: 45px 0 0 45px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -45px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 45px;
						}

				.row.gtr-200 {
					margin-top: -60px;
					margin-left: -60px;
				}

					.row.gtr-200 > * {
						padding: 60px 0 0 60px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -60px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 60px;
						}

		}

		@media screen and (max-width: 840px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-narrower {
					order: -1;
				}

				.row > .col-1-narrower {
					width: 8.33333%;
				}

				.row > .off-1-narrower {
					margin-left: 8.33333%;
				}

				.row > .col-2-narrower {
					width: 16.66667%;
				}

				.row > .off-2-narrower {
					margin-left: 16.66667%;
				}

				.row > .col-3-narrower {
					width: 25%;
				}

				.row > .off-3-narrower {
					margin-left: 25%;
				}

				.row > .col-4-narrower {
					width: 33.33333%;
				}

				.row > .off-4-narrower {
					margin-left: 33.33333%;
				}

				.row > .col-5-narrower {
					width: 41.66667%;
				}

				.row > .off-5-narrower {
					margin-left: 41.66667%;
				}

				.row > .col-6-narrower {
					width: 50%;
				}

				.row > .off-6-narrower {
					margin-left: 50%;
				}

				.row > .col-7-narrower {
					width: 58.33333%;
				}

				.row > .off-7-narrower {
					margin-left: 58.33333%;
				}

				.row > .col-8-narrower {
					width: 66.66667%;
				}

				.row > .off-8-narrower {
					margin-left: 66.66667%;
				}

				.row > .col-9-narrower {
					width: 75%;
				}

				.row > .off-9-narrower {
					margin-left: 75%;
				}

				.row > .col-10-narrower {
					width: 83.33333%;
				}

				.row > .off-10-narrower {
					margin-left: 83.33333%;
				}

				.row > .col-11-narrower {
					width: 91.66667%;
				}

				.row > .off-11-narrower {
					margin-left: 91.66667%;
				}

				.row > .col-12-narrower {
					width: 100%;
				}

				.row > .off-12-narrower {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -7.5px;
					margin-left: -7.5px;
				}

					.row.gtr-25 > * {
						padding: 7.5px 0 0 7.5px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -7.5px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 7.5px;
						}

				.row.gtr-50 {
					margin-top: -15px;
					margin-left: -15px;
				}

					.row.gtr-50 > * {
						padding: 15px 0 0 15px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -15px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 15px;
						}

				.row {
					margin-top: -30px;
					margin-left: -30px;
				}

					.row > * {
						padding: 30px 0 0 30px;
					}

					.row.gtr-uniform {
						margin-top: -30px;
					}

						.row.gtr-uniform > * {
							padding-top: 30px;
						}

				.row.gtr-150 {
					margin-top: -45px;
					margin-left: -45px;
				}

					.row.gtr-150 > * {
						padding: 45px 0 0 45px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -45px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 45px;
						}

				.row.gtr-200 {
					margin-top: -60px;
					margin-left: -60px;
				}

					.row.gtr-200 > * {
						padding: 60px 0 0 60px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -60px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 60px;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-mobile {
					order: -1;
				}

				.row > .col-1-mobile {
					width: 8.33333%;
				}

				.row > .off-1-mobile {
					margin-left: 8.33333%;
				}

				.row > .col-2-mobile {
					width: 16.66667%;
				}

				.row > .off-2-mobile {
					margin-left: 16.66667%;
				}

				.row > .col-3-mobile {
					width: 25%;
				}

				.row > .off-3-mobile {
					margin-left: 25%;
				}

				.row > .col-4-mobile {
					width: 33.33333%;
				}

				.row > .off-4-mobile {
					margin-left: 33.33333%;
				}

				.row > .col-5-mobile {
					width: 41.66667%;
				}

				.row > .off-5-mobile {
					margin-left: 41.66667%;
				}

				.row > .col-6-mobile {
					width: 50%;
				}

				.row > .off-6-mobile {
					margin-left: 50%;
				}

				.row > .col-7-mobile {
					width: 58.33333%;
				}

				.row > .off-7-mobile {
					margin-left: 58.33333%;
				}

				.row > .col-8-mobile {
					width: 66.66667%;
				}

				.row > .off-8-mobile {
					margin-left: 66.66667%;
				}

				.row > .col-9-mobile {
					width: 75%;
				}

				.row > .off-9-mobile {
					margin-left: 75%;
				}

				.row > .col-10-mobile {
					width: 83.33333%;
				}

				.row > .off-10-mobile {
					margin-left: 83.33333%;
				}

				.row > .col-11-mobile {
					width: 91.66667%;
				}

				.row > .off-11-mobile {
					margin-left: 91.66667%;
				}

				.row > .col-12-mobile {
					width: 100%;
				}

				.row > .off-12-mobile {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -5px;
					margin-left: -5px;
				}

					.row.gtr-25 > * {
						padding: 5px 0 0 5px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -5px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 5px;
						}

				.row.gtr-50 {
					margin-top: -10px;
					margin-left: -10px;
				}

					.row.gtr-50 > * {
						padding: 10px 0 0 10px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -10px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 10px;
						}

				.row {
					margin-top: -20px;
					margin-left: -20px;
				}

					.row > * {
						padding: 20px 0 0 20px;
					}

					.row.gtr-uniform {
						margin-top: -20px;
					}

						.row.gtr-uniform > * {
							padding-top: 20px;
						}

				.row.gtr-150 {
					margin-top: -30px;
					margin-left: -30px;
				}

					.row.gtr-150 > * {
						padding: 30px 0 0 30px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -30px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 30px;
						}

				.row.gtr-200 {
					margin-top: -40px;
					margin-left: -40px;
				}

					.row.gtr-200 > * {
						padding: 40px 0 0 40px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -40px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 40px;
						}

		}

		@media screen and (max-width: 480px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-mobilep {
					order: -1;
				}

				.row > .col-1-mobilep {
					width: 8.33333%;
				}

				.row > .off-1-mobilep {
					margin-left: 8.33333%;
				}

				.row > .col-2-mobilep {
					width: 16.66667%;
				}

				.row > .off-2-mobilep {
					margin-left: 16.66667%;
				}

				.row > .col-3-mobilep {
					width: 25%;
				}

				.row > .off-3-mobilep {
					margin-left: 25%;
				}

				.row > .col-4-mobilep {
					width: 33.33333%;
				}

				.row > .off-4-mobilep {
					margin-left: 33.33333%;
				}

				.row > .col-5-mobilep {
					width: 41.66667%;
				}

				.row > .off-5-mobilep {
					margin-left: 41.66667%;
				}

				.row > .col-6-mobilep {
					width: 50%;
				}

				.row > .off-6-mobilep {
					margin-left: 50%;
				}

				.row > .col-7-mobilep {
					width: 58.33333%;
				}

				.row > .off-7-mobilep {
					margin-left: 58.33333%;
				}

				.row > .col-8-mobilep {
					width: 66.66667%;
				}

				.row > .off-8-mobilep {
					margin-left: 66.66667%;
				}

				.row > .col-9-mobilep {
					width: 75%;
				}

				.row > .off-9-mobilep {
					margin-left: 75%;
				}

				.row > .col-10-mobilep {
					width: 83.33333%;
				}

				.row > .off-10-mobilep {
					margin-left: 83.33333%;
				}

				.row > .col-11-mobilep {
					width: 91.66667%;
				}

				.row > .off-11-mobilep {
					margin-left: 91.66667%;
				}

				.row > .col-12-mobilep {
					width: 100%;
				}

				.row > .off-12-mobilep {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -5px;
					margin-left: -5px;
				}

					.row.gtr-25 > * {
						padding: 5px 0 0 5px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -5px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 5px;
						}

				.row.gtr-50 {
					margin-top: -10px;
					margin-left: -10px;
				}

					.row.gtr-50 > * {
						padding: 10px 0 0 10px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -10px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 10px;
						}

				.row {
					margin-top: -20px;
					margin-left: -20px;
				}

					.row > * {
						padding: 20px 0 0 20px;
					}

					.row.gtr-uniform {
						margin-top: -20px;
					}

						.row.gtr-uniform > * {
							padding-top: 20px;
						}

				.row.gtr-150 {
					margin-top: -30px;
					margin-left: -30px;
				}

					.row.gtr-150 > * {
						padding: 30px 0 0 30px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -30px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 30px;
						}

				.row.gtr-200 {
					margin-top: -40px;
					margin-left: -40px;
				}

					.row.gtr-200 > * {
						padding: 40px 0 0 40px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -40px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 40px;
						}

		}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header p {
		color: #999;
		font-size: 1.25em;
		position: relative;
		margin-top: -1.25em;
		margin-bottom: 2.25em;
	}

	header.major {
		text-align: center;
		margin: 0 0 2em 0;
	}

		header.major h2 {
			font-size: 2.25em;
		}

		header.major p {
			position: relative;
			border-top: solid 1px #e0e0e0;
			padding: 1em 0 0 0;
			margin: 0;
			top: -1em;
			font-size: 1.5em;
			letter-spacing: -0.025em;
		}

	footer {
		margin: 0 0 3em 0;
	}

		footer > :last-child {
			margin-bottom: 0;
		}

		footer.major {
			padding-top: 3em;
		}

/* Form */

	input[type="text"],
	input[type="password"],
	input[type="email"],
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: border-color 0.2s ease-in-out;
		-webkit-transition: border-color 0.2s ease-in-out;
		-ms-transition: border-color 0.2s ease-in-out;
		transition: border-color 0.2s ease-in-out;
		background: #fff;
		border: solid 1px #e0e0e0;
		border-radius: 5px;
		color: inherit;
		display: block;
		outline: 0;
		padding: 0.75em;
		text-decoration: none;
		width: 100%;
	}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		textarea:focus {
			border-color: #37c0fb;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"] {
		line-height: 1em;
	}

	label {
		display: block;
		color: inherit;
		font-weight: 600;
		line-height: 1.75em;
		margin-bottom: 0.5em;
	}

	::-webkit-input-placeholder {
		color: #999;
		position: relative;
		top: 3px;
	}

	:-moz-placeholder {
		color: #999;
	}

	::-moz-placeholder {
		color: #999;
	}

	:-ms-input-placeholder {
		color: #999;
	}

/* Image */

	.image {
		border: 0;
		display: inline-block;
		position: relative;
		border-radius: 5px;
	}

		.image img {
			display: block;
			border-radius: 5px;
		}

		.image.left {
			display: block;
			float: left;
			margin: 0 2em 2em 0;
			position: relative;
			top: 0.25em;
		}

			.image.left img {
				display: block;
				width: 100%;
			}

		.image.fit {
			display: block;
		}

			.image.fit img {
				display: block;
				width: 100%;
			}

		.image.featured {
			display: block;
			margin: 0 0 2em 0;
		}

			.image.featured img {
				display: block;
				width: 100%;
			}

/* Icon */

	.icon {
		text-decoration: none;
		position: relative;
		text-decoration: none;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 400;
		}

		.icon > .label {
			display: none;
		}

		.icon:before {
			line-height: inherit;
		}

		.icon.solid:before {
			font-weight: 900;
		}

		.icon.brands:before {
			font-family: 'Font Awesome 5 Brands';
		}

		.icon.major {
			text-align: center;
			cursor: default;
			background-color: #37c0fb;
			background-image: -moz-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
			background-image: -webkit-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
			background-image: -ms-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
			background-image: linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
			color: #fff;
			border-radius: 100%;
			display: inline-block;
			width: 5em;
			height: 5em;
			line-height: 5em;
			box-shadow: 0 0 0 7px white, 0 0 0 8px #e0e0e0;
			margin: 0 0 2em 0;
		}

			.icon.major:before {
				font-size: 36px;
			}

/* Lists */

	ol {
		list-style: decimal;
		padding-left: 1.25em;
	}

		ol li {
			padding-left: 0.25em;
		}

	ul {
		list-style: disc;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
		}

/* Links */

	ul.links {
		list-style: none;
		padding-left: 0;
	}

		ul.links li {
			line-height: 2.5em;
			padding-left: 0;
		}

/* Icons */

	ul.icons {
		cursor: default;
		list-style: none;
		padding-left: 0;
	}

		ul.icons li {
			display: inline-block;
			line-height: 1em;
			padding-left: 1.5em;
		}

			ul.icons li:first-child {
				padding-left: 0;
			}

			ul.icons li a, ul.icons li span {
				font-size: 2em;
				border: 0;
			}

/* Menu */

	ul.menu {
		list-style: none;
		padding-left: 0;
	}

		ul.menu li {
			border-left: solid 1px #e0e0e0;
			display: inline-block;
			padding: 0 0 0 1em;
			margin: 0 0 0 1em;
		}

			ul.menu li:first-child {
				border-left: 0;
				margin-left: 0;
				padding-left: 0;
			}

/* Actions */

	ul.actions {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		cursor: default;
		list-style: none;
		margin-left: -1em;
		padding-left: 0;
	}

		ul.actions li {
			padding: 0 0 0 1em;
			vertical-align: middle;
		}

		ul.actions.special {
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 100%;
			margin-left: 0;
		}

			ul.actions.special li:first-child {
				padding-left: 0;
			}

		ul.actions.stacked {
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			margin-left: 0;
		}

			ul.actions.stacked li {
				padding: 1.25em 0 0 0;
			}

				ul.actions.stacked li:first-child {
					padding-top: 0;
				}

		ul.actions.fit {
			width: calc(100% + 1em);
		}

			ul.actions.fit li {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				width: 100%;
			}

				ul.actions.fit li > * {
					width: 100%;
				}

			ul.actions.fit.stacked {
				width: 100%;
			}

		@media screen and (max-width: 736px) {

			ul.actions:not(.fixed) {
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
				margin-left: 0;
				width: 100% !important;
			}

				ul.actions:not(.fixed) li {
					-moz-flex-grow: 1;
					-webkit-flex-grow: 1;
					-ms-flex-grow: 1;
					flex-grow: 1;
					-moz-flex-shrink: 1;
					-webkit-flex-shrink: 1;
					-ms-flex-shrink: 1;
					flex-shrink: 1;
					padding: 1em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions:not(.fixed) li > * {
						width: 100%;
					}

					ul.actions:not(.fixed) li:first-child {
						padding-top: 0;
					}

					ul.actions:not(.fixed) li input[type="submit"],
					ul.actions:not(.fixed) li input[type="reset"],
					ul.actions:not(.fixed) li input[type="button"],
					ul.actions:not(.fixed) li button,
					ul.actions:not(.fixed) li .button {
						width: 100%;
					}

						ul.actions:not(.fixed) li input[type="submit"].icon:before,
						ul.actions:not(.fixed) li input[type="reset"].icon:before,
						ul.actions:not(.fixed) li input[type="button"].icon:before,
						ul.actions:not(.fixed) li button.icon:before,
						ul.actions:not(.fixed) li .button.icon:before {
							margin-left: -0.5em;
						}

		}

/* Tables */

	table {
		width: 100%;
	}

		table.default {
			width: 100%;
		}

			table.default tbody tr {
				border-bottom: solid 1px #e0e0e0;
			}

			table.default td {
				padding: 0.5em 1em 0.5em 1em;
			}

			table.default th {
				font-weight: 600;
				padding: 0.5em 1em 0.5em 1em;
				text-align: left;
			}

			table.default thead {
				background-color: #555555;
				background-image: -moz-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
				background-image: -webkit-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
				background-image: -ms-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
				background-image: linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
				color: #fff;
			}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	button,
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
		background-image: -moz-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
		background-image: -webkit-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
		background-image: -ms-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
		background-image: linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
		background-color: #37c0fb;
		border-radius: 5px;
		border: 0;
		color: #fff;
		cursor: pointer;
		display: inline-block;
		padding: 0 1.5em;
		line-height: 2.75em;
		min-width: 9em;
		text-align: center;
		text-decoration: none;
		font-weight: 600;
		letter-spacing: -0.025em;
	}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		button:hover,
		.button:hover {
			background-color: #50c8fc;
			color: #fff !important;
		}

		input[type="submit"]:active,
		input[type="reset"]:active,
		input[type="button"]:active,
		button:active,
		.button:active {
			background-color: #1eb8fb;
			color: #fff;
		}

		input[type="submit"].alt,
		input[type="reset"].alt,
		input[type="button"].alt,
		button.alt,
		.button.alt {
			background-color: #555555;
			color: #fff;
		}

			input[type="submit"].alt:hover,
			input[type="reset"].alt:hover,
			input[type="button"].alt:hover,
			button.alt:hover,
			.button.alt:hover {
				background-color: #626262;
			}

			input[type="submit"].alt:active,
			input[type="reset"].alt:active,
			input[type="button"].alt:active,
			button.alt:active,
			.button.alt:active {
				background-color: #484848;
			}

		input[type="submit"].icon:before,
		input[type="reset"].icon:before,
		input[type="button"].icon:before,
		button.icon:before,
		.button.icon:before {
			margin-right: 0.5em;
		}

		input[type="submit"].fit,
		input[type="reset"].fit,
		input[type="button"].fit,
		button.fit,
		.button.fit {
			width: 100%;
		}

		input[type="submit"].small,
		input[type="reset"].small,
		input[type="button"].small,
		button.small,
		.button.small {
			font-size: 0.8em;
		}

/* Box */

	.box.highlight {
		text-align: center;
	}

	.box.post {
		position: relative;
		margin: 0 0 2em 0;
	}

		.box.post:after {
			content: '';
			display: block;
			clear: both;
		}

		.box.post .inner {
			margin-left: calc(30% + 2em);
		}

			.box.post .inner > :last-child {
				margin-bottom: 0;
			}

		.box.post .image {
			width: 30%;
			margin: 0;
		}

/* Header */

	#header {
		text-align: center;
		padding: 3em 0 0 0;
		background-color: #fff;
		background-image: url("ambient.png"), url("images/bg02.png"), url("images/bg01.png");
		background-position: top left,					top left,					top left;
		background-size: 100% 6em,					100% 6em,					auto;
		background-repeat: no-repeat,					no-repeat,					repeat;
	}

		#header h1 {
			padding: 0 0 2.75em 0;
			margin: 0;
		}

			#header h1 a {
				font-size: 1.5em;
				letter-spacing: -0.025em;
				border: 0;
			}

	#nav {
		cursor: default;
		background-color: #333;
		background-image: -moz-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.3)), url("images/bg01.png");
		background-image: -webkit-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.3)), url("images/bg01.png");
		background-image: -ms-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.3)), url("images/bg01.png");
		background-image: linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.3)), url("images/bg01.png");
		padding: 0;
	}

		#nav:after {
			content: '';
			display: block;
			width: 100%;
			height: 0.75em;
			background-color: #37c0fb;
			background-image: url("images/bg01.png");
		}

		#nav > ul {
			margin: 0;
		}

			#nav > ul > li {
				position: relative;
				display: inline-block;
				margin-left: 1em;
			}

				#nav > ul > li a {
					color: #c0c0c0;
					text-decoration: none;
					border: 0;
					display: block;
					padding: 1.5em 0.5em 1.35em 0.5em;
				}

				#nav > ul > li:first-child {
					margin-left: 0;
				}

				#nav > ul > li:hover a {
					color: #fff;
				}

				#nav > ul > li.current {
					font-weight: 600;
				}

					#nav > ul > li.current:before {
						-moz-transform: rotateZ(45deg);
						-webkit-transform: rotateZ(45deg);
						-ms-transform: rotateZ(45deg);
						transform: rotateZ(45deg);
						width: 0.75em;
						height: 0.75em;
						content: '';
						display: block;
						position: absolute;
						bottom: -0.5em;
						left: 50%;
						margin-left: -0.375em;
						background-color: #37c0fb;
						background-image: url("images/bg01.png");
					}

					#nav > ul > li.current a {
						color: #fff;
					}

				#nav > ul > li.active a {
					color: #fff;
				}

				#nav > ul > li.active.current:before {
					opacity: 0;
				}

				#nav > ul > li > ul {
					display: none;
				}

/* Dropotron */

	.dropotron {
		background-image: -moz-linear-gradient(top, rgba(0,0,0,0.3), rgba(0,0,0,0)), url("images/bg01.png");
		background-image: -webkit-linear-gradient(top, rgba(0,0,0,0.3), rgba(0,0,0,0)), url("images/bg01.png");
		background-image: -ms-linear-gradient(top, rgba(0,0,0,0.3), rgba(0,0,0,0)), url("images/bg01.png");
		background-image: linear-gradient(top, rgba(0,0,0,0.3), rgba(0,0,0,0)), url("images/bg01.png");
		background-color: #333;
		border-radius: 5px;
		color: #fff;
		min-width: 10em;
		padding: 1em 0;
		text-align: center;
		box-shadow: 0 1em 1em 0 rgba(0, 0, 0, 0.5);
		list-style: none;
	}

		.dropotron > li {
			line-height: 2em;
			padding: 0 1.1em 0 1em;
		}

			.dropotron > li > a {
				color: #c0c0c0;
				text-decoration: none;
				border: 0;
			}

			.dropotron > li.active > a, .dropotron > li:hover > a {
				color: #fff;
			}

		.dropotron.level-0 {
			border-radius: 0 0 5px 5px;
			font-size: 0.9em;
			padding-top: 0;
			margin-top: -1px;
		}

/* Banner */

	#banner {
		background-image: url("../../images/banner.jpg");
		background-position: center center;
		background-size: cover;
		height: 28em;
		text-align: center;
		position: relative;
	}

		#banner header {
			position: absolute;
			bottom: 0;
			left: 0;
			width: 100%;
			background: #212121;
			background: rgba(27, 27, 27, 0.75);
			color: #fff;
			padding: 1.5em 0;
		}

			#banner header h2 {
				display: inline-block;
				margin: 0;
				font-size: 1.25em;
				vertical-align: middle;
			}

				#banner header h2 em {
					opacity: 0.75;
				}

				#banner header h2 a {
					border-bottom-color: rgba(255, 255, 255, 0.5);
				}

					#banner header h2 a:hover {
						border-bottom-color: transparent;
					}

			#banner header .button {
				vertical-align: middle;
				margin-left: 1em;
			}

/* Wrapper */

	.wrapper {
		padding: 5em 0 3em 0;
	}

		.wrapper.style1 {
			background: #fff;
		}

		.wrapper.style2 {
			background-color: #fff;
			background-image: url("images/bg02.png"), url("images/bg03.png"), url("images/bg01.png");
			background-position: top left,						bottom left,					top left;
			background-size: 100% 6em,						100% 6em,						auto;
			background-repeat: no-repeat,						no-repeat,						repeat;
		}

		.wrapper.style3 {
			background-color: #37c0fb;
			background-image: -moz-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
			background-image: -webkit-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
			background-image: -ms-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
			background-image: linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.15)), url("images/bg01.png");
			color: #fff;
		}

			.wrapper.style3 .button {
				background: #fff;
				color: #474747;
			}

				.wrapper.style3 .button:hover {
					color: #37c0fb !important;
				}

/* CTA */

	#cta {
		text-align: center;
		padding: 3.5em 0;
	}

		#cta header h2 {
			display: inline-block;
			vertical-align: middle;
			margin: 0;
		}

		#cta header .button {
			vertical-align: middle;
			margin-left: 1em;
		}

/* Footer */

	#footer {
		padding: 4em 0 8em 0;
	}

		#footer a {
			color: inherit;
			border-bottom-color: rgba(71, 71, 71, 0.25);
		}

			#footer a:hover {
				color: #37c0fb;
				border-bottom-color: transparent;
			}

		#footer .container {
			margin-bottom: 4em;
		}

		#footer .icons {
			text-align: center;
			margin: 0;
		}

			#footer .icons a {
				color: #999;
			}

				#footer .icons a:hover {
					color: #474747;
				}

		#footer .copyright {
			color: #999;
			margin-top: 1.5em;
			text-align: center;
			font-size: 0.9em;
		}

/* Wide */

	@media screen and (max-width: 1680px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 14pt;
				line-height: 1.5em;
			}

		/* Banner */

			#banner {
				height: 24em;
			}

	}

/* Normal */

	@media screen and (max-width: 1280px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 13pt;
				line-height: 1.5em;
			}

		/* Lists */

			ol {
				padding-left: 1.25em;
			}

				ol li {
					padding-left: 0.25em;
				}

		/* Icons */

			ul.icons li a, ul.icons li span {
				font-size: 1.5em;
			}

		/* Header */

			#header {
				padding: 2em 0 0 0;
			}

				#header h1 {
					padding: 0 0 1.75em 0;
				}

		/* Banner */

			#banner {
				height: 20em;
			}

		/* Wrapper */

			.wrapper {
				padding: 3em 0 1em 0;
			}

		/* CTA */

			#cta {
				padding: 2em 0;
			}

		/* Footer */

			#footer {
				padding: 3em 0 3em 0;
			}

				#footer .container {
					margin-bottom: 1em;
				}

	}

/* Narrow */

	@media screen and (max-width: 980px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 12pt;
				line-height: 1.5em;
			}

	}

/* Narrower */

	#navPanel, #titleBar {
		display: none;
	}

	@media screen and (max-width: 840px) {

		/* Basic */

			html, body {
				overflow-x: hidden;
			}

			body, input, select, textarea {
				font-size: 13pt;
			}

			h1, h2, h3, h4, h5, h6 {
				margin-bottom: 0.5em;
			}

			header p {
				margin-top: -0.75em;
			}

			header.major {
				text-align: center;
				margin: 0 0 2em 0;
			}

				header.major h2 {
					font-size: 1.75em;
				}

				header.major p {
					top: -0.25em;
					font-size: 1.25em;
				}

		/* Box */

			.box.highlight {
				text-align: left;
				position: relative;
				padding-left: 7em;
			}

				.box.highlight i {
					position: absolute;
					margin: 0;
					left: 0;
					top: 0.25em;
				}

			.box.post .inner {
				margin-left: calc(20% + 2em);
			}

			.box.post .image {
				width: 20%;
			}

		/* Header */

			#header {
				display: none;
			}

		/* Banner */

			#banner {
				height: 20em;
			}

				#banner header h2 {
					display: block;
				}

				#banner header .button {
					margin: 1em 0 0 0;
				}

		/* CTA */

			#cta {
				padding: 1.5em 0;
			}

				#cta header h2 {
					display: block;
				}

				#cta header .button {
					margin: 1em 0 0 0;
				}

		/* Footer */

			#footer {
				text-align: center;
			}

				#footer .container {
					margin-bottom: 4em;
				}

				#footer form .actions {
					-moz-justify-content: center;
					-webkit-justify-content: center;
					-ms-justify-content: center;
					justify-content: center;
					width: 100%;
					margin-left: 0;
				}

					#footer form .actions li:first-child {
						padding-left: 0;
					}

		/* Nav */

			#page-wrapper {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				padding-bottom: 1px;
				padding-top: 44px;
			}

			#titleBar {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 44px;
				left: 0;
				position: fixed;
				top: 0;
				width: 100%;
				z-index: 10001;
				background-color: #333;
				background-image: -moz-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.3)), url("images/bg01.png");
				background-image: -webkit-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.3)), url("images/bg01.png");
				background-image: -ms-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.3)), url("images/bg01.png");
				background-image: linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.3)), url("images/bg01.png");
				height: 44px;
				line-height: 44px;
				box-shadow: 0 4px 0 0 #37c0fb;
			}

				#titleBar .title {
					display: block;
					position: relative;
					font-weight: 600;
					text-align: center;
					color: #fff;
					z-index: 1;
				}

					#titleBar .title em {
						font-style: normal;
						font-weight: 300;
					}

				#titleBar .toggle {
					text-decoration: none;
					border: 0;
					height: 60px;
					left: 0;
					position: absolute;
					top: 0;
					width: 80px;
					z-index: 2;
				}

					#titleBar .toggle:before {
						-moz-osx-font-smoothing: grayscale;
						-webkit-font-smoothing: antialiased;
						display: inline-block;
						font-style: normal;
						font-variant: normal;
						text-rendering: auto;
						line-height: 1;
						text-transform: none !important;
						font-family: 'Font Awesome 5 Free';
						font-weight: 900;
					}

					#titleBar .toggle:before {
						content: '\\f0c9';
						display: block;
						height: 44px;
						line-height: inherit;
						text-align: center;
						width: 44px;
						color: #fff;
						opacity: 0.5;
					}

					#titleBar .toggle:active:before {
						opacity: 0.75;
					}

			#navPanel {
				background-color: #1f1f1f;
				box-shadow: inset -1px 0 3px 0 rgba(0, 0, 0, 0.5);
				background-image: -moz-linear-gradient(left, rgba(0,0,0,0) 75%, rgba(0,0,0,0.15)), url("images/bg01.png");
				background-image: -webkit-linear-gradient(left, rgba(0,0,0,0) 75%, rgba(0,0,0,0.15)), url("images/bg01.png");
				background-image: -ms-linear-gradient(left, rgba(0,0,0,0) 75%, rgba(0,0,0,0.15)), url("images/bg01.png");
				background-image: linear-gradient(left, rgba(0,0,0,0) 75%, rgba(0,0,0,0.15)), url("images/bg01.png");
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transform: translateX(-275px);
				-webkit-transform: translateX(-275px);
				-ms-transform: translateX(-275px);
				transform: translateX(-275px);
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 100%;
				left: 0;
				overflow-y: auto;
				position: fixed;
				top: 0;
				width: 275px;
				z-index: 10002;
			}

				#navPanel .link {
					border-bottom: 0;
					border-top: solid 1px rgba(255, 255, 255, 0.05);
					color: #888;
					display: block;
					height: 48px;
					line-height: 48px;
					padding: 0 1em 0 1em;
					text-decoration: none;
				}

					#navPanel .link:first-child {
						border-top: 0;
					}

					#navPanel .link.depth-0 {
						color: #fff;
					}

					#navPanel .link .indent-1 {
						display: inline-block;
						width: 1em;
					}

					#navPanel .link .indent-2 {
						display: inline-block;
						width: 2em;
					}

					#navPanel .link .indent-3 {
						display: inline-block;
						width: 3em;
					}

					#navPanel .link .indent-4 {
						display: inline-block;
						width: 4em;
					}

					#navPanel .link .indent-5 {
						display: inline-block;
						width: 5em;
					}

			body.navPanel-visible #page-wrapper {
				-moz-transform: translateX(275px);
				-webkit-transform: translateX(275px);
				-ms-transform: translateX(275px);
				transform: translateX(275px);
			}

			body.navPanel-visible #titleBar {
				-moz-transform: translateX(275px);
				-webkit-transform: translateX(275px);
				-ms-transform: translateX(275px);
				transform: translateX(275px);
			}

			body.navPanel-visible #navPanel {
				-moz-transform: translateX(0);
				-webkit-transform: translateX(0);
				-ms-transform: translateX(0);
				transform: translateX(0);
			}

	}

/* Mobile */

	@media screen and (max-width: 736px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 11pt;
				line-height: 1.35em;
			}

			h2 {
				font-size: 1.25em;
				letter-spacing: 0;
				line-height: 1.35em;
			}

			h3 {
				font-size: 1em;
				letter-spacing: 0;
				line-height: 1.35em;
			}

			header p {
				margin-top: -0.5em;
				font-size: 1em;
			}

			header.major {
				padding: 0 20px;
			}

				header.major h2 {
					font-size: 1.25em;
				}

				header.major p {
					top: 0;
					margin-top: 1.25em;
					font-size: 1em;
				}

		/* Menu */

			ul.menu li {
				border: 0;
				padding: 0;
				margin: 0;
				display: block;
				line-height: 2em;
			}

		/* Banner */

			#banner {
				height: 18em;
			}

		/* Wrapper */

			.wrapper {
				padding: 2em 0 1px 0;
			}

	}

/* Mobile (Portrait) */

	@media screen and (max-width: 480px) {

		/* Icon */

			.icon.major {
				width: 4em;
				height: 4em;
				line-height: 4em;
				box-shadow: 0 0 0 7px white, 0 0 0 8px #e0e0e0;
			}

				.icon.major:before {
					font-size: 24px;
				}

		/* Button */

			input[type="submit"],
			input[type="reset"],
			input[type="button"],
			button,
			.button {
				width: 100%;
				display: block;
			}

		/* Box */

			.box.highlight {
				padding-left: calc(4em + 30px);
			}

			.box.post .inner {
				margin-left: calc(30% + 20px);
			}

			.box.post .image {
				width: 30%;
			}

		/* Banner */

			#banner {
				height: 20em;
			}

				#banner header {
					padding: 20px;
				}

		/* Wrapper */

			.wrapper {
				padding: 2em 20px 1px 20px;
			}

		/* CTA */

			#cta {
				padding: 20px;
			}

		/* Footer */

			#footer {
				padding: 2em 20px;
				text-align: left;
			}

	}"""
, "elegant":"""
table thead {
	background: #000000;
	color: #173B45;
	font-weight: 400;
	text-transform: uppercase;
	border: 0;
	box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
	font-size: 0.85em;
	letter-spacing: 2px;
}
input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #ed786a;
		color: #173B45 !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #173B45;
	}
	#header {
		background: #173B45;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #173B45, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #173B45;
			}
			.dropotron {
				background: #173B45;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #173B45;
			}
			#features {
				background: #173B45;
			}
			
	#banner {
		background: #173B45;
		color: #173B45;
	}
	
	#main {
		background: #173B45;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #173B45, inset 0px 10px 0px 0px #e5e5e5;
	}
	
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #173B45, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #173B45;
	}
	#navPanel .link.depth-0 {
		color: #173B45;
	}
	
	#navPanel .depth-0 {
		color: #173B45;
	}
	
	#navPanel .link
	{
		color: #fff;
	}
	#content section
	{
		background : #58075b;
	}
	#content{
		
	background : #fff;
	
	}
	h1, h2, h3, h4{
		color:white;
	}""", 
	"lime":"""input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #ed786a;
		color: #387F39 !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #387F39;
	}
	#header {
		background: #387F39;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #387F39, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #387F39;
			}
			.dropotron {
				background: #387F39;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #387F39;
			}
			#features {
				background: #387F39;
			}
			
	#banner {
		background: #387F39;
		color: #387F39;
	}
	
	#main {
		background: #387F39;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #387F39, inset 0px 10px 0px 0px #e5e5e5;
	}
	
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #387F39, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #387F39;
	}
	#navPanel .link.depth-0 {
		color: #387F39;
	}
	
	#navPanel .depth-0 {
		color: #387F39;
	}
	
	#navPanel .link
	{
		color: #fff;
	}
	#content section
	{
		background : #58075b;
	}
	#content{
		
	background : #fff;
	
	}
	h1, h2, h3, h4{
		color:white;
	}""", 
	"phantom":"""
table thead {
	background: #000000;
	color: #522258;
	font-weight: 400;
	text-transform: uppercase;
	border: 0;
	box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
	font-size: 0.85em;
	letter-spacing: 2px;
}
input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #ed786a;
		color: #522258 !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #522258;
	}
	#header {
		background: #522258;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #522258, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #522258;
			}
			.dropotron {
				background: #522258;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #522258;
			}
			#features {
				background: #522258;
			}
			
	#banner {
		background: #522258;
		color: #522258;
	}
	
	#main {
		background: #522258;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #522258, inset 0px 10px 0px 0px #e5e5e5;
	}
	
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #522258, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #522258;
	}
	#navPanel .link.depth-0 {
		color: #522258;
	}
	
	#navPanel .depth-0 {
		color: #522258;
	}
	
	#navPanel .link
	{
		color: #fff;
	}
	#content section
	{
		background : #58075b;
	}
	#content{
		
	background : #fff;
	
	}
	h1, h2, h3, h4{
		color:white;
	}""","sakura":"""table thead {
	background: #000000;
	color: #ea24b8;
	font-weight: 400;
	text-transform: uppercase;
	border: 0;
	box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
	font-size: 0.85em;
	letter-spacing: 2px;
}
input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #ed786a;
		color: #ea24b8 !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #ea24b8;
	}
	#header {
		background: #ea24b8;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #ea24b8, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #ea24b8;
			}
			.dropotron {
				background: #ea24b8;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #ea24b8;
			}
			#features {
				background: #ea24b8;
			}
			
	#banner {
		background: #ea24b8;
		color: #ea24b8;
	}
	
	#main {
		background: #ea24b8;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #ea24b8, inset 0px 10px 0px 0px #e5e5e5;
	}
	
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #ea24b8, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #ea24b8;
	}
	#navPanel .link.depth-0 {
		color: #ea24b8;
	}
	
	#navPanel .depth-0 {
		color: #ea24b8;
	}
	
	#navPanel .link
	{
		color: #fff;
	}
	#content section
	{
		background : #58075b;
	}
	#content{
		
	background : #fff;
	
	}
	h1, h2, h3, h4{
		color:white;
	}""" , 
	"valley":"""input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #ed786a;
		color: #6d7617 !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #6d7617;
	}
	#header {
		background: #6d7617;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #6d7617, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #6d7617;
			}
			.dropotron {
				background: #6d7617;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #6d7617;
			}
			#features {
				background: #6d7617;
			}
			
	#banner {
		background: #6d7617;
		color: #6d7617;
	}
	
	#main {
		background: #6d7617;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #6d7617, inset 0px 10px 0px 0px #e5e5e5;
	}
	
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #6d7617, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #6d7617;
	}
	#navPanel .link.depth-0 {
		color: #6d7617;
	}
	
	#navPanel .depth-0 {
		color: #6d7617;
	}
	
	#navPanel .link
	{
		color: #fff;
	}
	#content section
	{
		background : #58075b;
	}
	#content{
		
	background : #fff;
	
	}
	h1, h2, h3, h4{
		color:white;
	}"""
	}, 
"hycuna":
{
	"default":"""@import url("https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz:400,300,200");

/*
	Halcyonic by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #D4D9DD url("ambient.jpg");
		color: #474f51;
		font-size: 13.5pt;
		font-family: 'Yanone Kaffeesatz';
		line-height: 1.85em;
		font-weight: 300;
	}

	input, textarea, select {
		color: #474f51;
		font-size: 13.5pt;
		font-family: 'Yanone Kaffeesatz';
		line-height: 1.85em;
		font-weight: 300;
	}

	ul, ol, p, dl {
		margin: 0 0 2em 0;
	}

	a {
		text-decoration: underline;
	}

		a:hover {
			text-decoration: none;
		}

	section > :last-child,
	section:last-child,
	.last-child {
		margin-bottom: 0 !important;
	}

/* Container */

	.container {
		margin: 0 auto;
		max-width: 100%;
		width: 1200px;
	}

		@media screen and (max-width: 1680px) {

			.container {
				width: 1200px;
			}

		}

		@media screen and (max-width: 1280px) {

			.container {
				width: calc(100% - 40px);
			}

		}

		@media screen and (max-width: 980px) {

			.container {
				width: calc(100% - 50px);
			}

		}

		@media screen and (max-width: 736px) {

			.container {
				width: calc(100% - 40px);
			}

		}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0px;
			margin-left: 0px;
		}

			.row.gtr-0 > * {
				padding: 0px 0 0 0px;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0px;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0px;
				}

		.row.gtr-25 {
			margin-top: -6.25px;
			margin-left: -6.25px;
		}

			.row.gtr-25 > * {
				padding: 6.25px 0 0 6.25px;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -6.25px;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 6.25px;
				}

		.row.gtr-50 {
			margin-top: -12.5px;
			margin-left: -12.5px;
		}

			.row.gtr-50 > * {
				padding: 12.5px 0 0 12.5px;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -12.5px;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 12.5px;
				}

		.row {
			margin-top: -25px;
			margin-left: -25px;
		}

			.row > * {
				padding: 25px 0 0 25px;
			}

			.row.gtr-uniform {
				margin-top: -25px;
			}

				.row.gtr-uniform > * {
					padding-top: 25px;
				}

		.row.gtr-150 {
			margin-top: -37.5px;
			margin-left: -37.5px;
		}

			.row.gtr-150 > * {
				padding: 37.5px 0 0 37.5px;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -37.5px;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 37.5px;
				}

		.row.gtr-200 {
			margin-top: -50px;
			margin-left: -50px;
		}

			.row.gtr-200 > * {
				padding: 50px 0 0 50px;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -50px;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 50px;
				}

		@media screen and (max-width: 1680px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xlarge {
					order: -1;
				}

				.row > .col-1-xlarge {
					width: 8.33333%;
				}

				.row > .off-1-xlarge {
					margin-left: 8.33333%;
				}

				.row > .col-2-xlarge {
					width: 16.66667%;
				}

				.row > .off-2-xlarge {
					margin-left: 16.66667%;
				}

				.row > .col-3-xlarge {
					width: 25%;
				}

				.row > .off-3-xlarge {
					margin-left: 25%;
				}

				.row > .col-4-xlarge {
					width: 33.33333%;
				}

				.row > .off-4-xlarge {
					margin-left: 33.33333%;
				}

				.row > .col-5-xlarge {
					width: 41.66667%;
				}

				.row > .off-5-xlarge {
					margin-left: 41.66667%;
				}

				.row > .col-6-xlarge {
					width: 50%;
				}

				.row > .off-6-xlarge {
					margin-left: 50%;
				}

				.row > .col-7-xlarge {
					width: 58.33333%;
				}

				.row > .off-7-xlarge {
					margin-left: 58.33333%;
				}

				.row > .col-8-xlarge {
					width: 66.66667%;
				}

				.row > .off-8-xlarge {
					margin-left: 66.66667%;
				}

				.row > .col-9-xlarge {
					width: 75%;
				}

				.row > .off-9-xlarge {
					margin-left: 75%;
				}

				.row > .col-10-xlarge {
					width: 83.33333%;
				}

				.row > .off-10-xlarge {
					margin-left: 83.33333%;
				}

				.row > .col-11-xlarge {
					width: 91.66667%;
				}

				.row > .off-11-xlarge {
					margin-left: 91.66667%;
				}

				.row > .col-12-xlarge {
					width: 100%;
				}

				.row > .off-12-xlarge {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -6.25px;
					margin-left: -6.25px;
				}

					.row.gtr-25 > * {
						padding: 6.25px 0 0 6.25px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -6.25px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 6.25px;
						}

				.row.gtr-50 {
					margin-top: -12.5px;
					margin-left: -12.5px;
				}

					.row.gtr-50 > * {
						padding: 12.5px 0 0 12.5px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -12.5px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 12.5px;
						}

				.row {
					margin-top: -25px;
					margin-left: -25px;
				}

					.row > * {
						padding: 25px 0 0 25px;
					}

					.row.gtr-uniform {
						margin-top: -25px;
					}

						.row.gtr-uniform > * {
							padding-top: 25px;
						}

				.row.gtr-150 {
					margin-top: -37.5px;
					margin-left: -37.5px;
				}

					.row.gtr-150 > * {
						padding: 37.5px 0 0 37.5px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -37.5px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 37.5px;
						}

				.row.gtr-200 {
					margin-top: -50px;
					margin-left: -50px;
				}

					.row.gtr-200 > * {
						padding: 50px 0 0 50px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -50px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 50px;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-large {
					order: -1;
				}

				.row > .col-1-large {
					width: 8.33333%;
				}

				.row > .off-1-large {
					margin-left: 8.33333%;
				}

				.row > .col-2-large {
					width: 16.66667%;
				}

				.row > .off-2-large {
					margin-left: 16.66667%;
				}

				.row > .col-3-large {
					width: 25%;
				}

				.row > .off-3-large {
					margin-left: 25%;
				}

				.row > .col-4-large {
					width: 33.33333%;
				}

				.row > .off-4-large {
					margin-left: 33.33333%;
				}

				.row > .col-5-large {
					width: 41.66667%;
				}

				.row > .off-5-large {
					margin-left: 41.66667%;
				}

				.row > .col-6-large {
					width: 50%;
				}

				.row > .off-6-large {
					margin-left: 50%;
				}

				.row > .col-7-large {
					width: 58.33333%;
				}

				.row > .off-7-large {
					margin-left: 58.33333%;
				}

				.row > .col-8-large {
					width: 66.66667%;
				}

				.row > .off-8-large {
					margin-left: 66.66667%;
				}

				.row > .col-9-large {
					width: 75%;
				}

				.row > .off-9-large {
					margin-left: 75%;
				}

				.row > .col-10-large {
					width: 83.33333%;
				}

				.row > .off-10-large {
					margin-left: 83.33333%;
				}

				.row > .col-11-large {
					width: 91.66667%;
				}

				.row > .off-11-large {
					margin-left: 91.66667%;
				}

				.row > .col-12-large {
					width: 100%;
				}

				.row > .off-12-large {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -5px;
					margin-left: -5px;
				}

					.row.gtr-25 > * {
						padding: 5px 0 0 5px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -5px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 5px;
						}

				.row.gtr-50 {
					margin-top: -10px;
					margin-left: -10px;
				}

					.row.gtr-50 > * {
						padding: 10px 0 0 10px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -10px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 10px;
						}

				.row {
					margin-top: -20px;
					margin-left: -20px;
				}

					.row > * {
						padding: 20px 0 0 20px;
					}

					.row.gtr-uniform {
						margin-top: -20px;
					}

						.row.gtr-uniform > * {
							padding-top: 20px;
						}

				.row.gtr-150 {
					margin-top: -30px;
					margin-left: -30px;
				}

					.row.gtr-150 > * {
						padding: 30px 0 0 30px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -30px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 30px;
						}

				.row.gtr-200 {
					margin-top: -40px;
					margin-left: -40px;
				}

					.row.gtr-200 > * {
						padding: 40px 0 0 40px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -40px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 40px;
						}

		}

		@media screen and (max-width: 980px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-medium {
					order: -1;
				}

				.row > .col-1-medium {
					width: 8.33333%;
				}

				.row > .off-1-medium {
					margin-left: 8.33333%;
				}

				.row > .col-2-medium {
					width: 16.66667%;
				}

				.row > .off-2-medium {
					margin-left: 16.66667%;
				}

				.row > .col-3-medium {
					width: 25%;
				}

				.row > .off-3-medium {
					margin-left: 25%;
				}

				.row > .col-4-medium {
					width: 33.33333%;
				}

				.row > .off-4-medium {
					margin-left: 33.33333%;
				}

				.row > .col-5-medium {
					width: 41.66667%;
				}

				.row > .off-5-medium {
					margin-left: 41.66667%;
				}

				.row > .col-6-medium {
					width: 50%;
				}

				.row > .off-6-medium {
					margin-left: 50%;
				}

				.row > .col-7-medium {
					width: 58.33333%;
				}

				.row > .off-7-medium {
					margin-left: 58.33333%;
				}

				.row > .col-8-medium {
					width: 66.66667%;
				}

				.row > .off-8-medium {
					margin-left: 66.66667%;
				}

				.row > .col-9-medium {
					width: 75%;
				}

				.row > .off-9-medium {
					margin-left: 75%;
				}

				.row > .col-10-medium {
					width: 83.33333%;
				}

				.row > .off-10-medium {
					margin-left: 83.33333%;
				}

				.row > .col-11-medium {
					width: 91.66667%;
				}

				.row > .off-11-medium {
					margin-left: 91.66667%;
				}

				.row > .col-12-medium {
					width: 100%;
				}

				.row > .off-12-medium {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -6.25px;
					margin-left: -6.25px;
				}

					.row.gtr-25 > * {
						padding: 6.25px 0 0 6.25px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -6.25px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 6.25px;
						}

				.row.gtr-50 {
					margin-top: -12.5px;
					margin-left: -12.5px;
				}

					.row.gtr-50 > * {
						padding: 12.5px 0 0 12.5px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -12.5px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 12.5px;
						}

				.row {
					margin-top: -25px;
					margin-left: -25px;
				}

					.row > * {
						padding: 25px 0 0 25px;
					}

					.row.gtr-uniform {
						margin-top: -25px;
					}

						.row.gtr-uniform > * {
							padding-top: 25px;
						}

				.row.gtr-150 {
					margin-top: -37.5px;
					margin-left: -37.5px;
				}

					.row.gtr-150 > * {
						padding: 37.5px 0 0 37.5px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -37.5px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 37.5px;
						}

				.row.gtr-200 {
					margin-top: -50px;
					margin-left: -50px;
				}

					.row.gtr-200 > * {
						padding: 50px 0 0 50px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -50px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 50px;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-small {
					order: -1;
				}

				.row > .col-1-small {
					width: 8.33333%;
				}

				.row > .off-1-small {
					margin-left: 8.33333%;
				}

				.row > .col-2-small {
					width: 16.66667%;
				}

				.row > .off-2-small {
					margin-left: 16.66667%;
				}

				.row > .col-3-small {
					width: 25%;
				}

				.row > .off-3-small {
					margin-left: 25%;
				}

				.row > .col-4-small {
					width: 33.33333%;
				}

				.row > .off-4-small {
					margin-left: 33.33333%;
				}

				.row > .col-5-small {
					width: 41.66667%;
				}

				.row > .off-5-small {
					margin-left: 41.66667%;
				}

				.row > .col-6-small {
					width: 50%;
				}

				.row > .off-6-small {
					margin-left: 50%;
				}

				.row > .col-7-small {
					width: 58.33333%;
				}

				.row > .off-7-small {
					margin-left: 58.33333%;
				}

				.row > .col-8-small {
					width: 66.66667%;
				}

				.row > .off-8-small {
					margin-left: 66.66667%;
				}

				.row > .col-9-small {
					width: 75%;
				}

				.row > .off-9-small {
					margin-left: 75%;
				}

				.row > .col-10-small {
					width: 83.33333%;
				}

				.row > .off-10-small {
					margin-left: 83.33333%;
				}

				.row > .col-11-small {
					width: 91.66667%;
				}

				.row > .off-11-small {
					margin-left: 91.66667%;
				}

				.row > .col-12-small {
					width: 100%;
				}

				.row > .off-12-small {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -5px;
					margin-left: -5px;
				}

					.row.gtr-25 > * {
						padding: 5px 0 0 5px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -5px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 5px;
						}

				.row.gtr-50 {
					margin-top: -10px;
					margin-left: -10px;
				}

					.row.gtr-50 > * {
						padding: 10px 0 0 10px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -10px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 10px;
						}

				.row {
					margin-top: -20px;
					margin-left: -20px;
				}

					.row > * {
						padding: 20px 0 0 20px;
					}

					.row.gtr-uniform {
						margin-top: -20px;
					}

						.row.gtr-uniform > * {
							padding-top: 20px;
						}

				.row.gtr-150 {
					margin-top: -30px;
					margin-left: -30px;
				}

					.row.gtr-150 > * {
						padding: 30px 0 0 30px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -30px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 30px;
						}

				.row.gtr-200 {
					margin-top: -40px;
					margin-left: -40px;
				}

					.row.gtr-200 > * {
						padding: 40px 0 0 40px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -40px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 40px;
						}

		}

/* Multi-use */

	.link-list li {
		padding: 0.2em 0 0.2em 0;
	}

		.link-list li:first-child {
			padding-top: 0 !important;
			border-top: 0 !important;
		}

		.link-list li:last-child {
			padding-bottom: 0 !important;
			border-bottom: 0 !important;
		}

	.quote-list li {
		padding: 1em 0 1em 0;
		overflow: hidden;
	}

		.quote-list li:first-child {
			padding-top: 0 !important;
			border-top: 0 !important;
		}

		.quote-list li:last-child {
			padding-bottom: 0 !important;
			border-bottom: 0 !important;
		}

		.quote-list li img {
			float: left;
		}

		.quote-list li p {
			margin: 0 0 0 90px;
			font-size: 1.2em;
			font-style: italic;
		}

		.quote-list li span {
			display: block;
			margin-left: 90px;
			font-size: 0.9em;
			font-weight: 400;
		}

	.check-list li {
		padding: 0.7em 0 0.7em 45px;
		font-size: 1.2em;
		background: url("images/icon-checkmark.png") 0px 1.05em no-repeat;
	}

		.check-list li:first-child {
			padding-top: 0 !important;
			border-top: 0 !important;
			background-position: 0 0.3em;
		}

		.check-list li:last-child {
			padding-bottom: 0 !important;
			border-bottom: 0 !important;
		}

	.feature-image {
		display: block;
		margin: 0 0 2em 0;
		outline: 0;
	}

		.feature-image img {
			display: block;
			width: 100%;
		}

	.bordered-feature-image {
		display: block;
		background: #fff url("blog_image_3.png");
		padding: 10px;
		box-shadow: 3px 3px 3px 1px rgba(0, 0, 0, 0.15);
		margin: 0 0 1.5em 0;
		outline: 0;
	}

		.bordered-feature-image img {
			display: block;
			width: 100%;
		}

	.button-large {
		background-image: -moz-linear-gradient(top, #ed391b, #ce1a00);
		background-image: -webkit-linear-gradient(top, #ed391b, #ce1a00);
		background-image: -ms-linear-gradient(top, #ed391b, #ce1a00);
		background-image: linear-gradient(top, #ed391b, #ce1a00);
		display: inline-block;
		background-color: #ed391b;
		color: #fff;
		text-decoration: none;
		font-size: 1.75em;
		height: 2em;
		line-height: 2.125em;
		font-weight: 300;
		padding: 0 45px;
		outline: 0;
		border-radius: 10px;
		box-shadow: inset 0px 0px 0px 1px rgba(0, 0, 0, 0.75), inset 0px 2px 0px 0px rgba(255, 192, 192, 0.5), inset 0px 0px 0px 2px rgba(255, 96, 96, 0.85), 3px 3px 3px 1px rgba(0, 0, 0, 0.15);
		text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.5);
	}

		.button-large:hover {
			background-image: -moz-linear-gradient(top, #fd492b, #de2a10);
			background-image: -webkit-linear-gradient(top, #fd492b, #de2a10);
			background-image: -ms-linear-gradient(top, #fd492b, #de2a10);
			background-image: linear-gradient(top, #fd492b, #de2a10);
			background-color: #fd492b;
			box-shadow: inset 0px 0px 0px 1px rgba(0, 0, 0, 0.75), inset 0px 2px 0px 0px rgba(255, 192, 192, 0.5), inset 0px 0px 0px 2px rgba(255, 96, 96, 0.85), 3px 3px 3px 1px rgba(0, 0, 0, 0.15);
		}

		.button-large:active {
			background-image: -moz-linear-gradient(top, #ce1a00, #ed391b);
			background-image: -webkit-linear-gradient(top, #ce1a00, #ed391b);
			background-image: -ms-linear-gradient(top, #ce1a00, #ed391b);
			background-image: linear-gradient(top, #ce1a00, #ed391b);
			background-color: #ce1a00;
			box-shadow: inset 0px 0px 0px 1px rgba(0, 0, 0, 0.75), inset 0px 2px 0px 0px rgba(255, 192, 192, 0.5), inset 0px 0px 0px 2px rgba(255, 96, 96, 0.85), 3px 3px 3px 1px rgba(0, 0, 0, 0.15);
		}

/* Header */

	#header {
		position: relative;
		background: #3B4346 url("ambeint.jpg");
		border-bottom: solid 1px #272d30;
		box-shadow: inset 0px -1px 0px 0px #51575a;
		text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.75);
	}

		#header > .container {
			position: relative;
			min-height: 155px;
		}

		#header h1 {
			position: absolute;
			left: 0;
			bottom: 35px;
			font-size: 2.75em;
		}

			#header h1 a {
				color: #fff;
				text-decoration: none;
			}

		#header nav {
			position: absolute;
			right: 0;
			bottom: 35px;
			font-weight: 200;
		}

			#header nav a {
				color: #c6c8c8;
				text-decoration: none;
				font-size: 1.4em;
				margin-left: 60px;
				outline: 0;
			}

				#header nav a:hover {
					color: #f6f8f8;
				}

		.subpage #header > .container {
			height: 155px;
		}

/* Banner */

	#banner {
		border-top: solid 1px #222628;
		box-shadow: inset 0px 1px 0px 0px #3e484a;
		padding: 35px 0 35px 0;
		color: #fff;
	}

		#banner .bordered-feature-image {
			margin-bottom: 0;
		}

		#banner p {
			font-size: 2em;
			font-weight: 200;
			line-height: 1.25em;
			padding-right: 1em;
			margin: 0 0 1em 0;
		}

/* Features */

	#features {
		background: #353D40 url("images/bg02.jpg");
		border-bottom: solid 1px #272e31;
		padding: 45px 0 45px 0;
		text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.75);
		color: #a0a8ab;
	}

		#features h2 {
			font-size: 1.25em;
			color: #fff;
			margin: 0 0 0.25em 0;
		}

		#features a {
			color: #e0e8eb;
		}

		#features strong {
			color: #fff;
		}

/* Content */

	#content {
		background: #f7f7f7 url("images/ambient.png");
		border-top: solid 1px #fff;
		padding: 45px 0 45px 0;
	}

		#content section {
			background: #fff;
			padding: 40px 30px 45px 30px;
			box-shadow: 2px 2px 2px 1px rgba(128, 128, 128, 0.1);
			margin: 0 0 25px 0;
		}

		#content h2 {
			font-size: 1.8em;
			color: #373f42;
			margin: 0 0 0.25em 0;
		}

		#content h3 {
			color: #96a9b5;
			font-size: 1.25em;
		}

		#content a {
			color: #ED391B;
		}

		#content header {
			margin: 0 0 2em 0;
		}

		#content .quote-list li {
			border-bottom: solid 1px #e2e6e8;
		}

		#content .link-list li {
			border-bottom: solid 1px #e2e6e8;
		}

		#content .check-list li {
			border-bottom: solid 1px #e2e6e8;
		}

/* Footer */

	#footer {
		padding: 45px 0 45px 0;
		text-shadow: 1px 1px 1px white;
		color: #546b76;
		text-shadow: 1px 1px 0px rgba(255, 255, 255, 0.5);
	}

		#footer h2 {
			font-size: 1.25em;
			color: #212f35;
			margin: 0 0 1em 0;
		}

		#footer a {
			color: #546b76;
		}

		#footer .quote-list li {
			border-top: solid 1px #e0e4e6;
			border-bottom: solid 1px #b5bec3;
		}

		#footer .link-list li {
			border-top: solid 1px #e0e4e6;
			border-bottom: solid 1px #b5bec3;
		}

		#footer .check-list li {
			border-top: solid 1px #e0e4e6;
			border-bottom: solid 1px #b5bec3;
		}

/* Copyright */

	#copyright {
		border-top: solid 1px #b5bec3;
		box-shadow: inset 0px 1px 0px 0px #e0e4e7;
		text-align: center;
		padding: 45px 0 80px 0;
		color: #8d9ca3;
		text-shadow: 1px 1px 0px rgba(255, 255, 255, 0.5);
	}

		#copyright a {
			color: #8d9ca3;
		}

/* Large */

	@media screen and (max-width: 1280px) {

		/* Multi-use */

			.check-list li {
				font-size: 1em;
				line-height: 2em;
			}

			.quote-list li {
				padding: 1em 0 1em 0;
			}

				.quote-list li img {
					width: 60px;
				}

				.quote-list li p {
					margin: 0 0 0 80px;
					font-size: 1em;
					font-style: italic;
					line-height: 1.8em;
				}

				.quote-list li span {
					display: block;
					margin-left: 80px;
					font-size: 0.8em;
					font-weight: 400;
					line-height: 1.8em;
				}

			.feature-image {
				margin: 0 0 1em 0;
			}

			.button-large {
				font-size: 1.5em;
			}

		/* Banner */

			#banner p {
				font-size: 1.75em;
			}

		/* Header */

			#header h1 {
				font-size: 2.25em;
			}

			#header nav a {
				font-size: 1.1em;
			}

		/* Content */

			#content h2 {
				font-size: 1.4em;
			}

			#content h3 {
				font-size: 1.1em;
			}

			#content header {
				margin: 0 0 1.25em 0;
			}

	}

/* Medium */

	#navPanel, #titleBar {
		display: none;
	}

	@media screen and (max-width: 980px) {

		/* Basic */

			html, body {
				overflow-x: hidden;
			}

		/* Header */

			#header {
				text-align: center;
			}

				#header > .container:first-child {
					display: none;
				}

		/* Content */

			#content {
				padding: 25px 0;
			}

		/* Nav */

			#page-wrapper {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				padding-bottom: 1px;
				padding-top: 44px;
			}

			#titleBar {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 44px;
				left: 0;
				position: fixed;
				top: 0;
				width: 100%;
				z-index: 10001;
				color: #fff;
				background: url("ambient.jpg");
				box-shadow: inset 0px -20px 70px 0px rgba(200, 220, 245, 0.1), inset 0px -1px 0px 0px rgba(255, 255, 255, 0.1), 0px 1px 7px 0px rgba(0, 0, 0, 0.6);
				text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.75);
			}

				#titleBar .title {
					display: block;
					text-align: center;
					font-size: 1.2em;
					font-weight: 400;
					line-height: 48px;
				}

				#titleBar .toggle {
					position: absolute;
					left: 0;
					top: 0;
					width: 80px;
					height: 60px;
				}

					#titleBar .toggle:after {
						content: '';
						display: block;
						position: absolute;
						top: 6px;
						left: 6px;
						color: #fff;
						background: rgba(255, 255, 255, 0.025);
						box-shadow: inset 0px 1px 0px 0px rgba(255, 255, 255, 0.1), inset 0px 0px 0px 1px rgba(255, 255, 255, 0.05), inset 0px -8px 10px 0px rgba(0, 0, 0, 0.15), 0px 1px 2px 0px rgba(0, 0, 0, 0.25);
						text-shadow: -1px -1px 1px black;
						width: 49px;
						height: 31px;
						border-radius: 8px;
					}

					#titleBar .toggle:before {
						content: '';
						position: absolute;
						width: 20px;
						height: 30px;
						background: url("images/mobileUI-site-nav-opener-bg.svg");
						top: 15px;
						left: 20px;
						z-index: 1;
						opacity: 0.25;
					}

					#titleBar .toggle:active:after {
						background: rgba(255, 255, 255, 0.05);
					}

			#navPanel {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transform: translateX(-275px);
				-webkit-transform: translateX(-275px);
				-ms-transform: translateX(-275px);
				transform: translateX(-275px);
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 100%;
				left: 0;
				overflow-y: auto;
				position: fixed;
				top: 0;
				width: 275px;
				z-index: 10002;
				background: url("ambeint.jpg");
				box-shadow: inset -1px 0px 0px 0px rgba(255, 255, 255, 0.25), inset -2px 0px 25px 0px rgba(0, 0, 0, 0.5);
				text-shadow: -1px -1px 1px black;
			}

				#navPanel .link {
					display: block;
					color: #fff;
					text-decoration: none;
					font-size: 1.25em;
					line-height: 2em;
					padding: 0.625em 1.5em 0.325em 1.5em;
					border-top: solid 1px #373d40;
					border-bottom: solid 1px rgba(0, 0, 0, 0.4);
				}

					#navPanel .link:first-child {
						border-top: 0;
					}

					#navPanel .link:last-child {
						border-bottom: 0;
					}

			body.navPanel-visible #page-wrapper {
				-moz-transform: translateX(275px);
				-webkit-transform: translateX(275px);
				-ms-transform: translateX(275px);
				transform: translateX(275px);
			}

			body.navPanel-visible #titleBar {
				-moz-transform: translateX(275px);
				-webkit-transform: translateX(275px);
				-ms-transform: translateX(275px);
				transform: translateX(275px);
			}

			body.navPanel-visible #navPanel {
				-moz-transform: translateX(0);
				-webkit-transform: translateX(0);
				-ms-transform: translateX(0);
				transform: translateX(0);
			}

	}

/* Small */

	@media screen and (max-width: 736px) {

		/* Basic */

			body, input, textarea, select {
				font-size: 13pt;
				line-height: 1.4em;
			}

		/* Multi-use */

			.link-list li {
				padding: 0.75em 0 0.75em 0;
			}

			.quote-list li p {
				margin-bottom: 0.5em;
			}

			.check-list li {
				font-size: 1em;
			}

			.button-large {
				width: 100%;
			}

		/* Banner */

			#banner p {
				font-size: 1.25em;
				font-weight: 200;
				line-height: 1.25em;
				margin: 0 0 1em 0;
			}

		/* Content */

			#content section {
				padding: 30px 20px;
			}

			#content h2 {
				font-size: 1.25em;
			}

			#content h3 {
				font-size: 1em;
			}

			#content header {
				margin: 0 0 1.25em 0;
			}

		/* Footer */

			#footer .link-list {
				margin: 0 0 10px 0 !important;
			}

		/* Copyright */

			#copyright {
				padding: 20px 30px;
			}

	}""", 
	"elegant":"""
	#header {
		background: #173B45;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #173B45, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #173B45;
			}
			.dropotron {
				background: #173B45;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #173B45;
			}
			#features {
				background: #173B45;
			}
			
	#banner {
		background: #173B45;
		color: #173B45;
	}
	
	#main {
		background: #173B45;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #173B45, inset 0px 10px 0px 0px #e5e5e5;
	}
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #173B45, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #173B45;
	}
	#navPanel .link.depth-0 {
		color: #173B45;
	}
	
	#navPanel .depth-0 {
		color: #173B45;
	}
	
	#navPanel .link
	{
		color: #fff;
	}
	#content section
	{
		background : #fff;
	}
	h1, h2, h3, h4, h5,h6{
		color:#ed786a;
	}""",
	"lime":"""
	#header {
		background: #17451f;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #17451f, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #17451f;
			}
			.dropotron {
				background: #17451f;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #17451f;
			}
			#features {
				background: #17451f;
			}
			
	#banner {
		background: #17451f;
		color: #17451f;
	}
	
	#main {
		background: #17451f;
	}
	#footer {
		background: #A2CA71;
		color: white;
	}
	#footer h2{color:#F6E96B}
	#navPanel .link.depth-0 {
		color: #17451f;
	}
	
	#navPanel .depth-0 {
		color: #17451f;
	}
	
	#navPanel .link
	{
		color: #fff;
	}
	#content section
	{
		background : #fff;
	}
	h1, h2, h3, h4, h5,h6{
		color:#ed786a;
		
	}
	
	#header {
		position: relative;
		border-bottom: solid 1px #272d30;
		box-shadow: inset 0px 0px 0px 0px #51575a;
		text-shadow: -1px -1px 1px rgba(0, 0, 0, 0);
	}""",
	"sakura":"""
	#header {
		background: #ff25c9;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #ff25c9, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #ff25c9;
			}
			.dropotron {
				background: #ff25c9;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #ff25c9;
			}
			#features {
				background: #ff25c9;
			}
			
	#banner {
		background: #ff25c9;
		color: #ff25c9;
	}
	
	#main {
		background: #ff25c9;
	}
	#footer {
		background: #81064b;
		color: white;
	}
	#footer h2{color:#F6E96B}
	#navPanel .link.depth-0 {
		color: #ff25c9;
	}
	
	#navPanel .depth-0 {
		color: #ff25c9;
	}
	
	#navPanel .link
	{
		color: #fff;
	}
	#content section
	{
		background : #fff;
	}
	h1, h2, h3, h4, h5,h6{
		color:#ed786a;
		
	}
	""", 
	"phantom":"""	#header {
		background: #4b055a;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #4b055a, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #4b055a;
			}
			.dropotron {
				background: #4b055a;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #4b055a;
			}
			#features {
				background: #4b055a;
			}
			
	#banner {
		background: #4b055a;
		color: #4b055a;
	}
	
	#main {
		background: #4b055a;
	}
	#footer {
		background: #81064b;
		color: white;
	}
	#footer h2{color:#3f76b5}
	#navPanel .link.depth-0 {
		color: #4b055a;
	}
	
	#navPanel .depth-0 {
		color: #4b055a;
	}
	
	#navPanel .link
	{
		color: #fff;
	}
	#content section
	{
		background : #fff;
	}
	h1, h2, h3, h4, h5,h6{
		color:#ed786a;
		
	}
	
	#header {
		position: relative;
		color:#3f76b5;
		border-bottom: solid 1px #272d30;
		box-shadow: inset 0px 0px 0px 0px #51575a;
		text-shadow: -1px -1px 1px rgba(0, 0, 0, 0);
	}
	""", 
	"valley":"""	#header {
		background: #4b055a;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #4b055a, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #4b055a;
			}
			.dropotron {
				background: #4b055a;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #4b055a;
			}
			#features {
				background: #4b055a;
			}
			
	#banner {
		background: #4b055a;
		color: #4b055a;
	}
	
	#main {
		background: #4b055a;
	}
	#footer {
		background: #81064b;
		color: white;
	}
	#footer h2{color:#3f76b5}
	#navPanel .link.depth-0 {
		color: #4b055a;
	}
	
	#navPanel .depth-0 {
		color: #4b055a;
	}
	
	#navPanel .link
	{
		color: #fff;
	}
	#content section
	{
		background : #fff;
	}
	h1, h2, h3, h4, h5,h6{
		color:#ed786a;
		
	}
	
	#header {
		position: relative;
		color:#3f76b5;
		border-bottom: solid 1px #272d30;
		box-shadow: inset 0px 0px 0px 0px #51575a;
		text-shadow: -1px -1px 1px rgba(0, 0, 0, 0);
	}""",
}, 
"space":{
	"default":"""@import url(fontawesome-all.min.css);

/*
	Hyperspace by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	@-ms-viewport {
		width: device-width;
	}

	body {
		-ms-overflow-style: scrollbar;
	}

	@media screen and (max-width: 480px) {

		html, body {
			min-width: 320px;
		}

	}

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #312450;
	}

		body.is-preload *, body.is-preload *:before, body.is-preload *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

/* Type */

	body, input, select, textarea {
		color: rgba(255, 255, 255, 0.55);
		font-family: Arial, Helvetica, sans-serif;
		font-size: 16.5pt;
		font-weight: normal;
		line-height: 1.75;
	}

		@media screen and (max-width: 1680px) {

			body, input, select, textarea {
				font-size: 13pt;
			}

		}

		@media screen and (max-width: 1280px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 360px) {

			body, input, select, textarea {
				font-size: 11pt;
			}

		}

	a {
		-moz-transition: color 0.2s ease, border-bottom-color 0.2s ease;
		-webkit-transition: color 0.2s ease, border-bottom-color 0.2s ease;
		-ms-transition: color 0.2s ease, border-bottom-color 0.2s ease;
		transition: color 0.2s ease, border-bottom-color 0.2s ease;
		border-bottom: dotted 1px rgba(255, 255, 255, 0.35);
		color: inherit;
		text-decoration: none;
	}

		a:hover {
			border-bottom-color: transparent;
			color: #ffffff;
		}

	strong, b {
		color: #ffffff;
		font-weight: bold;
	}

	em, i {
		font-style: italic;
	}

	p {
		margin: 0 0 2em 0;
	}

	h1, h2, h3, h4, h5, h6 {
		color: #ffffff;
		font-weight: bold;
		line-height: 1.5;
		margin: 0 0 0.5em 0;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			color: inherit;
			text-decoration: none;
		}

	h1 {
		font-size: 2.75em;
	}

		h1.major {
			margin: 0 0 1.3em 0;
			position: relative;
			padding-bottom: 0.35em;
		}

			h1.major:after {
				background-image: -moz-linear-gradient(to right, #5e42a6, #b74e91);
				background-image: -webkit-linear-gradient(to right, #5e42a6, #b74e91);
				background-image: -ms-linear-gradient(to right, #5e42a6, #b74e91);
				background-image: linear-gradient(to right, #5e42a6, #b74e91);
				-moz-transition: max-width 0.2s ease;
				-webkit-transition: max-width 0.2s ease;
				-ms-transition: max-width 0.2s ease;
				transition: max-width 0.2s ease;
				border-radius: 0.2em;
				bottom: 0;
				content: '';
				height: 0.05em;
				position: absolute;
				right: 0;
				width: 100%;
			}

	h2 {
		font-size: 1.75em;
	}

	h3 {
		font-size: 1.1em;
	}

	h4 {
		font-size: 1em;
	}

	h5 {
		font-size: 0.8em;
	}

	h6 {
		font-size: 0.6em;
	}

	@media screen and (max-width: 736px) {

		h1 {
			font-size: 2em;
		}

		h2 {
			font-size: 1.25em;
		}

		h3 {
			font-size: 1em;
		}

		h4 {
			font-size: 0.8em;
		}

		h5 {
			font-size: 0.6em;
		}

		h6 {
			font-size: 0.6em;
		}

	}

	sub {
		font-size: 0.8em;
		position: relative;
		top: 0.5em;
	}

	sup {
		font-size: 0.8em;
		position: relative;
		top: -0.5em;
	}

	blockquote {
		border-left: solid 4px rgba(255, 255, 255, 0.15);
		font-style: italic;
		margin: 0 0 2em 0;
		padding: 0.5em 0 0.5em 2em;
	}

	code {
		background: rgba(255, 255, 255, 0.05);
		border-radius: 0.25em;
		border: solid 1px rgba(255, 255, 255, 0.15);
		font-family: "Courier New", monospace;
		font-size: 0.9em;
		margin: 0 0.25em;
		padding: 0.25em 0.65em;
	}

	pre {
		-webkit-overflow-scrolling: touch;
		font-family: "Courier New", monospace;
		font-size: 0.9em;
		margin: 0 0 2em 0;
	}

		pre code {
			display: block;
			line-height: 1.75em;
			padding: 1em 1.5em;
			overflow-x: auto;
		}

	hr {
		border: 0;
		border-bottom: solid 1px rgba(255, 255, 255, 0.15);
		margin: 2em 0;
	}

		hr.major {
			margin: 3em 0;
		}

	.align-left {
		text-align: left;
	}

	.align-center {
		text-align: center;
	}

	.align-right {
		text-align: right;
	}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0;
			margin-left: 0em;
		}

			.row.gtr-0 > * {
				padding: 0 0 0 0em;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0em;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0em;
				}

		.row.gtr-25 {
			margin-top: 0;
			margin-left: -0.375em;
		}

			.row.gtr-25 > * {
				padding: 0 0 0 0.375em;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -0.375em;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 0.375em;
				}

		.row.gtr-50 {
			margin-top: 0;
			margin-left: -0.75em;
		}

			.row.gtr-50 > * {
				padding: 0 0 0 0.75em;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -0.75em;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 0.75em;
				}

		.row {
			margin-top: 0;
			margin-left: -1.5em;
		}

			.row > * {
				padding: 0 0 0 1.5em;
			}

			.row.gtr-uniform {
				margin-top: -1.5em;
			}

				.row.gtr-uniform > * {
					padding-top: 1.5em;
				}

		.row.gtr-150 {
			margin-top: 0;
			margin-left: -2.25em;
		}

			.row.gtr-150 > * {
				padding: 0 0 0 2.25em;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -2.25em;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 2.25em;
				}

		.row.gtr-200 {
			margin-top: 0;
			margin-left: -3em;
		}

			.row.gtr-200 > * {
				padding: 0 0 0 3em;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -3em;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 3em;
				}

		@media screen and (max-width: 1680px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xlarge {
					order: -1;
				}

				.row > .col-1-xlarge {
					width: 8.33333%;
				}

				.row > .off-1-xlarge {
					margin-left: 8.33333%;
				}

				.row > .col-2-xlarge {
					width: 16.66667%;
				}

				.row > .off-2-xlarge {
					margin-left: 16.66667%;
				}

				.row > .col-3-xlarge {
					width: 25%;
				}

				.row > .off-3-xlarge {
					margin-left: 25%;
				}

				.row > .col-4-xlarge {
					width: 33.33333%;
				}

				.row > .off-4-xlarge {
					margin-left: 33.33333%;
				}

				.row > .col-5-xlarge {
					width: 41.66667%;
				}

				.row > .off-5-xlarge {
					margin-left: 41.66667%;
				}

				.row > .col-6-xlarge {
					width: 50%;
				}

				.row > .off-6-xlarge {
					margin-left: 50%;
				}

				.row > .col-7-xlarge {
					width: 58.33333%;
				}

				.row > .off-7-xlarge {
					margin-left: 58.33333%;
				}

				.row > .col-8-xlarge {
					width: 66.66667%;
				}

				.row > .off-8-xlarge {
					margin-left: 66.66667%;
				}

				.row > .col-9-xlarge {
					width: 75%;
				}

				.row > .off-9-xlarge {
					margin-left: 75%;
				}

				.row > .col-10-xlarge {
					width: 83.33333%;
				}

				.row > .off-10-xlarge {
					margin-left: 83.33333%;
				}

				.row > .col-11-xlarge {
					width: 91.66667%;
				}

				.row > .off-11-xlarge {
					margin-left: 91.66667%;
				}

				.row > .col-12-xlarge {
					width: 100%;
				}

				.row > .off-12-xlarge {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-large {
					order: -1;
				}

				.row > .col-1-large {
					width: 8.33333%;
				}

				.row > .off-1-large {
					margin-left: 8.33333%;
				}

				.row > .col-2-large {
					width: 16.66667%;
				}

				.row > .off-2-large {
					margin-left: 16.66667%;
				}

				.row > .col-3-large {
					width: 25%;
				}

				.row > .off-3-large {
					margin-left: 25%;
				}

				.row > .col-4-large {
					width: 33.33333%;
				}

				.row > .off-4-large {
					margin-left: 33.33333%;
				}

				.row > .col-5-large {
					width: 41.66667%;
				}

				.row > .off-5-large {
					margin-left: 41.66667%;
				}

				.row > .col-6-large {
					width: 50%;
				}

				.row > .off-6-large {
					margin-left: 50%;
				}

				.row > .col-7-large {
					width: 58.33333%;
				}

				.row > .off-7-large {
					margin-left: 58.33333%;
				}

				.row > .col-8-large {
					width: 66.66667%;
				}

				.row > .off-8-large {
					margin-left: 66.66667%;
				}

				.row > .col-9-large {
					width: 75%;
				}

				.row > .off-9-large {
					margin-left: 75%;
				}

				.row > .col-10-large {
					width: 83.33333%;
				}

				.row > .off-10-large {
					margin-left: 83.33333%;
				}

				.row > .col-11-large {
					width: 91.66667%;
				}

				.row > .off-11-large {
					margin-left: 91.66667%;
				}

				.row > .col-12-large {
					width: 100%;
				}

				.row > .off-12-large {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 980px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-medium {
					order: -1;
				}

				.row > .col-1-medium {
					width: 8.33333%;
				}

				.row > .off-1-medium {
					margin-left: 8.33333%;
				}

				.row > .col-2-medium {
					width: 16.66667%;
				}

				.row > .off-2-medium {
					margin-left: 16.66667%;
				}

				.row > .col-3-medium {
					width: 25%;
				}

				.row > .off-3-medium {
					margin-left: 25%;
				}

				.row > .col-4-medium {
					width: 33.33333%;
				}

				.row > .off-4-medium {
					margin-left: 33.33333%;
				}

				.row > .col-5-medium {
					width: 41.66667%;
				}

				.row > .off-5-medium {
					margin-left: 41.66667%;
				}

				.row > .col-6-medium {
					width: 50%;
				}

				.row > .off-6-medium {
					margin-left: 50%;
				}

				.row > .col-7-medium {
					width: 58.33333%;
				}

				.row > .off-7-medium {
					margin-left: 58.33333%;
				}

				.row > .col-8-medium {
					width: 66.66667%;
				}

				.row > .off-8-medium {
					margin-left: 66.66667%;
				}

				.row > .col-9-medium {
					width: 75%;
				}

				.row > .off-9-medium {
					margin-left: 75%;
				}

				.row > .col-10-medium {
					width: 83.33333%;
				}

				.row > .off-10-medium {
					margin-left: 83.33333%;
				}

				.row > .col-11-medium {
					width: 91.66667%;
				}

				.row > .off-11-medium {
					margin-left: 91.66667%;
				}

				.row > .col-12-medium {
					width: 100%;
				}

				.row > .off-12-medium {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-small {
					order: -1;
				}

				.row > .col-1-small {
					width: 8.33333%;
				}

				.row > .off-1-small {
					margin-left: 8.33333%;
				}

				.row > .col-2-small {
					width: 16.66667%;
				}

				.row > .off-2-small {
					margin-left: 16.66667%;
				}

				.row > .col-3-small {
					width: 25%;
				}

				.row > .off-3-small {
					margin-left: 25%;
				}

				.row > .col-4-small {
					width: 33.33333%;
				}

				.row > .off-4-small {
					margin-left: 33.33333%;
				}

				.row > .col-5-small {
					width: 41.66667%;
				}

				.row > .off-5-small {
					margin-left: 41.66667%;
				}

				.row > .col-6-small {
					width: 50%;
				}

				.row > .off-6-small {
					margin-left: 50%;
				}

				.row > .col-7-small {
					width: 58.33333%;
				}

				.row > .off-7-small {
					margin-left: 58.33333%;
				}

				.row > .col-8-small {
					width: 66.66667%;
				}

				.row > .off-8-small {
					margin-left: 66.66667%;
				}

				.row > .col-9-small {
					width: 75%;
				}

				.row > .off-9-small {
					margin-left: 75%;
				}

				.row > .col-10-small {
					width: 83.33333%;
				}

				.row > .off-10-small {
					margin-left: 83.33333%;
				}

				.row > .col-11-small {
					width: 91.66667%;
				}

				.row > .off-11-small {
					margin-left: 91.66667%;
				}

				.row > .col-12-small {
					width: 100%;
				}

				.row > .off-12-small {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 480px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xsmall {
					order: -1;
				}

				.row > .col-1-xsmall {
					width: 8.33333%;
				}

				.row > .off-1-xsmall {
					margin-left: 8.33333%;
				}

				.row > .col-2-xsmall {
					width: 16.66667%;
				}

				.row > .off-2-xsmall {
					margin-left: 16.66667%;
				}

				.row > .col-3-xsmall {
					width: 25%;
				}

				.row > .off-3-xsmall {
					margin-left: 25%;
				}

				.row > .col-4-xsmall {
					width: 33.33333%;
				}

				.row > .off-4-xsmall {
					margin-left: 33.33333%;
				}

				.row > .col-5-xsmall {
					width: 41.66667%;
				}

				.row > .off-5-xsmall {
					margin-left: 41.66667%;
				}

				.row > .col-6-xsmall {
					width: 50%;
				}

				.row > .off-6-xsmall {
					margin-left: 50%;
				}

				.row > .col-7-xsmall {
					width: 58.33333%;
				}

				.row > .off-7-xsmall {
					margin-left: 58.33333%;
				}

				.row > .col-8-xsmall {
					width: 66.66667%;
				}

				.row > .off-8-xsmall {
					margin-left: 66.66667%;
				}

				.row > .col-9-xsmall {
					width: 75%;
				}

				.row > .off-9-xsmall {
					margin-left: 75%;
				}

				.row > .col-10-xsmall {
					width: 83.33333%;
				}

				.row > .off-10-xsmall {
					margin-left: 83.33333%;
				}

				.row > .col-11-xsmall {
					width: 91.66667%;
				}

				.row > .off-11-xsmall {
					margin-left: 91.66667%;
				}

				.row > .col-12-xsmall {
					width: 100%;
				}

				.row > .off-12-xsmall {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

/* Box */

	.box {
		border-radius: 0.25em;
		border: solid 1px rgba(255, 255, 255, 0.15);
		margin-bottom: 2em;
		padding: 1.5em;
	}

		.box > :last-child,
		.box > :last-child > :last-child,
		.box > :last-child > :last-child > :last-child {
			margin-bottom: 0;
		}

		.box.alt {
			border: 0;
			border-radius: 0;
			padding: 0;
		}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	button,
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: border-color 0.2s ease;
		-webkit-transition: border-color 0.2s ease;
		-ms-transition: border-color 0.2s ease;
		transition: border-color 0.2s ease;
		background-color: transparent;
		border: solid 1px !important;
		border-color: rgba(255, 255, 255, 0.15) !important;
		border-radius: 3em;
		color: #ffffff !important;
		cursor: pointer;
		display: inline-block;
		font-size: 0.6em;
		font-weight: bold;
		height: calc(4.75em + 2px);
		letter-spacing: 0.25em;
		line-height: 4.75em;
		outline: 0;
		padding: 0 3.75em;
		position: relative;
		text-align: center;
		text-decoration: none;
		text-transform: uppercase;
		white-space: nowrap;
	}

		input[type="submit"]:after,
		input[type="reset"]:after,
		input[type="button"]:after,
		button:after,
		.button:after {
			-moz-transform: scale(0.25);
			-webkit-transform: scale(0.25);
			-ms-transform: scale(0.25);
			transform: scale(0.25);
			pointer-events: none;
			-moz-transition: opacity 0.2s ease, -moz-transform 0.2s ease;
			-webkit-transition: opacity 0.2s ease, -webkit-transform 0.2s ease;
			-ms-transition: opacity 0.2s ease, -ms-transform 0.2s ease;
			transition: opacity 0.2s ease, transform 0.2s ease;
			background: #ffffff;
			border-radius: 3em;
			content: '';
			height: 100%;
			left: 0;
			opacity: 0;
			position: absolute;
			top: 0;
			width: 100%;
		}

		input[type="submit"].icon:before,
		input[type="reset"].icon:before,
		input[type="button"].icon:before,
		button.icon:before,
		.button.icon:before {
			margin-right: 0.75em;
		}

		input[type="submit"].fit,
		input[type="reset"].fit,
		input[type="button"].fit,
		button.fit,
		.button.fit {
			width: 100%;
		}

		input[type="submit"].small,
		input[type="reset"].small,
		input[type="button"].small,
		button.small,
		.button.small {
			font-size: 0.4em;
		}

		input[type="submit"].large,
		input[type="reset"].large,
		input[type="button"].large,
		button.large,
		.button.large {
			font-size: 0.8em;
		}

		input[type="submit"].primary,
		input[type="reset"].primary,
		input[type="button"].primary,
		button.primary,
		.button.primary {
			background-color: #ffffff;
			color: #312450 !important;
		}

			input[type="submit"].primary:after,
			input[type="reset"].primary:after,
			input[type="button"].primary:after,
			button.primary:after,
			.button.primary:after {
				display: none;
			}

		input[type="submit"].disabled, input[type="submit"]:disabled,
		input[type="reset"].disabled,
		input[type="reset"]:disabled,
		input[type="button"].disabled,
		input[type="button"]:disabled,
		button.disabled,
		button:disabled,
		.button.disabled,
		.button:disabled {
			cursor: default;
			opacity: 0.5;
			pointer-events: none;
		}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		button:hover,
		.button:hover {
			border-color: rgba(255, 255, 255, 0.55) !important;
		}

			input[type="submit"]:hover:after,
			input[type="reset"]:hover:after,
			input[type="button"]:hover:after,
			button:hover:after,
			.button:hover:after {
				opacity: 0.05;
				-moz-transform: scale(1);
				-webkit-transform: scale(1);
				-ms-transform: scale(1);
				transform: scale(1);
			}

			input[type="submit"]:hover:active,
			input[type="reset"]:hover:active,
			input[type="button"]:hover:active,
			button:hover:active,
			.button:hover:active {
				border-color: #ffffff !important;
			}

				input[type="submit"]:hover:active:after,
				input[type="reset"]:hover:active:after,
				input[type="button"]:hover:active:after,
				button:hover:active:after,
				.button:hover:active:after {
					opacity: 0.1;
				}

/* Features */

	.features {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-wrap: wrap;
		-webkit-flex-wrap: wrap;
		-ms-flex-wrap: wrap;
		flex-wrap: wrap;
		border-radius: 0.25em;
		border: solid 1px rgba(255, 255, 255, 0.15);
		background: rgba(255, 255, 255, 0.05);
		margin: 0 0 2em 0;
	}

		.features section {
			padding: 3.5em 3em 1em 7em ;
			width: 50%;
			border-top: solid 1px rgba(255, 255, 255, 0.15);
			position: relative;
		}

			.features section:nth-child(-n + 2) {
				border-top-width: 0;
			}

			.features section:nth-child(2n) {
				border-left: solid 1px rgba(255, 255, 255, 0.15);
			}

			.features section .icon {
				-moz-transition: opacity 0.5s ease, -moz-transform 0.5s ease;
				-webkit-transition: opacity 0.5s ease, -webkit-transform 0.5s ease;
				-ms-transition: opacity 0.5s ease, -ms-transform 0.5s ease;
				transition: opacity 0.5s ease, transform 0.5s ease;
				-moz-transition-delay: 1s;
				-webkit-transition-delay: 1s;
				-ms-transition-delay: 1s;
				transition-delay: 1s;
				-moz-transform: scale(1);
				-webkit-transform: scale(1);
				-ms-transform: scale(1);
				transform: scale(1);
				position: absolute;
				left: 3em;
				top: 3em;
				opacity: 1;
			}

			.features section:nth-child(1) .icon {
				-moz-transition-delay: 0.15s;
				-webkit-transition-delay: 0.15s;
				-ms-transition-delay: 0.15s;
				transition-delay: 0.15s;
			}

			.features section:nth-child(2) .icon {
				-moz-transition-delay: 0.3s;
				-webkit-transition-delay: 0.3s;
				-ms-transition-delay: 0.3s;
				transition-delay: 0.3s;
			}

			.features section:nth-child(3) .icon {
				-moz-transition-delay: 0.45s;
				-webkit-transition-delay: 0.45s;
				-ms-transition-delay: 0.45s;
				transition-delay: 0.45s;
			}

			.features section:nth-child(4) .icon {
				-moz-transition-delay: 0.6s;
				-webkit-transition-delay: 0.6s;
				-ms-transition-delay: 0.6s;
				transition-delay: 0.6s;
			}

			.features section:nth-child(5) .icon {
				-moz-transition-delay: 0.75s;
				-webkit-transition-delay: 0.75s;
				-ms-transition-delay: 0.75s;
				transition-delay: 0.75s;
			}

			.features section:nth-child(6) .icon {
				-moz-transition-delay: 0.9s;
				-webkit-transition-delay: 0.9s;
				-ms-transition-delay: 0.9s;
				transition-delay: 0.9s;
			}

			.features section:nth-child(7) .icon {
				-moz-transition-delay: 1.05s;
				-webkit-transition-delay: 1.05s;
				-ms-transition-delay: 1.05s;
				transition-delay: 1.05s;
			}

			.features section:nth-child(8) .icon {
				-moz-transition-delay: 1.2s;
				-webkit-transition-delay: 1.2s;
				-ms-transition-delay: 1.2s;
				transition-delay: 1.2s;
			}

			.features section:nth-child(9) .icon {
				-moz-transition-delay: 1.35s;
				-webkit-transition-delay: 1.35s;
				-ms-transition-delay: 1.35s;
				transition-delay: 1.35s;
			}

			.features section:nth-child(10) .icon {
				-moz-transition-delay: 1.5s;
				-webkit-transition-delay: 1.5s;
				-ms-transition-delay: 1.5s;
				transition-delay: 1.5s;
			}

			.features section:nth-child(11) .icon {
				-moz-transition-delay: 1.65s;
				-webkit-transition-delay: 1.65s;
				-ms-transition-delay: 1.65s;
				transition-delay: 1.65s;
			}

			.features section:nth-child(12) .icon {
				-moz-transition-delay: 1.8s;
				-webkit-transition-delay: 1.8s;
				-ms-transition-delay: 1.8s;
				transition-delay: 1.8s;
			}

			.features section:nth-child(13) .icon {
				-moz-transition-delay: 1.95s;
				-webkit-transition-delay: 1.95s;
				-ms-transition-delay: 1.95s;
				transition-delay: 1.95s;
			}

			.features section:nth-child(14) .icon {
				-moz-transition-delay: 2.1s;
				-webkit-transition-delay: 2.1s;
				-ms-transition-delay: 2.1s;
				transition-delay: 2.1s;
			}

			.features section:nth-child(15) .icon {
				-moz-transition-delay: 2.25s;
				-webkit-transition-delay: 2.25s;
				-ms-transition-delay: 2.25s;
				transition-delay: 2.25s;
			}

			.features section:nth-child(16) .icon {
				-moz-transition-delay: 2.4s;
				-webkit-transition-delay: 2.4s;
				-ms-transition-delay: 2.4s;
				transition-delay: 2.4s;
			}

			.features section:nth-child(17) .icon {
				-moz-transition-delay: 2.55s;
				-webkit-transition-delay: 2.55s;
				-ms-transition-delay: 2.55s;
				transition-delay: 2.55s;
			}

			.features section:nth-child(18) .icon {
				-moz-transition-delay: 2.7s;
				-webkit-transition-delay: 2.7s;
				-ms-transition-delay: 2.7s;
				transition-delay: 2.7s;
			}

			.features section:nth-child(19) .icon {
				-moz-transition-delay: 2.85s;
				-webkit-transition-delay: 2.85s;
				-ms-transition-delay: 2.85s;
				transition-delay: 2.85s;
			}

			.features section:nth-child(20) .icon {
				-moz-transition-delay: 3s;
				-webkit-transition-delay: 3s;
				-ms-transition-delay: 3s;
				transition-delay: 3s;
			}

		.features.inactive section .icon {
			-moz-transform: scale(0.5);
			-webkit-transform: scale(0.5);
			-ms-transform: scale(0.5);
			transform: scale(0.5);
			opacity: 0;
		}

		@media screen and (max-width: 980px) {

			.features {
				display: block;
			}

				.features section {
					border-top-width: 1px !important;
					border-left-width: 0 !important;
					width: 100%;
				}

					.features section:first-child {
						border-top-width: 0 !important;
					}

		}

		@media screen and (max-width: 736px) {

			.features section {
				padding: 2.5em 1.5em 0.1em 5.5em ;
			}

				.features section .icon {
					left: 1.5em;
					top: 2em;
				}

		}

		@media screen and (max-width: 480px) {

			.features section {
				padding: 2em 1.5em 0.1em 1.5em ;
			}

				.features section .icon {
					left: 0;
					position: relative;
					top: 0;
				}

		}

/* Form */

	form {
		margin: 0 0 2em 0;
	}

		form > :last-child {
			margin-bottom: 0;
		}

		form > .fields {
			display: -moz-flex;
			display: -webkit-flex;
			display: -ms-flex;
			display: flex;
			-moz-flex-wrap: wrap;
			-webkit-flex-wrap: wrap;
			-ms-flex-wrap: wrap;
			flex-wrap: wrap;
			width: calc(100% + 3em);
			margin: -1.5em 0 2em -1.5em;
		}

			form > .fields > .field {
				-moz-flex-grow: 0;
				-webkit-flex-grow: 0;
				-ms-flex-grow: 0;
				flex-grow: 0;
				-moz-flex-shrink: 0;
				-webkit-flex-shrink: 0;
				-ms-flex-shrink: 0;
				flex-shrink: 0;
				padding: 1.5em 0 0 1.5em;
				width: calc(100% - 1.5em);
			}

				form > .fields > .field.half {
					width: calc(50% - 0.75em);
				}

				form > .fields > .field.third {
					width: calc(100%/3 - 0.5em);
				}

				form > .fields > .field.quarter {
					width: calc(25% - 0.375em);
				}

		@media screen and (max-width: 480px) {

			form > .fields {
				width: calc(100% + 3em);
				margin: -1.5em 0 2em -1.5em;
			}

				form > .fields > .field {
					padding: 1.5em 0 0 1.5em;
					width: calc(100% - 1.5em);
				}

					form > .fields > .field.half {
						width: calc(100% - 1.5em);
					}

					form > .fields > .field.third {
						width: calc(100% - 1.5em);
					}

					form > .fields > .field.quarter {
						width: calc(100% - 1.5em);
					}

		}

	label {
		color: #ffffff;
		font-weight: bold;
		line-height: 1.5;
		margin: 0 0 0.7em 0;
		display: block;
		font-size: 1.1em;
	}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	input[type="tel"],
	select,
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		background: rgba(255, 255, 255, 0.05);
		border-radius: 0.25em;
		border: none;
		border: solid 1px rgba(255, 255, 255, 0.15);
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 1em;
		text-decoration: none;
		width: 100%;
	}

		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		input[type="tel"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		input[type="tel"]:focus,
		select:focus,
		textarea:focus {
			border-color: #ffffff;
			box-shadow: 0 0 0 1px #ffffff;
		}

	select {
		background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' preserveAspectRatio='none' viewBox='0 0 40 40'%3E%3Cpath d='M9.4,12.3l10.4,10.4l10.4-10.4c0.2-0.2,0.5-0.4,0.9-0.4c0.3,0,0.6,0.1,0.9,0.4l3.3,3.3c0.2,0.2,0.4,0.5,0.4,0.9 c0,0.4-0.1,0.6-0.4,0.9L20.7,31.9c-0.2,0.2-0.5,0.4-0.9,0.4c-0.3,0-0.6-0.1-0.9-0.4L4.3,17.3c-0.2-0.2-0.4-0.5-0.4-0.9 c0-0.4,0.1-0.6,0.4-0.9l3.3-3.3c0.2-0.2,0.5-0.4,0.9-0.4S9.1,12.1,9.4,12.3z' fill='rgba(255, 255, 255, 0.15)' /%3E%3C/svg%3E");
		background-size: 1.25rem;
		background-repeat: no-repeat;
		background-position: calc(100% - 1rem) center;
		height: 2.75em;
		padding-right: 2.75em;
		text-overflow: ellipsis;
	}

		select option {
			color: #ffffff;
			background: #312450;
		}

		select:focus::-ms-value {
			background-color: transparent;
		}

		select::-ms-expand {
			display: none;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 2.75em;
	}

	textarea {
		padding: 0.75em 1em;
	}

		body.is-ie textarea {
			min-height: 10em;
		}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2em;
		opacity: 0;
		width: 1em;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			color: rgba(255, 255, 255, 0.55);
			cursor: pointer;
			display: inline-block;
			font-size: 1em;
			font-weight: normal;
			padding-left: 2.4em;
			padding-right: 0.75em;
			position: relative;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				background: rgba(255, 255, 255, 0.05);
				border-radius: 0.25em;
				border: solid 1px rgba(255, 255, 255, 0.15);
				content: '';
				display: inline-block;
				font-size: 0.8em;
				height: 2.0625em;
				left: 0;
				line-height: 2.0625em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.0625em;
			}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			background: #ffffff;
			border-color: #ffffff;
			color: #b74e91;
			content: '\\f00c';
		}

		input[type="checkbox"]:focus + label:before,
		input[type="radio"]:focus + label:before {
			border-color: #ffffff;
			box-shadow: 0 0 0 1px #ffffff;
		}

	input[type="checkbox"] + label:before {
		border-radius: 0.25em;
	}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		color: rgba(255, 255, 255, 0.35) !important;
		opacity: 1.0;
	}

	:-moz-placeholder {
		color: rgba(255, 255, 255, 0.35) !important;
		opacity: 1.0;
	}

	::-moz-placeholder {
		color: rgba(255, 255, 255, 0.35) !important;
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		color: rgba(255, 255, 255, 0.35) !important;
		opacity: 1.0;
	}

/* Icon */

	.icon {
		text-decoration: none;
		border-bottom: none;
		position: relative;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 400;
		}

		.icon > .label {
			display: none;
		}

		.icon:before {
			line-height: inherit;
		}

		.icon.solid:before {
			font-weight: 900;
		}

		.icon.brands:before {
			font-family: 'Font Awesome 5 Brands';
		}

		.icon.major {
			width: 2.5em;
			height: 2.5em;
			display: block;
			background: #ffffff;
			border-radius: 100%;
			color: #312450;
			text-align: center;
			line-height: 2.5em;
			margin: 0 0 1.3em 0;
		}

			.icon.major:before {
				font-size: 1.25em;
			}

				.wrapper.style1 .icon.major:before {
					color: #5e42a6;
				}

				.wrapper.style1-alt .icon.major:before {
					color: #493382;
				}

				.wrapper.style2 .icon.major:before {
					color: #5052b5;
				}

				.wrapper.style2-alt .icon.major:before {
					color: #3e4094;
				}

				.wrapper.style3 .icon.major:before {
					color: #b74e91;
				}

				.wrapper.style3-alt .icon.major:before {
					color: #953d75;
				}

/* Image */

	.image {
		border-radius: 0.25em;
		border: 0;
		display: inline-block;
		position: relative;
	}

		.image img {
			border-radius: 0.25em;
			display: block;
		}

		.image.left, .image.right {
			max-width: 40%;
		}

			.image.left img, .image.right img {
				width: 100%;
			}

		.image.left {
			float: left;
			margin: 0 1.5em 1em 0;
			top: 0.25em;
		}

		.image.right {
			float: right;
			margin: 0 0 1em 1.5em;
			top: 0.25em;
		}

		.image.fit {
			display: block;
			margin: 0 0 2em 0;
			width: 100%;
		}

			.image.fit img {
				width: 100%;
			}

		.image.main {
			display: block;
			margin: 0 0 3em 0;
			width: 100%;
		}

			.image.main img {
				width: 100%;
			}

/* List */

	ol {
		list-style: decimal;
		margin: 0 0 2em 0;
		padding-left: 1.25em;
	}

		ol li {
			padding-left: 0.25em;
		}

	ul {
		list-style: disc;
		margin: 0 0 2em 0;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
		}

		ul.alt {
			list-style: none;
			padding-left: 0;
		}

			ul.alt li {
				border-top: solid 1px rgba(255, 255, 255, 0.15);
				padding: 0.5em 0;
			}

				ul.alt li:first-child {
					border-top: 0;
					padding-top: 0;
				}

	dl {
		margin: 0 0 2em 0;
	}

		dl dt {
			display: block;
			font-weight: bold;
			margin: 0 0 1em 0;
		}

		dl dd {
			margin-left: 2em;
		}

/* Actions */

	ul.actions {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		cursor: default;
		list-style: none;
		margin-left: -1em;
		padding-left: 0;
	}

		ul.actions li {
			padding: 0 0 0 1em;
			vertical-align: middle;
		}

		ul.actions.special {
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 100%;
			margin-left: 0;
		}

			ul.actions.special li:first-child {
				padding-left: 0;
			}

		ul.actions.stacked {
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			margin-left: 0;
		}

			ul.actions.stacked li {
				padding: 1.3em 0 0 0;
			}

				ul.actions.stacked li:first-child {
					padding-top: 0;
				}

		ul.actions.fit {
			width: calc(100% + 1em);
		}

			ul.actions.fit li {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				width: 100%;
			}

				ul.actions.fit li > * {
					width: 100%;
				}

			ul.actions.fit.stacked {
				width: 100%;
			}

		@media screen and (max-width: 480px) {

			ul.actions:not(.fixed) {
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
				margin-left: 0;
				width: 100% !important;
			}

				ul.actions:not(.fixed) li {
					-moz-flex-grow: 1;
					-webkit-flex-grow: 1;
					-ms-flex-grow: 1;
					flex-grow: 1;
					-moz-flex-shrink: 1;
					-webkit-flex-shrink: 1;
					-ms-flex-shrink: 1;
					flex-shrink: 1;
					padding: 1em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions:not(.fixed) li > * {
						width: 100%;
					}

					ul.actions:not(.fixed) li:first-child {
						padding-top: 0;
					}

					ul.actions:not(.fixed) li input[type="submit"],
					ul.actions:not(.fixed) li input[type="reset"],
					ul.actions:not(.fixed) li input[type="button"],
					ul.actions:not(.fixed) li button,
					ul.actions:not(.fixed) li .button {
						width: 100%;
					}

						ul.actions:not(.fixed) li input[type="submit"].icon:before,
						ul.actions:not(.fixed) li input[type="reset"].icon:before,
						ul.actions:not(.fixed) li input[type="button"].icon:before,
						ul.actions:not(.fixed) li button.icon:before,
						ul.actions:not(.fixed) li .button.icon:before {
							margin-left: -0.5rem;
						}

		}

/* Contact */

	ul.contact {
		list-style: none;
		padding: 0;
	}

		ul.contact > li {
			padding: 0;
			margin: 1.5em 0 0 0;
		}

			ul.contact > li:first-child {
				margin-top: 0;
			}

/* Icons */

	ul.icons {
		cursor: default;
		list-style: none;
		padding-left: 0;
	}

		ul.icons li {
			display: inline-block;
			padding: 0 0.75em 0 0;
		}

			ul.icons li:last-child {
				padding-right: 0;
			}

			ul.icons li > a, ul.icons li > span {
				border: 0;
			}

				ul.icons li > a .label, ul.icons li > span .label {
					display: none;
				}

/* Menu */

	ul.menu {
		list-style: none;
		padding: 0;
	}

		ul.menu > li {
			border-left: solid 1px rgba(255, 255, 255, 0.15);
			display: inline-block;
			line-height: 1;
			margin-left: 1.5em;
			padding: 0 0 0 1.5em;
		}

			ul.menu > li:first-child {
				border-left: 0;
				margin: 0;
				padding-left: 0;
			}

		@media screen and (max-width: 480px) {

			ul.menu > li {
				border-left: 0;
				display: block;
				line-height: inherit;
				margin: 0.5em 0 0 0;
				padding-left: 0;
			}

		}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header p {
		color: rgba(255, 255, 255, 0.35);
		position: relative;
		margin: 0 0 1.5em 0;
	}

	header h2 + p {
		font-size: 1.25em;
		margin-top: -1em;
		line-height: 1.5em;
	}

	header h3 + p {
		font-size: 1.1em;
		margin-top: -0.8em;
		line-height: 1.5em;
	}

	header h4 + p,
	header h5 + p,
	header h6 + p {
		font-size: 0.9em;
		margin-top: -0.6em;
		line-height: 1.5em;
	}

/* Split */

	.split {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
	}

		.split > * {
			width: calc(50% - 2.5em);
		}

		.split > :nth-child(2n - 1) {
			padding-right: 2.5em;
			border-right: solid 1px rgba(255, 255, 255, 0.15);
		}

		.split > :nth-child(2n) {
			padding-left: 2.5em;
		}

		.split.style1 > :nth-child(2n - 1) {
			width: calc(66.66666% - 2.5em);
		}

		.split.style1 > :nth-child(2n) {
			width: calc(33.33333% - 2.5em);
		}

		@media screen and (max-width: 1680px) {

			.split > * {
				width: calc(50% - 2em);
			}

			.split > :nth-child(2n - 1) {
				padding-right: 2em;
			}

			.split > :nth-child(2n) {
				padding-left: 2em;
			}

			.split.style1 > :nth-child(2n - 1) {
				width: calc(66.66666% - 2em);
			}

			.split.style1 > :nth-child(2n) {
				width: calc(33.33333% - 2em);
			}

		}

		@media screen and (max-width: 980px) {

			.split {
				display: block;
			}

				.split > * {
					border-top: solid 1px rgba(255, 255, 255, 0.15);
					margin: 4em 0 0 0;
					padding: 4em 0 0 0;
					width: 100% !important;
				}

				.split > :nth-child(2n - 1) {
					border-right: 0;
					padding-right: 0;
				}

				.split > :nth-child(2n) {
					padding-left: 0;
				}

				.split > :first-child {
					border-top: 0;
					margin-top: 0;
					padding-top: 0;
				}

		}

		@media screen and (max-width: 736px) {

			.split > * {
				margin: 3em 0 0 0;
				padding: 3em 0 0 0;
			}

		}

/* Spotlights */

	.spotlights > section {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: row;
		-webkit-flex-direction: row;
		-ms-flex-direction: row;
		flex-direction: row;
		min-height: 22.5em;
	}

		body.is-ie .spotlights > section {
			min-height: 0;
		}

		.spotlights > section > .image {
			background-position: center center;
			background-size: cover;
			border-radius: 0;
			display: block;
			position: relative;
			width: 25em;
		}

			.spotlights > section > .image img {
				border-radius: 0;
				display: block;
			}

			.spotlights > section > .image:before {
				-moz-transition: opacity 1s ease;
				-webkit-transition: opacity 1s ease;
				-ms-transition: opacity 1s ease;
				transition: opacity 1s ease;
				background: rgba(49, 36, 80, 0.9);
				content: '';
				display: block;
				height: 100%;
				left: 0;
				opacity: 0;
				position: absolute;
				top: 0;
				width: 100%;
			}

		.spotlights > section > .content {
			padding: 4em 5em 2em 5em ;
			display: -moz-flex;
			display: -webkit-flex;
			display: -ms-flex;
			display: flex;
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 50em;
			-ms-flex: 1;
		}

			.spotlights > section > .content > .inner {
				-moz-transform: translateX(0) translateY(0);
				-webkit-transform: translateX(0) translateY(0);
				-ms-transform: translateX(0) translateY(0);
				transform: translateX(0) translateY(0);
				-moz-transition: opacity 1s ease, -moz-transform 1s ease;
				-webkit-transition: opacity 1s ease, -webkit-transform 1s ease;
				-ms-transition: opacity 1s ease, -ms-transform 1s ease;
				transition: opacity 1s ease, transform 1s ease;
				opacity: 1;
			}

		.spotlights > section:nth-child(2) {
			background-color: rgba(0, 0, 0, 0.05);
		}

		.spotlights > section:nth-child(3) {
			background-color: rgba(0, 0, 0, 0.1);
		}

		.spotlights > section.inactive > .image:before,
		body.is-preload .spotlights > section > .image:before {
			opacity: 1;
		}

		.spotlights > section.inactive > .content > .inner,
		body.is-preload .spotlights > section > .content > .inner {
			-moz-transform: translateX(-1em);
			-webkit-transform: translateX(-1em);
			-ms-transform: translateX(-1em);
			transform: translateX(-1em);
			opacity: 0;
		}

		@media screen and (max-width: 1680px) {

			.spotlights > section > .content {
				padding: 4em 4em 2em 4em ;
			}

		}

		@media screen and (max-width: 980px) {

			.spotlights > section {
				display: block;
			}

				.spotlights > section > .image {
					width: 100%;
					height: 50vh;
				}

				.spotlights > section > .content {
					width: 100%;
				}

				.spotlights > section.inactive > .content > .inner,
				body.is-preload .spotlights > section > .content > .inner {
					-moz-transform: translateY(1em);
					-webkit-transform: translateY(1em);
					-ms-transform: translateY(1em);
					transform: translateY(1em);
				}

		}

		@media screen and (max-width: 736px) {

			.spotlights > section > .image {
				height: 50vh;
				min-height: 15em;
			}

			.spotlights > section > .content {
				padding: 3em 2em 1em 2em ;
			}

		}

/* Table */

	.table-wrapper {
		-webkit-overflow-scrolling: touch;
		overflow-x: auto;
	}

	table {
		margin: 0 0 2em 0;
		width: 100%;
	}

		table tbody tr {
			border: solid 1px rgba(255, 255, 255, 0.15);
			border-left: 0;
			border-right: 0;
		}

			table tbody tr:nth-child(2n + 1) {
				background-color: rgba(255, 255, 255, 0.05);
			}

		table td {
			padding: 0.75em 0.75em;
		}

		table th {
			color: #ffffff;
			font-size: 1em;
			font-weight: bold;
			padding: 0 0.75em 0.75em 0.75em;
			text-align: left;
		}

		table thead {
			border-bottom: solid 2px rgba(255, 255, 255, 0.15);
		}

		table tfoot {
			border-top: solid 2px rgba(255, 255, 255, 0.15);
		}

		table.alt {
			border-collapse: separate;
		}

			table.alt tbody tr td {
				border: solid 1px rgba(255, 255, 255, 0.15);
				border-left-width: 0;
				border-top-width: 0;
			}

				table.alt tbody tr td:first-child {
					border-left-width: 1px;
				}

			table.alt tbody tr:first-child td {
				border-top-width: 1px;
			}

			table.alt thead {
				border-bottom: 0;
			}

			table.alt tfoot {
				border-top: 0;
			}

/* Wrapper */

	.wrapper {
		position: relative;
	}

		.wrapper > .inner {
			padding: 5em 5em 3em 5em ;
			max-width: 100%;
			width: 75em;
		}

			@media screen and (max-width: 1680px) {

				.wrapper > .inner {
					padding: 4em 4em 2em 4em ;
				}

			}

			@media screen and (max-width: 1280px) {

				.wrapper > .inner {
					width: 100%;
				}

			}

			@media screen and (max-width: 736px) {

				.wrapper > .inner {
					padding: 3em 2em 1em 2em ;
				}

			}

		.wrapper.alt {
			background-color: #261c3e;
		}

		.wrapper.style1 {
			background-color: #5e42a6;
		}

		.wrapper.style1-alt {
			background-color: #493382;
		}

		.wrapper.style2 {
			background-color: #5052b5;
		}

		.wrapper.style2-alt {
			background-color: #3e4094;
		}

		.wrapper.style3 {
			background-color: #b74e91;
		}

		.wrapper.style3-alt {
			background-color: #953d75;
		}

		.wrapper.fullscreen {
			display: -moz-flex;
			display: -webkit-flex;
			display: -ms-flex;
			display: flex;
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			min-height: 100vh;
		}

			body.is-ie .wrapper.fullscreen {
				height: 100vh;
			}

			@media screen and (max-width: 1280px) {

				.wrapper.fullscreen {
					min-height: calc(100vh - 2.5em);
				}

					body.is-ie .wrapper.fullscreen {
						height: calc(100vh - 2.5em);
					}

			}

			@media screen and (max-width: 736px) {

				.wrapper.fullscreen {
					padding: 2em 0;
					min-height: 0;
				}

					body.is-ie .wrapper.fullscreen {
						height: auto;
					}

			}

		.wrapper.fade-up > .inner {
			-moz-transform: translateY(0);
			-webkit-transform: translateY(0);
			-ms-transform: translateY(0);
			transform: translateY(0);
			-moz-transition: opacity 1s ease, -moz-transform 1s ease;
			-webkit-transition: opacity 1s ease, -webkit-transform 1s ease;
			-ms-transition: opacity 1s ease, -ms-transform 1s ease;
			transition: opacity 1s ease, transform 1s ease;
			opacity: 1.0;
		}

		.wrapper.fade-up.inactive > .inner,
		body.is-preload .wrapper.fade-up > .inner {
			opacity: 0;
			-moz-transform: translateY(1em);
			-webkit-transform: translateY(1em);
			-ms-transform: translateY(1em);
			transform: translateY(1em);
		}

		.wrapper.fade-down > .inner {
			-moz-transform: translateY(0);
			-webkit-transform: translateY(0);
			-ms-transform: translateY(0);
			transform: translateY(0);
			-moz-transition: opacity 1s ease, -moz-transform 1s ease;
			-webkit-transition: opacity 1s ease, -webkit-transform 1s ease;
			-ms-transition: opacity 1s ease, -ms-transform 1s ease;
			transition: opacity 1s ease, transform 1s ease;
			opacity: 1.0;
		}

		.wrapper.fade-down.inactive > .inner,
		body.is-preload .wrapper.fade-down > .inner {
			opacity: 0;
			-moz-transform: translateY(-1em);
			-webkit-transform: translateY(-1em);
			-ms-transform: translateY(-1em);
			transform: translateY(-1em);
		}

		.wrapper.fade > .inner {
			-moz-transition: opacity 1s ease;
			-webkit-transition: opacity 1s ease;
			-ms-transition: opacity 1s ease;
			transition: opacity 1s ease;
			opacity: 1.0;
		}

		.wrapper.fade.inactive > .inner,
		body.is-preload .wrapper.fade > .inner {
			opacity: 0;
		}

/* Header */

	#header {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		background-color: #5e42a6;
		cursor: default;
		padding: 1.75em 2em;
	}

		#header > .title {
			border: 0;
			color: #ffffff;
			display: block;
			font-size: 1.25em;
			font-weight: bold;
		}

		#header > nav {
			-moz-flex: 1;
			-webkit-flex: 1;
			-ms-flex: 1;
			flex: 1;
			text-align: right;
		}

			#header > nav > ul {
				margin: 0;
				padding: 0;
			}

				#header > nav > ul > li {
					display: inline-block;
					margin-left: 1.75em;
					padding: 0;
					vertical-align: middle;
				}

					#header > nav > ul > li:first-child {
						margin-left: 0;
					}

					#header > nav > ul > li a {
						border: 0;
						color: rgba(255, 255, 255, 0.35);
						display: inline-block;
						font-size: 0.6em;
						font-weight: bold;
						letter-spacing: 0.25em;
						text-transform: uppercase;
					}

						#header > nav > ul > li a:hover {
							color: rgba(255, 255, 255, 0.55);
						}

						#header > nav > ul > li a.active {
							color: #ffffff;
						}

		@media screen and (max-width: 736px) {

			#header {
				padding: 1em 2em;
			}

		}

		@media screen and (max-width: 480px) {

			#header {
				display: block;
				padding: 0 2em;
				text-align: left;
			}

				#header .title {
					font-size: 1.25em;
					padding: 1em 0;
				}

				#header > nav {
					border-top: solid 1px rgba(255, 255, 255, 0.15);
					text-align: inherit;
				}

					#header > nav > ul > li {
						margin-left: 1.5em;
					}

						#header > nav > ul > li a {
							height: 6em;
							line-height: 6em;
						}

		}

/* Wrapper (main) */

	#sidebar + #wrapper {
		margin-left: 18em;
	}

		@media screen and (max-width: 1280px) {

			#sidebar + #wrapper {
				margin-left: 0;
				padding-top: 3.5em;
			}

		}

		@media screen and (max-width: 736px) {

			#sidebar + #wrapper {
				padding-top: 0;
			}

		}

	#header + #wrapper > .wrapper > .inner {
		margin: 0 auto;
	}

/* Footer */

	#sidebar + #wrapper + #footer {
		margin-left: 18em;
	}

		@media screen and (max-width: 1280px) {

			#sidebar + #wrapper + #footer {
				margin-left: 0;
			}

		}

	#footer > .inner a {
		border-bottom-color: rgba(255, 255, 255, 0.15);
	}

		#footer > .inner a:hover {
			border-bottom-color: transparent;
		}

	#footer > .inner .menu {
		font-size: 0.8em;
		color: rgba(255, 255, 255, 0.15);
	}

	#header + #wrapper + #footer > .inner {
		margin: 0 auto;
	}

/* Sidebar */

	#sidebar {
		padding: 2.5em 2.5em 0.5em 2.5em ;
		background: #312450;
		cursor: default;
		height: 100vh;
		left: 0;
		overflow-x: hidden;
		overflow-y: auto;
		position: fixed;
		text-align: right;
		top: 0;
		width: 18em;
		z-index: 10000;
	}

		#sidebar > .inner {
			display: -moz-flex;
			display: -webkit-flex;
			display: -ms-flex;
			display: flex;
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			-moz-transform: translateY(0);
			-webkit-transform: translateY(0);
			-ms-transform: translateY(0);
			transform: translateY(0);
			-moz-transition: opacity 1s ease;
			-webkit-transition: opacity 1s ease;
			-ms-transition: opacity 1s ease;
			transition: opacity 1s ease;
			min-height: 100%;
			opacity: 1;
			width: 100%;
		}

			body.is-ie #sidebar > .inner {
				height: 100%;
			}

		#sidebar nav > ul {
			list-style: none;
			padding: 0;
		}

			#sidebar nav > ul > li {
				-moz-transform: translateY(0);
				-webkit-transform: translateY(0);
				-ms-transform: translateY(0);
				transform: translateY(0);
				-moz-transition: opacity 0.15s ease, -moz-transform 0.75s ease;
				-webkit-transition: opacity 0.15s ease, -webkit-transform 0.75s ease;
				-ms-transition: opacity 0.15s ease, -ms-transform 0.75s ease;
				transition: opacity 0.15s ease, transform 0.75s ease;
				margin: 1.5em 0 0 0;
				opacity: 1;
				padding: 0;
				position: relative;
			}

				#sidebar nav > ul > li:first-child {
					margin: 0;
				}

				#sidebar nav > ul > li:nth-child(1) {
					-moz-transition-delay: 0.45s;
					-webkit-transition-delay: 0.45s;
					-ms-transition-delay: 0.45s;
					transition-delay: 0.45s;
				}

				#sidebar nav > ul > li:nth-child(2) {
					-moz-transition-delay: 0.65s;
					-webkit-transition-delay: 0.65s;
					-ms-transition-delay: 0.65s;
					transition-delay: 0.65s;
				}

				#sidebar nav > ul > li:nth-child(3) {
					-moz-transition-delay: 0.85s;
					-webkit-transition-delay: 0.85s;
					-ms-transition-delay: 0.85s;
					transition-delay: 0.85s;
				}

				#sidebar nav > ul > li:nth-child(4) {
					-moz-transition-delay: 1.05s;
					-webkit-transition-delay: 1.05s;
					-ms-transition-delay: 1.05s;
					transition-delay: 1.05s;
				}

				#sidebar nav > ul > li:nth-child(5) {
					-moz-transition-delay: 1.25s;
					-webkit-transition-delay: 1.25s;
					-ms-transition-delay: 1.25s;
					transition-delay: 1.25s;
				}

				#sidebar nav > ul > li:nth-child(6) {
					-moz-transition-delay: 1.45s;
					-webkit-transition-delay: 1.45s;
					-ms-transition-delay: 1.45s;
					transition-delay: 1.45s;
				}

				#sidebar nav > ul > li:nth-child(7) {
					-moz-transition-delay: 1.65s;
					-webkit-transition-delay: 1.65s;
					-ms-transition-delay: 1.65s;
					transition-delay: 1.65s;
				}

				#sidebar nav > ul > li:nth-child(8) {
					-moz-transition-delay: 1.85s;
					-webkit-transition-delay: 1.85s;
					-ms-transition-delay: 1.85s;
					transition-delay: 1.85s;
				}

				#sidebar nav > ul > li:nth-child(9) {
					-moz-transition-delay: 2.05s;
					-webkit-transition-delay: 2.05s;
					-ms-transition-delay: 2.05s;
					transition-delay: 2.05s;
				}

				#sidebar nav > ul > li:nth-child(10) {
					-moz-transition-delay: 2.25s;
					-webkit-transition-delay: 2.25s;
					-ms-transition-delay: 2.25s;
					transition-delay: 2.25s;
				}

				#sidebar nav > ul > li:nth-child(11) {
					-moz-transition-delay: 2.45s;
					-webkit-transition-delay: 2.45s;
					-ms-transition-delay: 2.45s;
					transition-delay: 2.45s;
				}

				#sidebar nav > ul > li:nth-child(12) {
					-moz-transition-delay: 2.65s;
					-webkit-transition-delay: 2.65s;
					-ms-transition-delay: 2.65s;
					transition-delay: 2.65s;
				}

				#sidebar nav > ul > li:nth-child(13) {
					-moz-transition-delay: 2.85s;
					-webkit-transition-delay: 2.85s;
					-ms-transition-delay: 2.85s;
					transition-delay: 2.85s;
				}

				#sidebar nav > ul > li:nth-child(14) {
					-moz-transition-delay: 3.05s;
					-webkit-transition-delay: 3.05s;
					-ms-transition-delay: 3.05s;
					transition-delay: 3.05s;
				}

				#sidebar nav > ul > li:nth-child(15) {
					-moz-transition-delay: 3.25s;
					-webkit-transition-delay: 3.25s;
					-ms-transition-delay: 3.25s;
					transition-delay: 3.25s;
				}

				#sidebar nav > ul > li:nth-child(16) {
					-moz-transition-delay: 3.45s;
					-webkit-transition-delay: 3.45s;
					-ms-transition-delay: 3.45s;
					transition-delay: 3.45s;
				}

				#sidebar nav > ul > li:nth-child(17) {
					-moz-transition-delay: 3.65s;
					-webkit-transition-delay: 3.65s;
					-ms-transition-delay: 3.65s;
					transition-delay: 3.65s;
				}

				#sidebar nav > ul > li:nth-child(18) {
					-moz-transition-delay: 3.85s;
					-webkit-transition-delay: 3.85s;
					-ms-transition-delay: 3.85s;
					transition-delay: 3.85s;
				}

				#sidebar nav > ul > li:nth-child(19) {
					-moz-transition-delay: 4.05s;
					-webkit-transition-delay: 4.05s;
					-ms-transition-delay: 4.05s;
					transition-delay: 4.05s;
				}

				#sidebar nav > ul > li:nth-child(20) {
					-moz-transition-delay: 4.25s;
					-webkit-transition-delay: 4.25s;
					-ms-transition-delay: 4.25s;
					transition-delay: 4.25s;
				}

		#sidebar nav a {
			-moz-transition: color 0.2s ease;
			-webkit-transition: color 0.2s ease;
			-ms-transition: color 0.2s ease;
			transition: color 0.2s ease;
			border: 0;
			color: rgba(255, 255, 255, 0.35);
			display: block;
			font-size: 0.6em;
			font-weight: bold;
			letter-spacing: 0.25em;
			line-height: 1.75;
			outline: 0;
			padding: 1.35em 0;
			position: relative;
			text-decoration: none;
			text-transform: uppercase;
		}

			#sidebar nav a:before, #sidebar nav a:after {
				border-radius: 0.2em;
				bottom: 0;
				content: '';
				height: 0.2em;
				position: absolute;
				right: 0;
				width: 100%;
			}

			#sidebar nav a:before {
				background: #3c2c62;
			}

			#sidebar nav a:after {
				background-image: -moz-linear-gradient(to right, #5e42a6, #b74e91);
				background-image: -webkit-linear-gradient(to right, #5e42a6, #b74e91);
				background-image: -ms-linear-gradient(to right, #5e42a6, #b74e91);
				background-image: linear-gradient(to right, #5e42a6, #b74e91);
				-moz-transition: max-width 0.2s ease;
				-webkit-transition: max-width 0.2s ease;
				-ms-transition: max-width 0.2s ease;
				transition: max-width 0.2s ease;
				max-width: 0;
			}

			#sidebar nav a:hover {
				color: rgba(255, 255, 255, 0.55);
			}

			#sidebar nav a.active {
				color: #ffffff;
			}

				#sidebar nav a.active:after {
					max-width: 100%;
				}

		body.is-preload #sidebar > .inner {
			opacity: 0;
		}

		body.is-preload #sidebar nav ul li {
			-moz-transform: translateY(2em);
			-webkit-transform: translateY(2em);
			-ms-transform: translateY(2em);
			transform: translateY(2em);
			opacity: 0;
		}

		@media screen and (max-width: 1280px) {

			#sidebar {
				height: 3.5em;
				left: 0;
				line-height: 3.5em;
				overflow: hidden;
				padding: 0;
				text-align: center;
				top: 0;
				width: 100%;
			}

				#sidebar > .inner {
					-moz-flex-direction: row;
					-webkit-flex-direction: row;
					-ms-flex-direction: row;
					flex-direction: row;
					-moz-align-items: -moz-stretch;
					-webkit-align-items: -webkit-stretch;
					-ms-align-items: -ms-stretch;
					align-items: stretch;
					height: inherit;
					line-height: inherit;
				}

				#sidebar nav {
					height: inherit;
					line-height: inherit;
				}

					#sidebar nav ul {
						display: -moz-flex;
						display: -webkit-flex;
						display: -ms-flex;
						display: flex;
						height: inherit;
						line-height: inherit;
						margin: 0;
					}

						#sidebar nav ul li {
							display: block;
							height: inherit;
							line-height: inherit;
							margin: 0 0 0 2em;
							padding: 0;
						}

					#sidebar nav a {
						height: inherit;
						line-height: inherit;
						padding: 0;
					}

						#sidebar nav a:after {
							background-image: none;
							background-color: #b74e91;
						}

		}

		@media screen and (max-width: 736px) {

			#sidebar {
				display: none;
			}

		}

/* Intro */

	#intro {
		background-attachment: fixed;
		background-image: url("images/intro.svg");
		background-position: top right;
		background-repeat: no-repeat;
		background-size: 100% 100%;
	}

		#intro p {
			font-size: 1.25em;
		}

			@media screen and (max-width: 980px) {

				#intro p br {
					display: none;
				}

			}

			@media screen and (max-width: 736px) {

				#intro p {
					font-size: 1em;
				}

			}

		@media screen and (max-width: 1280px) {

			#intro {
				background-attachment: scroll;
			}

		}""", "lime":"""""", 
			"sakura":"""""", 
			"valley":"""""", 
			"elegant":"""""",
			"phantom":""""""
}, 
"strata":
{ "valley":"""#main
	{
		background-color: #1A3636;
	}
	#header
	{
		background-color: #40534C;
	}""",
	"default":"""@import url("fontawesome-all.min.css");
@import url("https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400italic");


html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #fff;
	}

		body.is-preload *, body.is-preload *:before, body.is-preload *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

	body, input, select, textarea {
		color: #a2a2a2;
		font-family: "Source Sans Pro", Helvetica, sans-serif;
		font-size: 16pt;
		font-weight: 400;
		line-height: 1.75em;
	}

	a {
		-moz-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-webkit-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-ms-transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		border-bottom: dotted 1px;
		color: #49bf9d;
		text-decoration: none;
	}

		a:hover {
			border-bottom-color: transparent;
			color: #49bf9d !important;
			text-decoration: none;
		}

	strong, b {
		color: #787878;
		font-weight: 400;
	}

	em, i {
		font-style: italic;
	}

	p {
		margin: 0 0 2em 0;
	}

	h1, h2, h3, h4, h5, h6 {
		color: #787878;
		font-weight: 400;
		line-height: 1em;
		margin: 0 0 1em 0;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			color: inherit;
			text-decoration: none;
		}

	h1 {
		font-size: 2em;
		line-height: 1.5em;
	}

	h2 {
		font-size: 1.5em;
		line-height: 1.5em;
	}

	h3 {
		font-size: 1.25em;
		line-height: 1.5em;
	}

	h4 {
		font-size: 1.1em;
		line-height: 1.5em;
	}

	h5 {
		font-size: 0.9em;
		line-height: 1.5em;
	}

	h6 {
		font-size: 0.7em;
		line-height: 1.5em;
	}

	sub {
		font-size: 0.8em;
		position: relative;
		top: 0.5em;
	}

	sup {
		font-size: 0.8em;
		position: relative;
		top: -0.5em;
	}

	hr {
		border: 0;
		border-bottom: solid 2px #efefef;
		margin: 2em 0;
	}

		hr.major {
			margin: 3em 0;
		}

	blockquote {
		border-left: solid 6px #efefef;
		font-style: italic;
		margin: 0 0 2em 0;
		padding: 0.5em 0 0.5em 1.5em;
	}

	code {
		background: #f7f7f7;
		border-radius: 0.35em;
		border: solid 2px #efefef;
		font-family: "Courier New", monospace;
		font-size: 0.9em;
		margin: 0 0.25em;
		padding: 0.25em 0.65em;
	}

	pre {
		-webkit-overflow-scrolling: touch;
		font-family: "Courier New", monospace;
		font-size: 0.9em;
		margin: 0 0 2em 0;
	}

		pre code {
			display: block;
			line-height: 1.75em;
			padding: 1em 1.5em;
			overflow-x: auto;
		}

	.align-left {
		text-align: left;
	}

	.align-center {
		text-align: center;
	}

	.align-right {
		text-align: right;
	}

/* Container */

	.container {
		margin: 0 auto;
		max-width: calc(100% - 4em);
		width: 100%;
	}

		.container.xsmall {
			width: 25%;
		}

		.container.small {
			width: 50%;
		}

		.container.medium {
			width: 75%;
		}

		.container.large {
			width: 125%;
		}

		.container.xlarge {
			width: 150%;
		}

		.container.max {
			width: 100%;
		}

		@media screen and (max-width: 980px) {

			.container {
				width: 100% !important;
				max-width: 100% !important;
			}

		}

		@media screen and (max-width: 480px) {

			.container {
				max-width: calc(100% - 3em);
			}

		}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0;
			margin-left: 0em;
		}

			.row.gtr-0 > * {
				padding: 0 0 0 0em;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0em;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0em;
				}

		.row.gtr-25 {
			margin-top: 0;
			margin-left: -0.625em;
		}

			.row.gtr-25 > * {
				padding: 0 0 0 0.625em;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -0.625em;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 0.625em;
				}

		.row.gtr-50 {
			margin-top: 0;
			margin-left: -1.25em;
		}

			.row.gtr-50 > * {
				padding: 0 0 0 1.25em;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -1.25em;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 1.25em;
				}

		.row {
			margin-top: 0;
			margin-left: -2.5em;
		}

			.row > * {
				padding: 0 0 0 2.5em;
			}

			.row.gtr-uniform {
				margin-top: -2.5em;
			}

				.row.gtr-uniform > * {
					padding-top: 2.5em;
				}

		.row.gtr-150 {
			margin-top: 0;
			margin-left: -3.75em;
		}

			.row.gtr-150 > * {
				padding: 0 0 0 3.75em;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -3.75em;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 3.75em;
				}

		.row.gtr-200 {
			margin-top: 0;
			margin-left: -5em;
		}

			.row.gtr-200 > * {
				padding: 0 0 0 5em;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -5em;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 5em;
				}

		@media screen and (max-width: 1800px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xlarge {
					order: -1;
				}

				.row > .col-1-xlarge {
					width: 8.33333%;
				}

				.row > .off-1-xlarge {
					margin-left: 8.33333%;
				}

				.row > .col-2-xlarge {
					width: 16.66667%;
				}

				.row > .off-2-xlarge {
					margin-left: 16.66667%;
				}

				.row > .col-3-xlarge {
					width: 25%;
				}

				.row > .off-3-xlarge {
					margin-left: 25%;
				}

				.row > .col-4-xlarge {
					width: 33.33333%;
				}

				.row > .off-4-xlarge {
					margin-left: 33.33333%;
				}

				.row > .col-5-xlarge {
					width: 41.66667%;
				}

				.row > .off-5-xlarge {
					margin-left: 41.66667%;
				}

				.row > .col-6-xlarge {
					width: 50%;
				}

				.row > .off-6-xlarge {
					margin-left: 50%;
				}

				.row > .col-7-xlarge {
					width: 58.33333%;
				}

				.row > .off-7-xlarge {
					margin-left: 58.33333%;
				}

				.row > .col-8-xlarge {
					width: 66.66667%;
				}

				.row > .off-8-xlarge {
					margin-left: 66.66667%;
				}

				.row > .col-9-xlarge {
					width: 75%;
				}

				.row > .off-9-xlarge {
					margin-left: 75%;
				}

				.row > .col-10-xlarge {
					width: 83.33333%;
				}

				.row > .off-10-xlarge {
					margin-left: 83.33333%;
				}

				.row > .col-11-xlarge {
					width: 91.66667%;
				}

				.row > .off-11-xlarge {
					margin-left: 91.66667%;
				}

				.row > .col-12-xlarge {
					width: 100%;
				}

				.row > .off-12-xlarge {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.625em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.625em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.625em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.625em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -1.25em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 1.25em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -1.25em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 1.25em;
						}

				.row {
					margin-top: 0;
					margin-left: -2.5em;
				}

					.row > * {
						padding: 0 0 0 2.5em;
					}

					.row.gtr-uniform {
						margin-top: -2.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 2.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -3.75em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 3.75em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -3.75em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 3.75em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -5em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 5em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -5em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 5em;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-large {
					order: -1;
				}

				.row > .col-1-large {
					width: 8.33333%;
				}

				.row > .off-1-large {
					margin-left: 8.33333%;
				}

				.row > .col-2-large {
					width: 16.66667%;
				}

				.row > .off-2-large {
					margin-left: 16.66667%;
				}

				.row > .col-3-large {
					width: 25%;
				}

				.row > .off-3-large {
					margin-left: 25%;
				}

				.row > .col-4-large {
					width: 33.33333%;
				}

				.row > .off-4-large {
					margin-left: 33.33333%;
				}

				.row > .col-5-large {
					width: 41.66667%;
				}

				.row > .off-5-large {
					margin-left: 41.66667%;
				}

				.row > .col-6-large {
					width: 50%;
				}

				.row > .off-6-large {
					margin-left: 50%;
				}

				.row > .col-7-large {
					width: 58.33333%;
				}

				.row > .off-7-large {
					margin-left: 58.33333%;
				}

				.row > .col-8-large {
					width: 66.66667%;
				}

				.row > .off-8-large {
					margin-left: 66.66667%;
				}

				.row > .col-9-large {
					width: 75%;
				}

				.row > .off-9-large {
					margin-left: 75%;
				}

				.row > .col-10-large {
					width: 83.33333%;
				}

				.row > .off-10-large {
					margin-left: 83.33333%;
				}

				.row > .col-11-large {
					width: 91.66667%;
				}

				.row > .off-11-large {
					margin-left: 91.66667%;
				}

				.row > .col-12-large {
					width: 100%;
				}

				.row > .off-12-large {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -1em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 1em;
						}

				.row {
					margin-top: 0;
					margin-left: -2em;
				}

					.row > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-uniform > * {
							padding-top: 2em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 3em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -4em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 4em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -4em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 4em;
						}

		}

		@media screen and (max-width: 980px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-medium {
					order: -1;
				}

				.row > .col-1-medium {
					width: 8.33333%;
				}

				.row > .off-1-medium {
					margin-left: 8.33333%;
				}

				.row > .col-2-medium {
					width: 16.66667%;
				}

				.row > .off-2-medium {
					margin-left: 16.66667%;
				}

				.row > .col-3-medium {
					width: 25%;
				}

				.row > .off-3-medium {
					margin-left: 25%;
				}

				.row > .col-4-medium {
					width: 33.33333%;
				}

				.row > .off-4-medium {
					margin-left: 33.33333%;
				}

				.row > .col-5-medium {
					width: 41.66667%;
				}

				.row > .off-5-medium {
					margin-left: 41.66667%;
				}

				.row > .col-6-medium {
					width: 50%;
				}

				.row > .off-6-medium {
					margin-left: 50%;
				}

				.row > .col-7-medium {
					width: 58.33333%;
				}

				.row > .off-7-medium {
					margin-left: 58.33333%;
				}

				.row > .col-8-medium {
					width: 66.66667%;
				}

				.row > .off-8-medium {
					margin-left: 66.66667%;
				}

				.row > .col-9-medium {
					width: 75%;
				}

				.row > .off-9-medium {
					margin-left: 75%;
				}

				.row > .col-10-medium {
					width: 83.33333%;
				}

				.row > .off-10-medium {
					margin-left: 83.33333%;
				}

				.row > .col-11-medium {
					width: 91.66667%;
				}

				.row > .off-11-medium {
					margin-left: 91.66667%;
				}

				.row > .col-12-medium {
					width: 100%;
				}

				.row > .off-12-medium {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.5em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.5em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.5em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.5em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -1em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 1em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -1em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 1em;
						}

				.row {
					margin-top: 0;
					margin-left: -2em;
				}

					.row > * {
						padding: 0 0 0 2em;
					}

					.row.gtr-uniform {
						margin-top: -2em;
					}

						.row.gtr-uniform > * {
							padding-top: 2em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 3em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -4em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 4em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -4em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 4em;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-small {
					order: -1;
				}

				.row > .col-1-small {
					width: 8.33333%;
				}

				.row > .off-1-small {
					margin-left: 8.33333%;
				}

				.row > .col-2-small {
					width: 16.66667%;
				}

				.row > .off-2-small {
					margin-left: 16.66667%;
				}

				.row > .col-3-small {
					width: 25%;
				}

				.row > .off-3-small {
					margin-left: 25%;
				}

				.row > .col-4-small {
					width: 33.33333%;
				}

				.row > .off-4-small {
					margin-left: 33.33333%;
				}

				.row > .col-5-small {
					width: 41.66667%;
				}

				.row > .off-5-small {
					margin-left: 41.66667%;
				}

				.row > .col-6-small {
					width: 50%;
				}

				.row > .off-6-small {
					margin-left: 50%;
				}

				.row > .col-7-small {
					width: 58.33333%;
				}

				.row > .off-7-small {
					margin-left: 58.33333%;
				}

				.row > .col-8-small {
					width: 66.66667%;
				}

				.row > .off-8-small {
					margin-left: 66.66667%;
				}

				.row > .col-9-small {
					width: 75%;
				}

				.row > .off-9-small {
					margin-left: 75%;
				}

				.row > .col-10-small {
					width: 83.33333%;
				}

				.row > .off-10-small {
					margin-left: 83.33333%;
				}

				.row > .col-11-small {
					width: 91.66667%;
				}

				.row > .off-11-small {
					margin-left: 91.66667%;
				}

				.row > .col-12-small {
					width: 100%;
				}

				.row > .off-12-small {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

		@media screen and (max-width: 480px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xsmall {
					order: -1;
				}

				.row > .col-1-xsmall {
					width: 8.33333%;
				}

				.row > .off-1-xsmall {
					margin-left: 8.33333%;
				}

				.row > .col-2-xsmall {
					width: 16.66667%;
				}

				.row > .off-2-xsmall {
					margin-left: 16.66667%;
				}

				.row > .col-3-xsmall {
					width: 25%;
				}

				.row > .off-3-xsmall {
					margin-left: 25%;
				}

				.row > .col-4-xsmall {
					width: 33.33333%;
				}

				.row > .off-4-xsmall {
					margin-left: 33.33333%;
				}

				.row > .col-5-xsmall {
					width: 41.66667%;
				}

				.row > .off-5-xsmall {
					margin-left: 41.66667%;
				}

				.row > .col-6-xsmall {
					width: 50%;
				}

				.row > .off-6-xsmall {
					margin-left: 50%;
				}

				.row > .col-7-xsmall {
					width: 58.33333%;
				}

				.row > .off-7-xsmall {
					margin-left: 58.33333%;
				}

				.row > .col-8-xsmall {
					width: 66.66667%;
				}

				.row > .off-8-xsmall {
					margin-left: 66.66667%;
				}

				.row > .col-9-xsmall {
					width: 75%;
				}

				.row > .off-9-xsmall {
					margin-left: 75%;
				}

				.row > .col-10-xsmall {
					width: 83.33333%;
				}

				.row > .off-10-xsmall {
					margin-left: 83.33333%;
				}

				.row > .col-11-xsmall {
					width: 91.66667%;
				}

				.row > .off-11-xsmall {
					margin-left: 91.66667%;
				}

				.row > .col-12-xsmall {
					width: 100%;
				}

				.row > .off-12-xsmall {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0;
					margin-left: 0em;
				}

					.row.gtr-0 > * {
						padding: 0 0 0 0em;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0em;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0em;
						}

				.row.gtr-25 {
					margin-top: 0;
					margin-left: -0.375em;
				}

					.row.gtr-25 > * {
						padding: 0 0 0 0.375em;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -0.375em;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 0.375em;
						}

				.row.gtr-50 {
					margin-top: 0;
					margin-left: -0.75em;
				}

					.row.gtr-50 > * {
						padding: 0 0 0 0.75em;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -0.75em;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 0.75em;
						}

				.row {
					margin-top: 0;
					margin-left: -1.5em;
				}

					.row > * {
						padding: 0 0 0 1.5em;
					}

					.row.gtr-uniform {
						margin-top: -1.5em;
					}

						.row.gtr-uniform > * {
							padding-top: 1.5em;
						}

				.row.gtr-150 {
					margin-top: 0;
					margin-left: -2.25em;
				}

					.row.gtr-150 > * {
						padding: 0 0 0 2.25em;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -2.25em;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 2.25em;
						}

				.row.gtr-200 {
					margin-top: 0;
					margin-left: -3em;
				}

					.row.gtr-200 > * {
						padding: 0 0 0 3em;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -3em;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 3em;
						}

		}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header p {
		color: #b2b2b2;
		position: relative;
		margin: 0 0 1.5em 0;
	}

	header h2 + p {
		font-size: 1.25em;
		margin-top: -1em;
		line-height: 1.5em;
	}

	header h3 + p {
		font-size: 1.1em;
		margin-top: -0.8em;
		line-height: 1.5em;
	}

	header h4 + p,
	header h5 + p,
	header h6 + p {
		font-size: 0.9em;
		margin-top: -0.6em;
		line-height: 1.5em;
	}

	header.major h2 {
		font-size: 2em;
	}

/* Form */

	form {
		margin: 0 0 2em 0;
	}

	label {
		color: #787878;
		display: block;
		font-size: 0.9em;
		font-weight: 400;
		margin: 0 0 1em 0;
	}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select,
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		background: #f7f7f7;
		border-radius: 0.35em;
		border: solid 2px transparent;
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 0.75em;
		text-decoration: none;
		width: 100%;
	}

		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		select:focus,
		textarea:focus {
			border-color: #49bf9d;
		}

	select {
		background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' preserveAspectRatio='none' viewBox='0 0 40 40'%3E%3Cpath d='M9.4,12.3l10.4,10.4l10.4-10.4c0.2-0.2,0.5-0.4,0.9-0.4c0.3,0,0.6,0.1,0.9,0.4l3.3,3.3c0.2,0.2,0.4,0.5,0.4,0.9 c0,0.4-0.1,0.6-0.4,0.9L20.7,31.9c-0.2,0.2-0.5,0.4-0.9,0.4c-0.3,0-0.6-0.1-0.9-0.4L4.3,17.3c-0.2-0.2-0.4-0.5-0.4-0.9 c0-0.4,0.1-0.6,0.4-0.9l3.3-3.3c0.2-0.2,0.5-0.4,0.9-0.4S9.1,12.1,9.4,12.3z' fill='%23dfdfdf' /%3E%3C/svg%3E");
		background-size: 1.25rem;
		background-repeat: no-repeat;
		background-position: calc(100% - 1rem) center;
		height: 2.75em;
		padding-right: 2.75em;
		text-overflow: ellipsis;
	}

		select option {
			color: #787878;
			background: #fff;
		}

		select:focus::-ms-value {
			background-color: transparent;
		}

		select::-ms-expand {
			display: none;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 2.75em;
	}

	textarea {
		padding: 0.75em;
	}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2em;
		opacity: 0;
		width: 1em;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			color: #a2a2a2;
			cursor: pointer;
			display: inline-block;
			font-size: 1em;
			font-weight: 400;
			padding-left: 2.4em;
			padding-right: 0.75em;
			position: relative;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				background: #f7f7f7;
				border-radius: 0.35em;
				border: solid 2px transparent;
				content: '';
				display: inline-block;
				font-size: 0.8em;
				height: 2.0625em;
				left: 0;
				line-height: 1.85625em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 2.0625em;
			}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			background: #787878;
			border-color: #787878;
			color: #fff;
			content: '\\f00c';
		}

		input[type="checkbox"]:focus + label:before,
		input[type="radio"]:focus + label:before {
			border-color: #49bf9d;
		}

	input[type="checkbox"] + label:before {
		border-radius: 0.35em;
	}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		color: #b2b2b2 !important;
		opacity: 1.0;
	}

	:-moz-placeholder {
		color: #b2b2b2 !important;
		opacity: 1.0;
	}

	::-moz-placeholder {
		color: #b2b2b2 !important;
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		color: #b2b2b2 !important;
		opacity: 1.0;
	}

/* Box */

	.box {
		border-radius: 0.35em;
		border: solid 2px #efefef;
		margin-bottom: 2em;
		padding: 1.5em;
	}

		.box > :last-child,
		.box > :last-child > :last-child,
		.box > :last-child > :last-child > :last-child {
			margin-bottom: 0;
		}

		.box.alt {
			border: 0;
			border-radius: 0;
			padding: 0;
		}

/* Icon */

	.icon {
		text-decoration: none;
		border-bottom: none;
		position: relative;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 400;
		}

		.icon > .label {
			display: none;
		}

		.icon:before {
			line-height: inherit;
		}

		.icon.solid:before {
			font-weight: 900;
		}

		.icon.brands:before {
			font-family: 'Font Awesome 5 Brands';
		}

/* Image */

	.image {
		border-radius: 0.35em;
		border: 0;
		display: inline-block;
		position: relative;
	}

		.image:before {
			-moz-transition: opacity 0.2s ease-in-out;
			-webkit-transition: opacity 0.2s ease-in-out;
			-ms-transition: opacity 0.2s ease-in-out;
			transition: opacity 0.2s ease-in-out;
			background: url("images/overlay.png");
			border-radius: 0.35em;
			content: '';
			display: block;
			height: 100%;
			left: 0;
			opacity: 0.5;
			position: absolute;
			top: 0;
			width: 100%;
		}

		.image.thumb {
			text-align: center;
		}

			.image.thumb:after {
				-moz-transition: opacity 0.2s ease-in-out;
				-webkit-transition: opacity 0.2s ease-in-out;
				-ms-transition: opacity 0.2s ease-in-out;
				transition: opacity 0.2s ease-in-out;
				border-radius: 0.35em;
				border: solid 3px rgba(255, 255, 255, 0.5);
				color: #fff;
				content: 'View';
				display: inline-block;
				font-size: 0.8em;
				font-weight: 400;
				left: 50%;
				line-height: 2.25em;
				margin: -1.25em 0 0 -3em;
				opacity: 0;
				padding: 0 1.5em;
				position: absolute;
				text-align: center;
				text-decoration: none;
				top: 50%;
				white-space: nowrap;
			}

			.image.thumb:hover:after {
				opacity: 1.0;
			}

			.image.thumb:hover:before {
				background: url("images/overlay.png"), url("images/overlay.png");
				opacity: 1.0;
			}

		.image img {
			border-radius: 0.35em;
			display: block;
		}

		.image.left {
			float: left;
			margin: 0 1.5em 1em 0;
			top: 0.25em;
		}

		.image.right {
			float: right;
			margin: 0 0 1em 1.5em;
			top: 0.25em;
		}

		.image.left, .image.right {
			max-width: 40%;
		}

			.image.left img, .image.right img {
				width: 100%;
			}

		.image.fit {
			display: block;
			margin: 0 0 2em 0;
			width: 100%;
		}

			.image.fit img {
				width: 100%;
			}

		.image.avatar {
			border-radius: 100%;
		}

			.image.avatar:before {
				display: none;
			}

			.image.avatar img {
				border-radius: 100%;
				width: 100%;
			}

/* List */

	ol {
		list-style: decimal;
		margin: 0 0 2em 0;
		padding-left: 1.25em;
	}

		ol li {
			padding-left: 0.25em;
		}

	ul {
		list-style: disc;
		margin: 0 0 2em 0;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
		}

		ul.alt {
			list-style: none;
			padding-left: 0;
		}

			ul.alt li {
				border-top: solid 2px #efefef;
				padding: 0.5em 0;
			}

				ul.alt li:first-child {
					border-top: 0;
					padding-top: 0;
				}

	dl {
		margin: 0 0 2em 0;
	}

/* Icons */

	ul.icons {
		cursor: default;
		list-style: none;
		padding-left: 0;
	}

		ul.icons li {
			display: inline-block;
			padding: 0 1em 0 0;
		}

			ul.icons li:last-child {
				padding-right: 0;
			}

			ul.icons li .icon:before {
				font-size: 1.5em;
			}

/* Labeled Icons */

	ul.labeled-icons {
		list-style: none;
		padding: 0;
	}

		ul.labeled-icons li {
			line-height: 1.75em;
			margin: 1.5em 0 0 0;
			padding-left: 2.25em;
			position: relative;
		}

			ul.labeled-icons li:first-child {
				margin-top: 0;
			}

			ul.labeled-icons li a {
				color: inherit;
			}

			ul.labeled-icons li h3 {
				color: #b2b2b2;
				left: 0;
				position: absolute;
				text-align: center;
				top: 0;
				width: 1em;
			}

/* Actions */

	ul.actions {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		cursor: default;
		list-style: none;
		margin-left: -1em;
		padding-left: 0;
	}

		ul.actions li {
			padding: 0 0 0 1em;
			vertical-align: middle;
		}

		ul.actions.special {
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 100%;
			margin-left: 0;
		}

			ul.actions.special li:first-child {
				padding-left: 0;
			}

		ul.actions.stacked {
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			margin-left: 0;
		}

			ul.actions.stacked li {
				padding: 1.3em 0 0 0;
			}

				ul.actions.stacked li:first-child {
					padding-top: 0;
				}

		ul.actions.fit {
			width: calc(100% + 1em);
		}

			ul.actions.fit li {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				width: 100%;
			}

				ul.actions.fit li > * {
					width: 100%;
				}

			ul.actions.fit.stacked {
				width: 100%;
			}

		@media screen and (max-width: 480px) {

			ul.actions:not(.fixed) {
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
				margin-left: 0;
				width: 100% !important;
			}

				ul.actions:not(.fixed) li {
					-moz-flex-grow: 1;
					-webkit-flex-grow: 1;
					-ms-flex-grow: 1;
					flex-grow: 1;
					-moz-flex-shrink: 1;
					-webkit-flex-shrink: 1;
					-ms-flex-shrink: 1;
					flex-shrink: 1;
					padding: 1em 0 0 0;
					text-align: center;
					width: 100%;
				}

					ul.actions:not(.fixed) li > * {
						width: 100%;
					}

					ul.actions:not(.fixed) li:first-child {
						padding-top: 0;
					}

					ul.actions:not(.fixed) li input[type="submit"],
					ul.actions:not(.fixed) li input[type="reset"],
					ul.actions:not(.fixed) li input[type="button"],
					ul.actions:not(.fixed) li button,
					ul.actions:not(.fixed) li .button {
						width: 100%;
					}

						ul.actions:not(.fixed) li input[type="submit"].icon:before,
						ul.actions:not(.fixed) li input[type="reset"].icon:before,
						ul.actions:not(.fixed) li input[type="button"].icon:before,
						ul.actions:not(.fixed) li button.icon:before,
						ul.actions:not(.fixed) li .button.icon:before {
							margin-left: -0.5em;
						}

		}

/* Table */

	.table-wrapper {
		-webkit-overflow-scrolling: touch;
		overflow-x: auto;
	}

	table {
		margin: 0 0 2em 0;
		width: 100%;
	}

		table tbody tr {
			border: solid 1px #efefef;
			border-left: 0;
			border-right: 0;
		}

			table tbody tr:nth-child(2n + 1) {
				background-color: #f7f7f7;
			}

		table td {
			padding: 0.75em 0.75em;
		}

		table th {
			color: #787878;
			font-size: 0.9em;
			font-weight: 400;
			padding: 0 0.75em 0.75em 0.75em;
			text-align: left;
		}

		table thead {
			border-bottom: solid 2px #efefef;
		}

		table tfoot {
			border-top: solid 2px #efefef;
		}

		table.alt {
			border-collapse: separate;
		}

			table.alt tbody tr td {
				border: solid 2px #efefef;
				border-left-width: 0;
				border-top-width: 0;
			}

				table.alt tbody tr td:first-child {
					border-left-width: 2px;
				}

			table.alt tbody tr:first-child td {
				border-top-width: 2px;
			}

			table.alt thead {
				border-bottom: 0;
			}

			table.alt tfoot {
				border-top: 0;
			}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out;
		background-color: transparent;
		border-radius: 0.35em;
		border: solid 3px #efefef;
		color: #787878 !important;
		cursor: pointer;
		display: inline-block;
		font-weight: 400;
		height: 3.15em;
		height: calc(2.75em + 6px);
		line-height: 2.75em;
		min-width: 10em;
		padding: 0 1.5em;
		text-align: center;
		text-decoration: none;
		white-space: nowrap;
	}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		.button:hover {
			border-color: #49bf9d;
			color: #49bf9d !important;
		}

		input[type="submit"]:active,
		input[type="reset"]:active,
		input[type="button"]:active,
		.button:active {
			background-color: rgba(73, 191, 157, 0.1);
			border-color: #49bf9d;
			color: #49bf9d !important;
		}

		input[type="submit"].icon,
		input[type="reset"].icon,
		input[type="button"].icon,
		.button.icon {
			padding-left: 1.35em;
		}

			input[type="submit"].icon:before,
			input[type="reset"].icon:before,
			input[type="button"].icon:before,
			.button.icon:before {
				margin-right: 0.5em;
			}

		input[type="submit"].fit,
		input[type="reset"].fit,
		input[type="button"].fit,
		.button.fit {
			min-width: 0;
			width: 100%;
		}

		input[type="submit"].small,
		input[type="reset"].small,
		input[type="button"].small,
		.button.small {
			font-size: 0.8em;
		}

		input[type="submit"].large,
		input[type="reset"].large,
		input[type="button"].large,
		.button.large {
			font-size: 1.35em;
		}

		input[type="submit"].primary,
		input[type="reset"].primary,
		input[type="button"].primary,
		.button.primary {
			background-color: #49bf9d;
			border-color: #49bf9d;
			color: #ffffff !important;
		}

			input[type="submit"].primary:hover,
			input[type="reset"].primary:hover,
			input[type="button"].primary:hover,
			.button.primary:hover {
				background-color: #5cc6a7;
				border-color: #5cc6a7;
			}

			input[type="submit"].primary:active,
			input[type="reset"].primary:active,
			input[type="button"].primary:active,
			.button.primary:active {
				background-color: #3eb08f;
				border-color: #3eb08f;
			}

		input[type="submit"].disabled, input[type="submit"]:disabled,
		input[type="reset"].disabled,
		input[type="reset"]:disabled,
		input[type="button"].disabled,
		input[type="button"]:disabled,
		.button.disabled,
		.button:disabled {
			background-color: #e7e7e7 !important;
			border-color: #e7e7e7 !important;
			color: #b2b2b2 !important;
			cursor: default;
		}

/* Work Item */

	.work-item {
		margin: 0 0 2em 0;
	}

		.work-item .image {
			margin: 0 0 1.5em 0;
		}

		.work-item h3 {
			font-size: 1em;
			margin: 0 0 0.5em 0;
		}

		.work-item p {
			font-size: 0.8em;
			line-height: 1.5em;
			margin: 0;
		}

/* Header */

	#header {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: column;
		-webkit-flex-direction: column;
		-ms-flex-direction: column;
		flex-direction: column;
		-moz-align-items: -moz-flex-end;
		-webkit-align-items: -webkit-flex-end;
		-ms-align-items: -ms-flex-end;
		align-items: flex-end;
		-moz-justify-content: space-between;
		-webkit-justify-content: space-between;
		-ms-justify-content: space-between;
		justify-content: space-between;
		background-color: #1f1815;
		background-attachment: scroll,								scroll;
		background-image: url("images/overlay.png"), url("../../images/bg.jpg");
		background-position: top left,							top left;
		background-repeat: repeat,								no-repeat;
		background-size: auto,								150%;
		color: rgba(255, 255, 255, 0.5);
		height: 100%;
		left: 0;
		padding: 8em 4em;
		position: fixed;
		text-align: right;
		top: 0;
		width: 35%;
	}

		#header > * {
			-moz-flex-shrink: 0;
			-webkit-flex-shrink: 0;
			-ms-flex-shrink: 0;
			flex-shrink: 0;
			width: 100%;
		}

		#header > .inner {
			-moz-flex-grow: 1;
			-webkit-flex-grow: 1;
			-ms-flex-grow: 1;
			flex-grow: 1;
			margin: 0 0 2em 0;
		}

		#header strong, #header b {
			color: #ffffff;
		}

		#header h2, #header h3, #header h4, #header h5, #header h6 {
			color: #ffffff;
		}

		#header h1 {
			color: rgba(255, 255, 255, 0.5);
			font-size: 1.35em;
			line-height: 1.75em;
			margin: 0;
		}

		#header .image.avatar {
			margin: 0 0 1em 0;
			width: 6.25em;
		}

/* Footer */

	#footer .icons {
		margin: 1em 0 0 0;
	}

		#footer .icons a {
			color: rgba(255, 255, 255, 0.4);
		}

	#footer .copyright {
		color: rgba(255, 255, 255, 0.4);
		font-size: 0.8em;
		list-style: none;
		margin: 1em 0 0 0;
		padding: 0;
	}

		#footer .copyright li {
			border-left: solid 1px rgba(255, 255, 255, 0.25);
			display: inline-block;
			line-height: 1em;
			margin-left: 0.75em;
			padding-left: 0.75em;
		}

			#footer .copyright li:first-child {
				border-left: 0;
				margin-left: 0;
				padding-left: 0;
			}

			#footer .copyright li a {
				color: inherit;
			}

/* Main */

	#main {
		margin-left: 35%;
		max-width: 54em;
		padding: 8em 4em 4em 4em;
		width: calc(100% - 35%);
	}

		#main > section {
			border-top: solid 2px #efefef;
			margin: 4em 0 0 0;
			padding: 4em 0 0 0;
		}

			#main > section:first-child {
				border-top: 0;
				margin-top: 0;
				padding-top: 0;
			}

/* Poptrox */

	@-moz-keyframes spin {
		0% {
			-moz-transform: rotate(0deg);
			-webkit-transform: rotate(0deg);
			-ms-transform: rotate(0deg);
			transform: rotate(0deg);
		}

		100% {
			-moz-transform: rotate(360deg);
			-webkit-transform: rotate(360deg);
			-ms-transform: rotate(360deg);
			transform: rotate(360deg);
		}
	}

	@-webkit-keyframes spin {
		0% {
			-moz-transform: rotate(0deg);
			-webkit-transform: rotate(0deg);
			-ms-transform: rotate(0deg);
			transform: rotate(0deg);
		}

		100% {
			-moz-transform: rotate(360deg);
			-webkit-transform: rotate(360deg);
			-ms-transform: rotate(360deg);
			transform: rotate(360deg);
		}
	}

	@-ms-keyframes spin {
		0% {
			-moz-transform: rotate(0deg);
			-webkit-transform: rotate(0deg);
			-ms-transform: rotate(0deg);
			transform: rotate(0deg);
		}

		100% {
			-moz-transform: rotate(360deg);
			-webkit-transform: rotate(360deg);
			-ms-transform: rotate(360deg);
			transform: rotate(360deg);
		}
	}

	@keyframes spin {
		0% {
			-moz-transform: rotate(0deg);
			-webkit-transform: rotate(0deg);
			-ms-transform: rotate(0deg);
			transform: rotate(0deg);
		}

		100% {
			-moz-transform: rotate(360deg);
			-webkit-transform: rotate(360deg);
			-ms-transform: rotate(360deg);
			transform: rotate(360deg);
		}
	}

	.poptrox-popup {
		-moz-box-sizing: content-box;
		-webkit-box-sizing: content-box;
		-ms-box-sizing: content-box;
		box-sizing: content-box;
		-webkit-tap-highlight-color: rgba(255, 255, 255, 0);
		background: #fff;
		border-radius: 0.35em;
		box-shadow: 0 0.1em 0.15em 0 rgba(0, 0, 0, 0.15);
		overflow: hidden;
		padding-bottom: 3em;
	}

		.poptrox-popup .loader {
			text-decoration: none;
			-moz-animation: spin 1s linear infinite;
			-webkit-animation: spin 1s linear infinite;
			-ms-animation: spin 1s linear infinite;
			animation: spin 1s linear infinite;
			font-size: 1.5em;
			height: 1em;
			left: 50%;
			line-height: 1em;
			margin: -0.5em 0 0 -0.5em;
			position: absolute;
			top: 50%;
			width: 1em;
		}

			.poptrox-popup .loader:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			.poptrox-popup .loader:before {
				content: '\\f1ce';
			}

		.poptrox-popup .caption {
			background: #fff;
			bottom: 0;
			cursor: default;
			font-size: 0.9em;
			height: 3em;
			left: 0;
			line-height: 2.8em;
			position: absolute;
			text-align: center;
			width: 100%;
			z-index: 1;
		}

		.poptrox-popup .nav-next,
		.poptrox-popup .nav-previous {
			text-decoration: none;
			-moz-transition: opacity 0.2s ease-in-out;
			-webkit-transition: opacity 0.2s ease-in-out;
			-ms-transition: opacity 0.2s ease-in-out;
			transition: opacity 0.2s ease-in-out;
			-webkit-tap-highlight-color: rgba(255, 255, 255, 0);
			background: rgba(0, 0, 0, 0.01);
			cursor: pointer;
			height: 100%;
			opacity: 0;
			position: absolute;
			top: 0;
			width: 50%;
		}

			.poptrox-popup .nav-next:before,
			.poptrox-popup .nav-previous:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			.poptrox-popup .nav-next:before,
			.poptrox-popup .nav-previous:before {
				color: #fff;
				font-size: 2.5em;
				height: 1em;
				line-height: 1em;
				margin-top: -0.75em;
				position: absolute;
				text-align: center;
				top: 50%;
				width: 1.5em;
			}

		.poptrox-popup .nav-next {
			right: 0;
		}

			.poptrox-popup .nav-next:before {
				content: '\\f105';
				right: 0;
			}

		.poptrox-popup .nav-previous {
			left: 0;
		}

			.poptrox-popup .nav-previous:before {
				content: '\\f104';
				left: 0;
			}

		.poptrox-popup .closer {
			text-decoration: none;
			-moz-transition: opacity 0.2s ease-in-out;
			-webkit-transition: opacity 0.2s ease-in-out;
			-ms-transition: opacity 0.2s ease-in-out;
			transition: opacity 0.2s ease-in-out;
			-webkit-tap-highlight-color: rgba(255, 255, 255, 0);
			color: #fff;
			height: 4em;
			line-height: 4em;
			opacity: 0;
			position: absolute;
			right: 0;
			text-align: center;
			top: 0;
			width: 4em;
			z-index: 2;
		}

			.poptrox-popup .closer:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			.poptrox-popup .closer:before {
				-moz-box-sizing: content-box;
				-webkit-box-sizing: content-box;
				-ms-box-sizing: content-box;
				box-sizing: content-box;
				border-radius: 100%;
				border: solid 3px rgba(255, 255, 255, 0.5);
				content: '\\f00d';
				display: block;
				font-size: 1em;
				height: 1.75em;
				left: 50%;
				line-height: 1.75em;
				margin: -0.875em 0 0 -0.875em;
				position: absolute;
				top: 50%;
				width: 1.75em;
			}

		.poptrox-popup:hover .nav-next,
		.poptrox-popup:hover .nav-previous {
			opacity: 0.5;
		}

			.poptrox-popup:hover .nav-next:hover,
			.poptrox-popup:hover .nav-previous:hover {
				opacity: 1.0;
			}

		.poptrox-popup:hover .closer {
			opacity: 0.5;
		}

			.poptrox-popup:hover .closer:hover {
				opacity: 1.0;
			}

/* Touch */

	body.is-touch .image.thumb:before {
		opacity: 0.5 !important;
	}

	body.is-touch .image.thumb:after {
		display: none !important;
	}

	body.is-touch #header {
		background-attachment: scroll;
		background-size: auto, cover;
	}

	body.is-touch .poptrox-popup .nav-next,
	body.is-touch .poptrox-popup .nav-previous,
	body.is-touch .poptrox-popup .closer {
		opacity: 1.0 !important;
	}

/* XLarge */

	@media screen and (max-width: 1800px) {

		/* Basic */

			body, input, select, textarea {
				font-size: 12pt;
			}

	}

/* Large */

	@media screen and (max-width: 1280px) {

		/* Header */

			#header {
				padding: 6em 3em 3em 3em;
				width: 30%;
			}

				#header h1 {
					font-size: 1.25em;
				}

					#header h1 br {
						display: none;
					}

				#header > .inner {
					margin-bottom: 0;
				}

		/* Footer */

			#footer .copyright li {
				border-left-width: 0;
				display: block;
				line-height: 2.25em;
				margin-left: 0;
				padding-left: 0;
			}

		/* Main */

			#main {
				margin-left: 30%;
				max-width: none;
				padding: 6em 3em 3em 3em;
				width: calc(100% - 30%);
			}

	}

/* Medium */

	@media screen and (max-width: 980px) {

		/* Basic */

			h1 br, h2 br, h3 br, h4 br, h5 br, h6 br {
				display: none;
			}

		/* List */

			ul.icons li .icon {
				font-size: 1.25em;
			}

		/* Header */

			#header {
				background-attachment: scroll;
				background-position: top left, center center;
				background-size: auto,		cover;
				left: auto;
				padding: 6em 4em;
				position: relative;
				text-align: center;
				top: auto;
				width: 100%;
				display: block;
			}

				#header h1 {
					font-size: 1.75em;
				}

					#header h1 br {
						display: inline;
					}

		/* Footer */

			#footer {
				background-attachment: scroll;
				background-color: #1f1815;
				background-image: url("images/overlay.png"), url("../../images/bg.jpg");
				background-position: top left,						bottom center;
				background-repeat: repeat,							no-repeat;
				background-size: auto,							cover;
				bottom: auto;
				left: auto;
				padding: 4em 4em 6em 4em;
				position: relative;
				text-align: center;
				width: 100%;
			}

				#footer .icons {
					margin: 0 0 1em 0;
				}

				#footer .copyright {
					margin: 0 0 1em 0;
				}

					#footer .copyright li {
						border-left-width: 1px;
						display: inline-block;
						line-height: 1em;
						margin-left: 0.75em;
						padding-left: 0.75em;
					}

		/* Main */

			#main {
				margin: 0;
				padding: 6em 4em;
				width: 100%;
			}

	}

/* Small */

	@media screen and (max-width: 736px) {

		/* Basic */

			h1 {
				font-size: 1.5em;
			}

			h2 {
				font-size: 1.2em;
			}

			h3 {
				font-size: 1em;
			}

		/* Section/Article */

			section.special, article.special {
				text-align: center;
			}

			header.major h2 {
				font-size: 1.35em;
			}

		/* List */

			ul.labeled-icons li {
				padding-left: 2em;
			}

				ul.labeled-icons li h3 {
					line-height: 1.75em;
				}

		/* Header */

			#header {
				padding: 2.25em 1.5em;
			}

				#header h1 {
					font-size: 1.35em;
				}

		/* Footer */

			#footer {
				padding: 2.25em 1.5em;
			}

		/* Main */

			#main {
				padding: 2.25em 1.5em 0.25em 1.5em;
			}

				#main > section {
					margin: 2.25em 0 0 0;
					padding: 2.25em 0 0 0;
				}

		/* Poptrox */

			.poptrox-popup {
				border-radius: 0;
			}

				.poptrox-popup .nav-next:before,
				.poptrox-popup .nav-previous:before {
					margin-top: -1em;
				}

	}

/* XSmall */

	@media screen and (max-width: 480px) {

		/* Header */

			#header {
				padding: 4.5em 1.5em;
			}

				#header h1 br {
					display: none;
				}

		/* Footer */

			#footer .copyright li {
				border-left-width: 0;
				display: block;
				line-height: 2.25em;
				margin-left: 0;
				padding-left: 0;
			}

	}""", 
	"elegant":"""root {
    --light-yellow: #F6E96B;
    --light-green: #BEDC74;
    --forest-green: #FFDFD6;
}


/* Example usage */
body {
    background-color: var(--light-yellow);
    color: var(--forest-green);
}

.header {
    background-color: var(--light-green);
    color: var(--forest-green);
}

.button {
    background-color: var(--forest-green);
    color: #fff;
}

.button:hover {
    background-color: var(--light-green);
    color: var(--forest-green);
}
.dropotron li:hover > span, .dropotron li:hover > a {transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				color: #FFDFD6;
			}


	
	#header h1 {
			color: #FFDFD6;
		}
		.button:active {
			background: #FFDFD6;
		}

		.button {
		background: #FFDFD6;
		color: #fff 
	}
	a:hover {
			color: #FFDFD6;
			border-bottom-color: rgba(255, 255, 255, 0);
		}

			a:hover strong {
				color: #FFDFD6;
			}

	
	h1, h2, h3, h4, h5, h6 {
		color: #FF8225;
	}
	#banner
	{
		color:#FFDFD6;
	}
	input[type="button"], input[type="submit"], input[type="reset"], button, .button {
    background: #FF8225;
    }

input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #ed786a;
		color: #173B45 !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #173B45;
	}
	#header {
		background: #173B45;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #173B45, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #173B45;
			}
			.dropotron {
				background: #173B45;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #173B45;
			}
			#features {
				background: #173B45;
			}
			
	#banner {
		background: #173B45;
		color: #173B45;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #173B45, inset 0px 10px 0px 0px #e5e5e5;
	}
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #173B45, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #173B45;
	}
	#navPanel .link.depth-0 {
		color: #173B45;
	}
	
	#navPanel .depth-0 {
		color: #173B45;
	}""", 
	"sakura":"""root {
    --light-yellow: #F6E96B;
    --light-green: #BEDC74;
    --forest-green: #000000;
}


/* Example usage */
body
{
	color: #FFEBD4;
}

.header {
    background-color: var(--light-green);
    color: var(--forest-green);
}

.button {
    background-color: var(--forest-green);
    color: #fff;
}

.button:hover {
    background-color: var(--light-green);
    color: var(--forest-green);
}
.dropotron li:hover > span, .dropotron li:hover > a {transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				color: #FFDFD6;
			}


	
	#header h1 {
			color: #FFDFD6;
		}
		.button:active {
			background: #FFDFD6;
		}

		.button {
		background: #FFDFD6;
		color: #fff 
	}
	a:hover {
			color: #FFDFD6;
			border-bottom-color: rgba(255, 255, 255, 0);
		}

			a:hover strong {
				color: #FFDFD6;
			}

	
	h1, h2, h3, h4, h5, h6 {
		color: #FFC6C6;
	}
	input[type="button"], input[type="submit"], input[type="reset"], button, .button {
    background: #FF8225;
    }

input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #ed786a;
		color: #921A40 !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #921A40;
	}
	#header {
		background: #921A40;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #921A40, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #921A40;
			}
			.dropotron {
				background: #921A40;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #921A40;
			}
			#features {
				background: #921A40;
			}
			
	#banner {
		background: #921A40;
		color: #921A40;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #921A40, inset 0px 10px 0px 0px #e5e5e5;
	}
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #921A40, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #921A40;
	}
	#navPanel .link.depth-0 {
		color: #921A40;
	}
	#main {
		background: #C75B7A;
	}
	#navPanel .depth-0 {
		color: #921A40;
	}""", 
	"lime": """
root {
    --light-yellow: #F6E96B;
    --light-green: #BEDC74;
    --forest-green: #000000;
}


/* Example usage */
body
{
	color: #387F39;
}

.header {
    background-color: var(--light-green);
    color: var(--forest-green);
}

.button {
    background-color: var(--forest-green);
    color: #fff;
}

.button:hover {
    background-color: var(--light-green);
    color: var(--forest-green);
}
.dropotron li:hover > span, .dropotron li:hover > a {transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				color: #FFDFD6;
			}


	
	#header h1 {
			color: #FFDFD6;
		}
		.button:active {
			background: #FFDFD6;
		}

		.button {
		background: #FFDFD6;
		color: #fff 
	}
	a:hover {
			color: #FFDFD6;
			border-bottom-color: rgba(255, 255, 255, 0);
		}

			a:hover strong {
				color: #FFDFD6;
			}

	
	h1, h2, h3, h4, h5, h6 {
		color: #1A3636;
	}
	input[type="button"], input[type="submit"], input[type="reset"], button, .button {
    background: #FF8225;
    }

input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #BEDC74;
		color: #387F39 !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #387F39;
	}
	#header {
		background: #387F39;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #387F39, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #387F39;
			}
			.dropotron {
				background: #387F39;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #387F39;
			}
			#features {
				background: #387F39;
			}
			
	#banner {
		background: #387F39;
		color: #387F39;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #387F39, inset 0px 10px 0px 0px #e5e5e5;
	}
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #387F39, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #387F39;
	}
	#navPanel .link.depth-0 {
		color: #387F39;
	}
	#main {
		background: #F6E96B;
	}
	#navPanel .depth-0 {
		color: #387F39;
	}""", 
	"phantom":"""root {
    --light-yellow: #F6E96B;
    --light-green: #BEDC74;
    --forest-green: #000000;
}


/* Example usage */
body
{
	color: #C8ACD6;
}

.header {
    background-color: var(--light-green);
    color: var(--forest-green);
}

.button {
    background-color: var(--forest-green);
    color: #fff;
}

.button:hover {
    background-color: var(--light-green);
    color: var(--forest-green);
}
.dropotron li:hover > span, .dropotron li:hover > a {transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				color: #FFDFD6;
			}


	
	#header h1 {
			color: #FFDFD6;
		}
		.button:active {
			background: #FFDFD6;
		}

		.button {
		background: #FFDFD6;
		color: #fff 
	}
	a:hover {
			color: #FFDFD6;
			border-bottom-color: rgba(255, 255, 255, 0);
		}

			a:hover strong {
				color: #FFDFD6;
			}

	
	h1, h2, h3, h4, h5, h6 {
		color: #AF47D2;
	}
	input[type="button"], input[type="submit"], input[type="reset"], button, .button {
    background: #FF8225;
    }

input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #AF47D2;
		color: #17153B !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #17153B;
	}
	#header {
		background: #17153B;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #17153B, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #17153B;
			}
			.dropotron {
				background: #17153B;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #17153B;
			}
			#features {
				background: #17153B;
			}
			
	#banner {
		background: #17153B;
		color: #17153B;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #17153B, inset 0px 10px 0px 0px #e5e5e5;
	}
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #17153B, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #17153B;
	}
	#navPanel .link.depth-0 {
		color: #17153B;
	}
	#main {
		background: #2E236C;
	}
	#navPanel .depth-0 {
		color: #17153B;
	}"""
}, 
"vintage":{
	"default":"""@import url("fontawesome-all.min.css");
@import url("https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600|Arvo:700");
html, body, div, span, applet, object,
iframe, h1, h2, h3, h4, h5, h6, p, blockquote,
pre, a, abbr, acronym, address, big, cite,
code, del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var, b,
u, i, center, dl, dt, dd, ol, ul, li, fieldset,
form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside,
canvas, details, embed, figure, figcaption,
footer, header, hgroup, menu, nav, output, ruby,
section, summary, time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;}

article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;}

body {
	line-height: 1;
}

ol, ul {
	list-style: none;
}

blockquote, q {
	quotes: none;
}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

table {
	border-collapse: collapse;
	border-spacing: 0;
}

body {
	-webkit-text-size-adjust: none;
}

mark {
	background-color: transparent;
	color: inherit;
}

input::-moz-focus-inner {
	border: 0;
	padding: 0;
}

input, select, textarea {
	-moz-appearance: none;
	-webkit-appearance: none;
	-ms-appearance: none;
	appearance: none;
}

/* Basic */

	html {
		box-sizing: border-box;
	}

	*, *:before, *:after {
		box-sizing: inherit;
	}

	body {
		background: #f0f0f0;
	}

		body.is-preload *, body.is-preload *:before, body.is-preload *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

	body, input, textarea, select {
		font-family: 'Source Sans Pro';
		font-weight: 300;
		color: #777;
		line-height: 1.65em;
		font-size: 15pt;
	}

	h1, h2, h3, h4, h5, h6 {
		font-weight: 600;
		text-transform: uppercase;
		color: #888;
	}

	h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
		color: inherit;
		text-decoration: none;
		border: 0;
	}

	h2 {
		font-size: 1.65em;
		font-weight: 400;
		letter-spacing: 4px;
		margin: 0 0 1.5em 0;
		line-height: 1.75em;
	}

	h3 {
		font-size: 1em;
		letter-spacing: 2px;
		margin: 0 0 1.25em 0;
	}

	a {
		-moz-transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
		-webkit-transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
		-ms-transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
		transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
		color: #666;
		text-decoration: none;
		border-bottom: solid 1px #ddd;
	}

		a strong {
			-moz-transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
			-webkit-transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
			-ms-transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
			transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
		}

		a:hover {
			color: #ed786a;
			border-bottom-color: rgba(255, 255, 255, 0);
		}

			a:hover strong {
				color: #ed786a;
			}

	strong, b {
		font-weight: 600;
		color: #666;
	}

	em, i {
		font-style: italic;
	}

	sub {
		position: relative;
		top: 0.5em;
		font-size: 0.8em;
	}

	sup {
		position: relative;
		top: -0.5em;
		font-size: 0.8em;
	}

	hr {
		border: 0;
		border-top: solid 1px #ddd;
	}

	blockquote {
		border-left: solid 0.5em #ddd;
		padding: 1em 0 1em 2em;
		font-style: italic;
	}

	p {
		text-align: justify;
		margin-bottom: 2em;
	}

	ul, ol, dl, table, blockquote {
		margin-bottom: 2em;
	}

	br.clear {
		clear: both;
	}

/* Container */

	.container {
		margin: 0 auto;
		max-width: 100%;
		width: 70em;
	}

		@media screen and (max-width: 1680px) {

			.container {
				width: 68em;
			}

		}

		@media screen and (max-width: 1280px) {

			.container {
				width: calc(100% - 80px);
			}

		}

		@media screen and (max-width: 980px) {

			.container {
				width: calc(100% - 100px);
			}

		}

		@media screen and (max-width: 736px) {

			.container {
				width: calc(100% - 40px);
			}

		}

/* Row */

	.row {
		display: flex;
		flex-wrap: wrap;
		box-sizing: border-box;
		align-items: stretch;
	}

		.row > * {
			box-sizing: border-box;
		}

		.row.gtr-uniform > * > :last-child {
			margin-bottom: 0;
		}

		.row.aln-left {
			justify-content: flex-start;
		}

		.row.aln-center {
			justify-content: center;
		}

		.row.aln-right {
			justify-content: flex-end;
		}

		.row.aln-top {
			align-items: flex-start;
		}

		.row.aln-middle {
			align-items: center;
		}

		.row.aln-bottom {
			align-items: flex-end;
		}

		.row > .imp {
			order: -1;
		}

		.row > .col-1 {
			width: 8.33333%;
		}

		.row > .off-1 {
			margin-left: 8.33333%;
		}

		.row > .col-2 {
			width: 16.66667%;
		}

		.row > .off-2 {
			margin-left: 16.66667%;
		}

		.row > .col-3 {
			width: 25%;
		}

		.row > .off-3 {
			margin-left: 25%;
		}

		.row > .col-4 {
			width: 33.33333%;
		}

		.row > .off-4 {
			margin-left: 33.33333%;
		}

		.row > .col-5 {
			width: 41.66667%;
		}

		.row > .off-5 {
			margin-left: 41.66667%;
		}

		.row > .col-6 {
			width: 50%;
		}

		.row > .off-6 {
			margin-left: 50%;
		}

		.row > .col-7 {
			width: 58.33333%;
		}

		.row > .off-7 {
			margin-left: 58.33333%;
		}

		.row > .col-8 {
			width: 66.66667%;
		}

		.row > .off-8 {
			margin-left: 66.66667%;
		}

		.row > .col-9 {
			width: 75%;
		}

		.row > .off-9 {
			margin-left: 75%;
		}

		.row > .col-10 {
			width: 83.33333%;
		}

		.row > .off-10 {
			margin-left: 83.33333%;
		}

		.row > .col-11 {
			width: 91.66667%;
		}

		.row > .off-11 {
			margin-left: 91.66667%;
		}

		.row > .col-12 {
			width: 100%;
		}

		.row > .off-12 {
			margin-left: 100%;
		}

		.row.gtr-0 {
			margin-top: 0px;
			margin-left: 0px;
		}

			.row.gtr-0 > * {
				padding: 0px 0 0 0px;
			}

			.row.gtr-0.gtr-uniform {
				margin-top: 0px;
			}

				.row.gtr-0.gtr-uniform > * {
					padding-top: 0px;
				}

		.row.gtr-25 {
			margin-top: -12.5px;
			margin-left: -12.5px;
		}

			.row.gtr-25 > * {
				padding: 12.5px 0 0 12.5px;
			}

			.row.gtr-25.gtr-uniform {
				margin-top: -12.5px;
			}

				.row.gtr-25.gtr-uniform > * {
					padding-top: 12.5px;
				}

		.row.gtr-50 {
			margin-top: -25px;
			margin-left: -25px;
		}

			.row.gtr-50 > * {
				padding: 25px 0 0 25px;
			}

			.row.gtr-50.gtr-uniform {
				margin-top: -25px;
			}

				.row.gtr-50.gtr-uniform > * {
					padding-top: 25px;
				}

		.row {
			margin-top: -50px;
			margin-left: -50px;
		}

			.row > * {
				padding: 50px 0 0 50px;
			}

			.row.gtr-uniform {
				margin-top: -50px;
			}

				.row.gtr-uniform > * {
					padding-top: 50px;
				}

		.row.gtr-150 {
			margin-top: -75px;
			margin-left: -75px;
		}

			.row.gtr-150 > * {
				padding: 75px 0 0 75px;
			}

			.row.gtr-150.gtr-uniform {
				margin-top: -75px;
			}

				.row.gtr-150.gtr-uniform > * {
					padding-top: 75px;
				}

		.row.gtr-200 {
			margin-top: -100px;
			margin-left: -100px;
		}

			.row.gtr-200 > * {
				padding: 100px 0 0 100px;
			}

			.row.gtr-200.gtr-uniform {
				margin-top: -100px;
			}

				.row.gtr-200.gtr-uniform > * {
					padding-top: 100px;
				}

		@media screen and (max-width: 1680px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-xlarge {
					order: -1;
				}

				.row > .col-1-xlarge {
					width: 8.33333%;
				}

				.row > .off-1-xlarge {
					margin-left: 8.33333%;
				}

				.row > .col-2-xlarge {
					width: 16.66667%;
				}

				.row > .off-2-xlarge {
					margin-left: 16.66667%;
				}

				.row > .col-3-xlarge {
					width: 25%;
				}

				.row > .off-3-xlarge {
					margin-left: 25%;
				}

				.row > .col-4-xlarge {
					width: 33.33333%;
				}

				.row > .off-4-xlarge {
					margin-left: 33.33333%;
				}

				.row > .col-5-xlarge {
					width: 41.66667%;
				}

				.row > .off-5-xlarge {
					margin-left: 41.66667%;
				}

				.row > .col-6-xlarge {
					width: 50%;
				}

				.row > .off-6-xlarge {
					margin-left: 50%;
				}

				.row > .col-7-xlarge {
					width: 58.33333%;
				}

				.row > .off-7-xlarge {
					margin-left: 58.33333%;
				}

				.row > .col-8-xlarge {
					width: 66.66667%;
				}

				.row > .off-8-xlarge {
					margin-left: 66.66667%;
				}

				.row > .col-9-xlarge {
					width: 75%;
				}

				.row > .off-9-xlarge {
					margin-left: 75%;
				}

				.row > .col-10-xlarge {
					width: 83.33333%;
				}

				.row > .off-10-xlarge {
					margin-left: 83.33333%;
				}

				.row > .col-11-xlarge {
					width: 91.66667%;
				}

				.row > .off-11-xlarge {
					margin-left: 91.66667%;
				}

				.row > .col-12-xlarge {
					width: 100%;
				}

				.row > .off-12-xlarge {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -12.5px;
					margin-left: -12.5px;
				}

					.row.gtr-25 > * {
						padding: 12.5px 0 0 12.5px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -12.5px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 12.5px;
						}

				.row.gtr-50 {
					margin-top: -25px;
					margin-left: -25px;
				}

					.row.gtr-50 > * {
						padding: 25px 0 0 25px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -25px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 25px;
						}

				.row {
					margin-top: -50px;
					margin-left: -50px;
				}

					.row > * {
						padding: 50px 0 0 50px;
					}

					.row.gtr-uniform {
						margin-top: -50px;
					}

						.row.gtr-uniform > * {
							padding-top: 50px;
						}

				.row.gtr-150 {
					margin-top: -75px;
					margin-left: -75px;
				}

					.row.gtr-150 > * {
						padding: 75px 0 0 75px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -75px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 75px;
						}

				.row.gtr-200 {
					margin-top: -100px;
					margin-left: -100px;
				}

					.row.gtr-200 > * {
						padding: 100px 0 0 100px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -100px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 100px;
						}

		}

		@media screen and (max-width: 1280px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-large {
					order: -1;
				}

				.row > .col-1-large {
					width: 8.33333%;
				}

				.row > .off-1-large {
					margin-left: 8.33333%;
				}

				.row > .col-2-large {
					width: 16.66667%;
				}

				.row > .off-2-large {
					margin-left: 16.66667%;
				}

				.row > .col-3-large {
					width: 25%;
				}

				.row > .off-3-large {
					margin-left: 25%;
				}

				.row > .col-4-large {
					width: 33.33333%;
				}

				.row > .off-4-large {
					margin-left: 33.33333%;
				}

				.row > .col-5-large {
					width: 41.66667%;
				}

				.row > .off-5-large {
					margin-left: 41.66667%;
				}

				.row > .col-6-large {
					width: 50%;
				}

				.row > .off-6-large {
					margin-left: 50%;
				}

				.row > .col-7-large {
					width: 58.33333%;
				}

				.row > .off-7-large {
					margin-left: 58.33333%;
				}

				.row > .col-8-large {
					width: 66.66667%;
				}

				.row > .off-8-large {
					margin-left: 66.66667%;
				}

				.row > .col-9-large {
					width: 75%;
				}

				.row > .off-9-large {
					margin-left: 75%;
				}

				.row > .col-10-large {
					width: 83.33333%;
				}

				.row > .off-10-large {
					margin-left: 83.33333%;
				}

				.row > .col-11-large {
					width: 91.66667%;
				}

				.row > .off-11-large {
					margin-left: 91.66667%;
				}

				.row > .col-12-large {
					width: 100%;
				}

				.row > .off-12-large {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -10px;
					margin-left: -10px;
				}

					.row.gtr-25 > * {
						padding: 10px 0 0 10px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -10px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 10px;
						}

				.row.gtr-50 {
					margin-top: -20px;
					margin-left: -20px;
				}

					.row.gtr-50 > * {
						padding: 20px 0 0 20px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -20px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 20px;
						}

				.row {
					margin-top: -40px;
					margin-left: -40px;
				}

					.row > * {
						padding: 40px 0 0 40px;
					}

					.row.gtr-uniform {
						margin-top: -40px;
					}

						.row.gtr-uniform > * {
							padding-top: 40px;
						}

				.row.gtr-150 {
					margin-top: -60px;
					margin-left: -60px;
				}

					.row.gtr-150 > * {
						padding: 60px 0 0 60px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -60px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 60px;
						}

				.row.gtr-200 {
					margin-top: -80px;
					margin-left: -80px;
				}

					.row.gtr-200 > * {
						padding: 80px 0 0 80px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -80px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 80px;
						}

		}

		@media screen and (max-width: 980px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-medium {
					order: -1;
				}

				.row > .col-1-medium {
					width: 8.33333%;
				}

				.row > .off-1-medium {
					margin-left: 8.33333%;
				}

				.row > .col-2-medium {
					width: 16.66667%;
				}

				.row > .off-2-medium {
					margin-left: 16.66667%;
				}

				.row > .col-3-medium {
					width: 25%;
				}

				.row > .off-3-medium {
					margin-left: 25%;
				}

				.row > .col-4-medium {
					width: 33.33333%;
				}

				.row > .off-4-medium {
					margin-left: 33.33333%;
				}

				.row > .col-5-medium {
					width: 41.66667%;
				}

				.row > .off-5-medium {
					margin-left: 41.66667%;
				}

				.row > .col-6-medium {
					width: 50%;
				}

				.row > .off-6-medium {
					margin-left: 50%;
				}

				.row > .col-7-medium {
					width: 58.33333%;
				}

				.row > .off-7-medium {
					margin-left: 58.33333%;
				}

				.row > .col-8-medium {
					width: 66.66667%;
				}

				.row > .off-8-medium {
					margin-left: 66.66667%;
				}

				.row > .col-9-medium {
					width: 75%;
				}

				.row > .off-9-medium {
					margin-left: 75%;
				}

				.row > .col-10-medium {
					width: 83.33333%;
				}

				.row > .off-10-medium {
					margin-left: 83.33333%;
				}

				.row > .col-11-medium {
					width: 91.66667%;
				}

				.row > .off-11-medium {
					margin-left: 91.66667%;
				}

				.row > .col-12-medium {
					width: 100%;
				}

				.row > .off-12-medium {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -12.5px;
					margin-left: -12.5px;
				}

					.row.gtr-25 > * {
						padding: 12.5px 0 0 12.5px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -12.5px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 12.5px;
						}

				.row.gtr-50 {
					margin-top: -25px;
					margin-left: -25px;
				}

					.row.gtr-50 > * {
						padding: 25px 0 0 25px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -25px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 25px;
						}

				.row {
					margin-top: -50px;
					margin-left: -50px;
				}

					.row > * {
						padding: 50px 0 0 50px;
					}

					.row.gtr-uniform {
						margin-top: -50px;
					}

						.row.gtr-uniform > * {
							padding-top: 50px;
						}

				.row.gtr-150 {
					margin-top: -75px;
					margin-left: -75px;
				}

					.row.gtr-150 > * {
						padding: 75px 0 0 75px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -75px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 75px;
						}

				.row.gtr-200 {
					margin-top: -100px;
					margin-left: -100px;
				}

					.row.gtr-200 > * {
						padding: 100px 0 0 100px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -100px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 100px;
						}

		}

		@media screen and (max-width: 736px) {

			.row {
				display: flex;
				flex-wrap: wrap;
				box-sizing: border-box;
				align-items: stretch;
			}

				.row > * {
					box-sizing: border-box;
				}

				.row.gtr-uniform > * > :last-child {
					margin-bottom: 0;
				}

				.row.aln-left {
					justify-content: flex-start;
				}

				.row.aln-center {
					justify-content: center;
				}

				.row.aln-right {
					justify-content: flex-end;
				}

				.row.aln-top {
					align-items: flex-start;
				}

				.row.aln-middle {
					align-items: center;
				}

				.row.aln-bottom {
					align-items: flex-end;
				}

				.row > .imp-small {
					order: -1;
				}

				.row > .col-1-small {
					width: 8.33333%;
				}

				.row > .off-1-small {
					margin-left: 8.33333%;
				}

				.row > .col-2-small {
					width: 16.66667%;
				}

				.row > .off-2-small {
					margin-left: 16.66667%;
				}

				.row > .col-3-small {
					width: 25%;
				}

				.row > .off-3-small {
					margin-left: 25%;
				}

				.row > .col-4-small {
					width: 33.33333%;
				}

				.row > .off-4-small {
					margin-left: 33.33333%;
				}

				.row > .col-5-small {
					width: 41.66667%;
				}

				.row > .off-5-small {
					margin-left: 41.66667%;
				}

				.row > .col-6-small {
					width: 50%;
				}

				.row > .off-6-small {
					margin-left: 50%;
				}

				.row > .col-7-small {
					width: 58.33333%;
				}

				.row > .off-7-small {
					margin-left: 58.33333%;
				}

				.row > .col-8-small {
					width: 66.66667%;
				}

				.row > .off-8-small {
					margin-left: 66.66667%;
				}

				.row > .col-9-small {
					width: 75%;
				}

				.row > .off-9-small {
					margin-left: 75%;
				}

				.row > .col-10-small {
					width: 83.33333%;
				}

				.row > .off-10-small {
					margin-left: 83.33333%;
				}

				.row > .col-11-small {
					width: 91.66667%;
				}

				.row > .off-11-small {
					margin-left: 91.66667%;
				}

				.row > .col-12-small {
					width: 100%;
				}

				.row > .off-12-small {
					margin-left: 100%;
				}

				.row.gtr-0 {
					margin-top: 0px;
					margin-left: 0px;
				}

					.row.gtr-0 > * {
						padding: 0px 0 0 0px;
					}

					.row.gtr-0.gtr-uniform {
						margin-top: 0px;
					}

						.row.gtr-0.gtr-uniform > * {
							padding-top: 0px;
						}

				.row.gtr-25 {
					margin-top: -7.5px;
					margin-left: -7.5px;
				}

					.row.gtr-25 > * {
						padding: 7.5px 0 0 7.5px;
					}

					.row.gtr-25.gtr-uniform {
						margin-top: -7.5px;
					}

						.row.gtr-25.gtr-uniform > * {
							padding-top: 7.5px;
						}

				.row.gtr-50 {
					margin-top: -15px;
					margin-left: -15px;
				}

					.row.gtr-50 > * {
						padding: 15px 0 0 15px;
					}

					.row.gtr-50.gtr-uniform {
						margin-top: -15px;
					}

						.row.gtr-50.gtr-uniform > * {
							padding-top: 15px;
						}

				.row {
					margin-top: -30px;
					margin-left: -30px;
				}

					.row > * {
						padding: 30px 0 0 30px;
					}

					.row.gtr-uniform {
						margin-top: -30px;
					}

						.row.gtr-uniform > * {
							padding-top: 30px;
						}

				.row.gtr-150 {
					margin-top: -45px;
					margin-left: -45px;
				}

					.row.gtr-150 > * {
						padding: 45px 0 0 45px;
					}

					.row.gtr-150.gtr-uniform {
						margin-top: -45px;
					}

						.row.gtr-150.gtr-uniform > * {
							padding-top: 45px;
						}

				.row.gtr-200 {
					margin-top: -60px;
					margin-left: -60px;
				}

					.row.gtr-200 > * {
						padding: 60px 0 0 60px;
					}

					.row.gtr-200.gtr-uniform {
						margin-top: -60px;
					}

						.row.gtr-200.gtr-uniform > * {
							padding-top: 60px;
						}

		}

/* Sections/Article */

	section, article {
		margin-bottom: 3em;
	}

	section > :last-child,
	article > :last-child,
	section:last-child,
	article:last-child {
		margin-bottom: 0;
	}

/* Image */

	.image {
		-moz-transition: opacity 0.25s ease-in-out;
		-webkit-transition: opacity 0.25s ease-in-out;
		-ms-transition: opacity 0.25s ease-in-out;
		transition: opacity 0.25s ease-in-out;
		display: inline-block;
		border: solid 6px #ebebeb !important;
	}

		.image:hover {
			opacity: 0.9;
		}

		.image img {
			display: block;
			width: 100%;
		}

		.image.fit {
			display: block;
			width: 100%;
		}

		.image.featured {
			display: block;
			width: 100%;
			margin: 0 0 3.5em 0;
		}

		.image.left {
			float: left;
			margin: 0 1.5em 1.5em 0;
			position: relative;
			top: 0.5em;
		}

		.image.centered {
			display: block;
			margin: 0 0 2em 0;
		}

			.image.centered img {
				margin: 0 auto;
				width: auto;
			}

/* List */

	ul {
		list-style: disc;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
			margin: 0.75em 0 0.75em 0;
		}

			ul li:first-child {
				margin-top: 0;
			}

	ol {
		list-style: decimal;
		padding-left: 1em;
	}

		ol li {
			padding-left: 0.5em;
			margin: 0.75em 0 0.75em 0;
		}

			ol li:first-child {
				margin-top: 0;
			}

/* Links */

	ul.links {
		list-style: none;
		padding-left: 0;
	}

		ul.links li {
			display: inline;
			border-left: solid 1px #d0d0d0;
			padding-left: 1em;
			margin: 0 0 0 1em;
		}

			ul.links li:first-child {
				margin-left: 0;
				padding-left: 0;
				border-left: 0;
			}

/* Actions */

	ul.actions {
		margin-top: 2.5em;
		clear: both;
		list-style: none;
		padding-left: 0;
	}

		ul.actions li {
			padding-left: 0;
			display: inline-block;
			margin: 0 0 0 1em;
		}

			ul.actions li:first-child {
				margin-left: 0;
			}

/* Divided */

	ul.divided {
		list-style: none;
		padding-left: 0;
	}

		ul.divided li {
			border-top: solid 2px #e5e5e5;
			padding-left: 0;
			margin: 2.5em 0 0 0;
			padding: 2.5em 0 0 0;
		}

			ul.divided li:first-child {
				border-top: 0;
				margin-top: 0;
				padding-top: 0;
			}

/* Icons */

	ul.icons {
		list-style: none;
		padding-left: 0;
	}

		ul.icons > li {
			position: relative;
			padding: 2em 0 0 3em;
			margin: 0;
		}

			ul.icons > li:before {
				position: absolute;
				left: 0;
				top: 2.6em;
				display: block;
				font-size: 0.8em;
				background: #878787;
				color: #e4e4e4;
				width: 2em;
				height: 2em;
				border-radius: 2em;
				line-height: 2em;
				text-align: center;
				box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
			}

			ul.icons > li:first-child {
				padding-top: 0;
			}

				ul.icons > li:first-child:before {
					top: 0;
				}

/* Form */

	form label {
		font-weight: 600;
		text-transform: uppercase;
		color: #888;
		display: block;
		margin: 0 0 1em 0;
	}

	form input[type="text"],
	form input[type="email"],
	form input[type="password"],
	form select,
	form textarea {
		-moz-transition: background-color 0.25s ease-in-out;
		-webkit-transition: background-color 0.25s ease-in-out;
		-ms-transition: background-color 0.25s ease-in-out;
		transition: background-color 0.25s ease-in-out;
		-webkit-appearance: none;
		display: block;
		border: 0;
		background: #e8e8e8;
		width: 100%;
		box-shadow: inset 2px 2px 0px 0px rgba(0, 0, 0, 0.1);
		border-radius: 4px;
		line-height: 1.25em;
		padding: 0.75em 1em 0.75em 1em;
	}

		form input[type="text"]:focus,
		form input[type="email"]:focus,
		form input[type="password"]:focus,
		form select:focus,
		form textarea:focus {
			background: #f0f0f0;
		}

	form textarea {
		min-height: 11em;
	}

	form ::-webkit-input-placeholder {
		color: #555 !important;
		line-height: 1.35em;
	}

	form :-moz-placeholder {
		color: #555 !important;
	}

	form ::-moz-placeholder {
		color: #555 !important;
	}

	form :-ms-input-placeholder {
		color: #555 !important;
	}

	form ::-moz-focus-inner {
		border: 0;
	}

/* Table */

	table {
		width: 100%;
	}

		table tbody tr {
			border-top: solid 1px #E5E5E5;
		}

			table tbody tr:first-child {
				border-top: 0;
			}

		table td {
			padding: 0.75em 1em 0.75em 1em;
		}

		table th {
			text-align: left;
			font-weight: bold;
			padding: 0.75em 1em 0.75em 1em;
		}

		table thead {
			background: #878787;
			color: #fff;
			font-weight: 400;
			text-transform: uppercase;
			border: 0;
			box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
			font-size: 0.85em;
			letter-spacing: 2px;
		}

		table tfoot {
			background: #F0F0F0;
			border-top: solid 2px #E5E5E5;
		}

/* Button */

	input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		-moz-transition: all 0.25s ease-in-out;
		-webkit-transition: all 0.25s ease-in-out;
		-ms-transition: all 0.25s ease-in-out;
		transition: all 0.25s ease-in-out;
		-webkit-appearance: none;
		position: relative;
		display: inline-block;
		background: #ed786a;
		color: #fff !important;
		text-transform: uppercase;
		border-radius: 4px;
		border: 0;
		outline: 0;
		font-size: 1em;
		box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
		font-weight: 600;
		text-align: center;
		font-size: 0.85em;
		letter-spacing: 2px;
		padding: 0.85em 2.75em 0.85em 2.75em;
	}

		input[type="button"].icon:before,
		input[type="submit"].icon:before,
		input[type="reset"].icon:before,
		button.icon:before,
		.button.icon:before {
			position: relative;
			padding-right: 0.75em;
			opacity: 0.5;
			top: 0.05em;
		}

		input[type="button"]:hover,
		input[type="submit"]:hover,
		input[type="reset"]:hover,
		button:hover,
		.button:hover {
			background: #fd887a;
		}

		input[type="button"]:active,
		input[type="submit"]:active,
		input[type="reset"]:active,
		button:active,
		.button:active {
			background: #ed786a;
		}

		input[type="button"].alt,
		input[type="submit"].alt,
		input[type="reset"].alt,
		button.alt,
		.button.alt {
			background: #878787;
		}

			input[type="button"].alt:hover,
			input[type="submit"].alt:hover,
			input[type="reset"].alt:hover,
			button.alt:hover,
			.button.alt:hover {
				background: #979797;
			}

			input[type="button"].alt:active,
			input[type="submit"].alt:active,
			input[type="reset"].alt:active,
			button.alt:active,
			.button.alt:active {
				background: #878787;
			}

/* Box */

	.no-sidebar .box.post > header {
		text-align: center;
	}

	.box.excerpt .date {
		background: #878787;
		color: #fff;
		font-weight: 400;
		text-transform: uppercase;
		border-radius: 4px;
		border: 0;
		box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
		display: inline-block;
		font-size: 0.85em;
		letter-spacing: 2px;
		padding: 0.25em 1em 0.25em 1em;
		margin: 0 0 2.5em 0;
	}

/* Icons */

	.icon {
		text-decoration: none;
		position: relative;
		text-decoration: none;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			display: inline-block;
			font-style: normal;
			font-variant: normal;
			text-rendering: auto;
			line-height: 1;
			text-transform: none !important;
			font-family: 'Font Awesome 5 Free';
			font-weight: 400;
		}

		.icon:before {
			line-height: inherit;
		}

		.icon > .label {
			display: none;
		}

		.icon.solid:before {
			font-weight: 900;
		}

		.icon.brands:before {
			font-family: 'Font Awesome 5 Brands';
		}

/* Page Wrapper */

	#page-wrapper > section {
		margin-bottom: 0;
	}

/* Header */

	#header {
		position: relative;
		position: relative;
		background: #fff;
		text-align: center;
	}

		#header > .container {
			padding: 14em 0 7em 0;
			border-bottom: solid 2px #e5e5e5;
			box-shadow: inset 0px -8px 0px 0px #fff, inset 0px -10px 0px 0px #e5e5e5;
		}

		#header h1 {
			font-family: 'Arvo';
			font-weight: 700;
			color: #ed786a;
			text-shadow: 0.05em 0.075em 0 rgba(0, 0, 0, 0.1);
			font-size: 3em;
			letter-spacing: 13px;
			line-height: 1.25em;
		}

			#header h1 a {
				border: 0;
			}

		#header p {
			text-transform: uppercase;
			font-weight: 400;
			color: #888;
			margin: 2.5em 0 0 0;
			font-size: 0.85em;
			letter-spacing: 3px;
			text-align: center;
		}

/* Nav */

	#nav {
		position: absolute;
		top: 3em;
		left: 0;
		width: 100%;
		cursor: default;
	}

		#nav > ul > li {
			display: inline-block;
			padding-right: 2em;
		}

			#nav > ul > li:last-child {
				padding-right: 0;
			}

			#nav > ul > li > a {
				border: 0;
				text-decoration: none;
				text-transform: uppercase;
				font-weight: 400;
				color: #777;
				outline: 0;
				display: block;
			}

				#nav > ul > li > a:before {
					display: inline-block;
					background: #878787;
					color: #e4e4e4;
					width: 2.25em;
					font-size: 0.8em;
					height: 2.25em;
					border-radius: 2.25em;
					line-height: 2.1em;
					text-align: center;
					box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
					margin-right: 0.75em;
					-moz-transition: color 0.25s ease-in-out, background 0.25s ease-in-out;
					-webkit-transition: color 0.25s ease-in-out, background 0.25s ease-in-out;
					-o-transition: color 0.25s ease-in-out, background 0.25s ease-in-out;
					-ms-transition: color 0.25s ease-in-out, background 0.25s ease-in-out;
					transition: color 0.25s ease-in-out, background 0.25s ease-in-out;
				}

				#nav > ul > li > a > span {
					-moz-transition: color 0.25s ease-in-out;
					-webkit-transition: color 0.25s ease-in-out;
					-o-transition: color 0.25s ease-in-out;
					-ms-transition: color 0.25s ease-in-out;
					transition: color 0.25s ease-in-out;
					font-size: 0.85em;
					letter-spacing: 3px;
				}

			#nav > ul > li > ul {
				display: none;
			}

			#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				background: #ED786A;
				color: #fff;
			}

			#nav > ul > li.active > a > span,
			#nav > ul > li:hover > a > span {
				color: #ED786A;
			}

	.dropotron {
		text-align: left;
		border: solid 1px #e5e5e5;
		border-radius: 4px;
		background: #fff;
		background: rgba(255, 255, 255, 0.965);
		box-shadow: 0px 2px 2px 0px rgba(0, 0, 0, 0.1);
		padding: 0.75em 0 0.5em 0;
		min-width: 12em;
		margin-top: calc(-0.5em + 1px);
		margin-left: -2px;
		list-style: none;
	}

		.dropotron.level-0 {
			margin-top: 1.5em;
			margin-left: -1em;
		}

			.dropotron.level-0:after {
				content: '';
				display: block;
				position: absolute;
				left: 1.25em;
				top: calc(-0.75em + 1px);
				border-left: solid 0.75em rgba(255, 255, 255, 0);
				border-right: solid 0.75em rgba(255, 255, 255, 0);
				border-bottom: solid 0.75em #fff;
			}

			.dropotron.level-0:before {
				content: '';
				display: block;
				position: absolute;
				left: 1.25em;
				top: -0.75em;
				border-left: solid 0.75em rgba(255, 255, 255, 0);
				border-right: solid 0.75em rgba(255, 255, 255, 0);
				border-bottom: solid 0.75em #ccc;
			}

		.dropotron span, .dropotron a {
			display: block;
			padding: 0.3em 1em 0.3em 1em;
			border: 0;
			border-top: solid 1px #f0f0f0;
			outline: 0;
		}

		.dropotron li {
			padding-left: 0;
			margin: 0;
		}

			.dropotron li:first-child > span, .dropotron li:first-child > a {
				border-top: 0;
				padding-top: 0;
			}

			.dropotron li:hover > span, .dropotron li:hover > a {
				-moz-transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				-webkit-transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				-ms-transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				color: #ed786a;
			}

/* Features */

	#features {
		position: relative;
		overflow: hidden;
		background: #fff;
		text-align: center;
		padding: 6em 0;
	}

		#features p {
			text-align: center;
		}

		#features ul.actions {
			margin-top: 1.25em;
		}

/* Banner */

	#banner {
		position: relative;
		overflow: hidden;
		background: #fff;
		color: #fff;
		text-align: center;
		border-top: solid 2px #e5e5e5;
		border-bottom: solid 2px #e5e5e5;
		box-shadow: inset 0px -8px 0px 0px #fff, inset 0px 8px 0px 0px #fff;
		position: relative;
		text-transform: uppercase;
		background: url("../../images/banner.jpg");
		background-size: cover;
		padding: 10em 0;
	}

		#banner p {
			font-weight: 400;
			font-size: 2em;
			line-height: 1.5em;
			letter-spacing: 4px;
			text-align: center;
			margin: 0;
		}

		#banner strong {
			color: inherit;
		}

		#banner > .container {
			position: relative;
		}

			#banner > .container:before, #banner > .container:after {
				content: '';
				display: block;
				position: absolute;
				top: 50%;
				width: 35px;
				height: 141px;
				margin-top: -70px;
				background: url("images/bracket.svg");
				opacity: 0.15;
			}

			#banner > .container:before {
				left: 0;
			}

			#banner > .container:after {
				-moz-transform: scaleX(-1);
				-webkit-transform: scaleX(-1);
				-ms-transform: scaleX(-1);
				transform: scaleX(-1);
				right: 0;
			}

/* Main */

	#main {
		position: relative;
		overflow: hidden;
		background: #fff;
		padding: 6em 0;
	}

/* Content */

	#content > section,
	#content > article {
		border-top: solid 2px #e5e5e5;
		box-shadow: inset 0px 8px 0px 0px #fff, inset 0px 10px 0px 0px #e5e5e5;
		margin: 5em 0 0 0;
		padding: 5em 0 0 0;
	}

		#content > section:first-child,
		#content > article:first-child {
			border-top: 0;
			box-shadow: none;
			margin: 0;
			padding: 0;
		}

/* Sidebar */

	#sidebar > section,
	#sidebar > article {
		border-top: solid 2px #e5e5e5;
		box-shadow: inset 0px 8px 0px 0px #fff, inset 0px 10px 0px 0px #e5e5e5;
		margin: 5em 0 0 0;
		padding: 5em 0 0 0;
	}

		#sidebar > section:first-child,
		#sidebar > article:first-child {
			border-top: 0;
			box-shadow: none;
			margin: 0;
			padding: 0;
		}

/* Footer */

	#footer {
		position: relative;
		overflow: hidden;
		border-top: solid 2px #e5e5e5;
		background: #f0f0f0;
		padding: 6em 0 8em 0;
	}

		#footer form input[type="text"],
		#footer form input[type="email"],
		#footer form input[type="password"],
		#footer form select,
		#footer form textarea {
			background: #f7f7f7;
		}

			#footer form input[type="text"]:focus,
			#footer form input[type="email"]:focus,
			#footer form input[type="password"]:focus,
			#footer form select:focus,
			#footer form textarea:focus {
				background: #fff;
			}

		#footer h2 {
			text-align: center;
		}

/* Copyright */

	#copyright {
		border-top: solid 2px #e5e5e5;
		text-align: center;
		margin-top: 6em;
		padding-top: 4em;
	}

/* XLarge */

	@media screen and (max-width: 1680px) {

		/* Basic */

			body, input, textarea, select {
				font-size: 13pt;
			}

	}

/* Large */

	@media screen and (max-width: 1280px) {

		/* Basic */

			body, input, textarea, select {
				font-size: 12pt;
			}

			h2 br, h3 br, h4 br, h5 br, h6 br {
				display: none;
			}

		/* Image */

			.image.left {
				max-width: 50%;
			}

			.image.right {
				max-width: 50%;
			}

		/* Header */

			#header > .container {
				padding: 12em 0 5em 0;
			}

			#header h1 {
				font-size: 2.5em;
			}

		/* Nav */

			#nav > ul > li {
				padding-right: 1.25em;
			}

		/* Features */

			#features {
				padding: 4em 0;
			}

		/* Banner */

			#banner {
				padding: 8em 0;
			}

				#banner > .container {
					padding: 0 4em;
				}

					#banner > .container br {
						display: none;
					}

		/* Main */

			#main {
				padding: 4em 0;
			}

		/* Footer */

			#footer {
				padding: 4em 0;
			}

		/* Copyright */

			#copyright {
				margin-top: 2em;
				padding-top: 2em;
			}

	}

/* Medium */

	#navPanel, #titleBar {
		display: none;
	}

	@media screen and (max-width: 980px) {

		/* Basic */

			html, body {
				overflow-x: hidden;
			}

		/* Header */

			#header > .container {
				padding: 10em 0 7em 0;
			}

		/* Nav */

			#nav {
				display: none;
			}

		/* Nav */

			#page-wrapper {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				padding-bottom: 1px;
			}

			#titleBar {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 44px;
				left: 0;
				position: fixed;
				top: 0;
				width: 100%;
				z-index: 10001;
			}

				#titleBar .toggle {
					text-decoration: none;
					position: absolute;
					left: 0;
					top: 0;
					width: 80px;
					height: 60px;
					border: 0;
				}

					#titleBar .toggle:before {
						-moz-osx-font-smoothing: grayscale;
						-webkit-font-smoothing: antialiased;
						display: inline-block;
						font-style: normal;
						font-variant: normal;
						text-rendering: auto;
						line-height: 1;
						text-transform: none !important;
						font-family: 'Font Awesome 5 Free';
						font-weight: 900;
					}

					#titleBar .toggle:before {
						display: inline-block;
						text-decoration: none;
						content: '\\f0c9';
						display: block;
						width: 60px;
						height: 40px;
						background: rgba(232, 232, 232, 0.9);
						border-radius: 4px;
						position: absolute;
						left: 5px;
						top: 5px;
						box-shadow: 0.125em 0.125em 0 0 rgba(0, 0, 0, 0.15);
						text-align: center;
						line-height: 40px;
						font-size: 18px;
						color: #aaa;
					}

					#titleBar .toggle:active:before {
						opacity: 0.5;
					}

			#navPanel {
				-moz-backface-visibility: hidden;
				-webkit-backface-visibility: hidden;
				-ms-backface-visibility: hidden;
				backface-visibility: hidden;
				-moz-transform: translateX(-275px);
				-webkit-transform: translateX(-275px);
				-ms-transform: translateX(-275px);
				transform: translateX(-275px);
				-moz-transition: -moz-transform 0.5s ease;
				-webkit-transition: -webkit-transform 0.5s ease;
				-ms-transition: -ms-transform 0.5s ease;
				transition: transform 0.5s ease;
				display: block;
				height: 100%;
				left: 0;
				overflow-y: auto;
				position: fixed;
				top: 0;
				width: 275px;
				z-index: 10002;
				background: #444;
				border-right: solid 2px #3c3c3c;
				font-weight: 400;
				text-transform: uppercase;
				color: #888;
				letter-spacing: 2px;
				font-size: 0.85em;
			}

				#navPanel .link {
					display: block;
					color: #ddd;
					text-decoration: none;
					height: 44px;
					line-height: 44px;
					border: 0;
					border-top: solid 1px #3c3c3c;
					padding: 0 1em 0 1em;
				}

					#navPanel .link:first-child {
						border-top: 0;
					}

					#navPanel .link.depth-0 {
						font-weight: 600;
						color: #fff;
					}

				#navPanel .indent-1 {
					display: inline-block;
					width: 1em;
				}

				#navPanel .indent-2 {
					display: inline-block;
					width: 2em;
				}

				#navPanel .indent-3 {
					display: inline-block;
					width: 3em;
				}

				#navPanel .indent-4 {
					display: inline-block;
					width: 4em;
				}

				#navPanel .indent-5 {
					display: inline-block;
					width: 5em;
				}

				#navPanel .depth-0 {
					color: #fff;
				}

			body.navPanel-visible #page-wrapper {
				-moz-transform: translateX(275px);
				-webkit-transform: translateX(275px);
				-ms-transform: translateX(275px);
				transform: translateX(275px);
			}

			body.navPanel-visible #titleBar {
				-moz-transform: translateX(275px);
				-webkit-transform: translateX(275px);
				-ms-transform: translateX(275px);
				transform: translateX(275px);
			}

			body.navPanel-visible #navPanel {
				-moz-transform: translateX(0);
				-webkit-transform: translateX(0);
				-ms-transform: translateX(0);
				transform: translateX(0);
			}

		/* Sidebar */

			#sidebar {
				padding-top: 6em;
			}

	}

/* Small */

	@media screen and (max-width: 736px) {

		/* Basic */

			body, input, textarea, select {
				font-size: 11pt;
			}

			h2, h3, h4, h5, h6 {
				font-size: 1.2em;
				letter-spacing: 2px;
				text-align: center;
				margin: 0 0 1em 0;
			}

				h2 br, h3 br, h4 br, h5 br, h6 br {
					display: none;
				}

		/* Image */

			.image.featured {
				margin: 0 0 1.5em 0;
			}

			.image.left {
				max-width: 35%;
			}

			.image.right {
				max-width: 35%;
			}

		/* Button */

			input[type="button"],
			input[type="submit"],
			input[type="reset"],
			button,
			.button {
				letter-spacing: 2px;
				display: block;
				padding: 1em 0 1em 0;
				width: 100%;
			}

		/* Actions */

			ul.actions li {
				display: block;
				margin: 1em 0 0 0;
			}

				ul.actions li:first-child {
					margin-top: 0;
				}

		/* Box */

			.box.excerpt header {
				text-align: center;
			}

		/* Header */

			#header > .container {
				padding: 6em 0 4em 0;
			}

			#header h1 {
				font-size: 2em;
				letter-spacing: 8px;
				line-height: 1.325em;
			}

			#header p {
				margin: 1.25em 0 0 0;
				letter-spacing: 2px;
			}

		/* Banner */

			#banner {
				padding: 5em 0;
			}

				#banner > .container {
					padding: 0;
				}

					#banner > .container:before, #banner > .container:after {
						display: none;
					}

				#banner p {
					font-size: 1.25em;
				}

		/* Features */

			#features {
				padding: 2em 0;
			}

				#features ul.actions {
					margin-top: 0;
				}

		/* Main */

			#main {
				padding: 2em 0;
			}

		/* Content */

			#content > section,
			#content > article {
				margin: 3em 0 0 0;
				padding: 3em 0 0 0;
			}

		/* Sidebar */

			#sidebar {
				padding-top: 3em;
			}

				#sidebar > section,
				#sidebar > article {
					margin: 3em 0 0 0;
					padding: 3em 0 0 0;
				}

		/* Footer */

			#footer {
				padding: 2em 0;
			}

				#footer ul.icons {
					margin-bottom: 0;
				}

		/* Copyright */

			#copyright .links {
				margin-bottom: 0;
			}

				#copyright .links li {
					display: block;
					padding-left: 0;
					margin-left: 0;
					border-left: 0;
				}

	}""", "lime":"""
    --light-yellow: #F6E96B;
    --light-green: #FF8C9E;
    --forest-green: #FF4E88;
}

/* Example usage */
body {
    background-color: var(--light-yellow);
    color: var(--forest-green);
}

.header {
    background-color: var(--light-green);
    color: var(--forest-green);
}

.button {
    background-color: var(--forest-green);
    color: #fff;
}

.button:hover {
    background-color: var(--light-green);
    color: var(--forest-green);
}
.dropotron li:hover > span, .dropotron li:hover > a {transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				color: #FF4E88;
			}

	#header h1 {
			color: #FF4E88;
		}
		.button:active {
			background: #FF4E88;
		}

		.button {
		background: #FF4E88;
		color: #fff 
	}
	a:hover {
			color: #FF4E88;
			border-bottom-color: rgba(255, 255, 255, 0);
		}

			a:hover strong {
				color: #FF4E88;
			}

	
	h1, h2, h3, h4, h5, h6 {
		color: #FF9EAA;
	}
	#banner
	{
		color:#FF4E88;
	}
	input[type="button"], input[type="submit"], input[type="reset"], button, .button {
    background: #FF9EAA;
    }""", 
	"valley":""":root {
    --light-yellow: #F6E96B;
    --light-green: #BEDC74;
    --forest-green: #254336;
}


/* Example usage */
body {
    background-color: var(--light-yellow);
    color: var(--forest-green);
}

.header {
    background-color: var(--light-green);
    color: var(--forest-green);
}

.button {
    background-color: var(--forest-green);
    color: #fff;
}

.button:hover {
    background-color: var(--light-green);
    color: var(--forest-green);
}
.dropotron li:hover > span, .dropotron li:hover > a {transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				color: #254336;
			}


	}
	#header h1 {
			color: #254336;
		}
		.button:active {
			background: #254336;
		}

		.button {
		background: #254336;
		color: #fff 
	}
	a:hover {
			color: #254336;
			border-bottom-color: rgba(255, 255, 255, 0);
		}

			a:hover strong {
				color: #254336;
			}

	
	h1, h2, h3, h4, h5, h6 {
		color: #A2CA71;
	}
	#banner
	{
		color:#254336;
	}
	input[type="button"], input[type="submit"], input[type="reset"], button, .button {
    background: #A2CA71;
    }
	table thead {
	background: #878787;
	color: #DAD3BE;
	font-weight: 400;
	text-transform: uppercase;
	border: 0;
	box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
	font-size: 0.85em;
	letter-spacing: 2px;
}
input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #254336;
		color: #DAD3BE !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #DAD3BE;
	}
	#header {
		background: #DAD3BE;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #DAD3BE, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #DAD3BE;
			}
			.dropotron {
				background: #DAD3BE;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #DAD3BE;
			}
			#features {
				background: #DAD3BE;
			}
			
	#banner {
		background: #DAD3BE;
		color: #DAD3BE;
	}
	
	#main {
		background: #DAD3BE;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #DAD3BE, inset 0px 10px 0px 0px #e5e5e5;
	}
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #DAD3BE, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #DAD3BE;
	}
	#navPanel .link.depth-0 {
		color: #DAD3BE;
	}
	
	#navPanel .depth-0 {
		color: #DAD3BE;
	}
	""", "phantom":""":root {
    --light-yellow: #F6E96B;
    --light-green: #BEDC74;
    --forest-green: #FFDFD6;
}


/* Example usage */
body {
    background-color: var(--light-yellow);
    color: var(--forest-green);
}

.header {
    background-color: var(--light-green);
    color: var(--forest-green);
}

.button {
    background-color: var(--forest-green);
    color: #fff;
}

.button:hover {
    background-color: var(--light-green);
    color: var(--forest-green);
}
.dropotron li:hover > span, .dropotron li:hover > a {transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				color: #FFDFD6;
			}


	}
	#header h1 {
			color: #FFDFD6;
		}
		.button:active {
			background: #FFDFD6;
		}

		.button {
		background: #FFDFD6;
		color: #fff 
	}
	a:hover {
			color: #FFDFD6;
			border-bottom-color: rgba(255, 255, 255, 0);
		}

			a:hover strong {
				color: #FFDFD6;
			}

	
	h1, h2, h3, h4, h5, h6 {
		color: #E3A5C7;
	}
	#banner
	{
		color:#FFDFD6;
	}
	input[type="button"], input[type="submit"], input[type="reset"], button, .button {
    background: #E3A5C7;
    }
table thead {
	background: #878787;
	color: #694F8E;
	font-weight: 400;
	text-transform: uppercase;
	border: 0;
	box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
	font-size: 0.85em;
	letter-spacing: 2px;
}
input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #ed786a;
		color: #694F8E !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #694F8E;
	}
	#header {
		background: #694F8E;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #694F8E, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #694F8E;
			}
			.dropotron {
				background: #694F8E;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #694F8E;
			}
			#features {
				background: #694F8E;
			}
			
	#banner {
		background: #694F8E;
		color: #694F8E;
	}
	
	#main {
		background: #694F8E;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #694F8E, inset 0px 10px 0px 0px #e5e5e5;
	}
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #694F8E, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #694F8E;
	}
	#navPanel .link.depth-0 {
		color: #694F8E;
	}
	
	#navPanel .depth-0 {
		color: #694F8E;
	}
	body, input, textarea, select {
    color: #E3A5C7;
}
	""", "elegant":""":root {
    --light-yellow: #F6E96B;
    --light-green: #BEDC74;
    --forest-green: #FFDFD6;
}


/* Example usage */
body {
    background-color: var(--light-yellow);
    color: var(--forest-green);
}

.header {
    background-color: var(--light-green);
    color: var(--forest-green);
}

.button {
    background-color: var(--forest-green);
    color: #fff;
}

.button:hover {
    background-color: var(--light-green);
    color: var(--forest-green);
}
.dropotron li:hover > span, .dropotron li:hover > a {transition: color 0.25s ease-in-out, border-bottom-color 0.25s ease-in-out;
				color: #FFDFD6;
			}


	}
	#header h1 {
			color: #FFDFD6;
		}
		.button:active {
			background: #FFDFD6;
		}

		.button {
		background: #FFDFD6;
		color: #fff 
	}
	a:hover {
			color: #FFDFD6;
			border-bottom-color: rgba(255, 255, 255, 0);
		}

			a:hover strong {
				color: #FFDFD6;
			}

	
	h1, h2, h3, h4, h5, h6 {
		color: #FF8225;
	}
	#banner
	{
		color:#FFDFD6;
	}
	input[type="button"], input[type="submit"], input[type="reset"], button, .button {
    background: #FF8225;
    }
	table thead {
	background: #878787;
	color: #173B45;
	font-weight: 400;
	text-transform: uppercase;
	border: 0;
	box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
	font-size: 0.85em;
	letter-spacing: 2px;
}
input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #ed786a;
		color: #173B45 !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #173B45;
	}
	#header {
		background: #173B45;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #173B45, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #173B45;
			}
			.dropotron {
				background: #173B45;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #173B45;
			}
			#features {
				background: #173B45;
			}
			
	#banner {
		background: #173B45;
		color: #173B45;
	}
	
	#main {
		background: #173B45;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #173B45, inset 0px 10px 0px 0px #e5e5e5;
	}
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #173B45, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #173B45;
	}
	#navPanel .link.depth-0 {
		color: #173B45;
	}
	
	#navPanel .depth-0 {
		color: #173B45;
	}
	
	""", "sakura":"""	table thead {
	background: #878787;
	color: #F0A8D0;
	font-weight: 400;
	text-transform: uppercase;
	border: 0;
	box-shadow: 0.125em 0.175em 0 0 rgba(0, 0, 0, 0.125);
	font-size: 0.85em;
	letter-spacing: 2px;
}
input[type="button"],
	input[type="submit"],
	input[type="reset"],
	button,
	.button {
		background: #ed786a;
		color: #F0A8D0 !important;
	}

	.box.excerpt .date {
		background: #878787;
		color: #F0A8D0;
	}
	#header {
		background: #F0A8D0;
	}
	#header > .container {
		box-shadow: inset 0px -8px 0px 0px #F0A8D0, inset 0px -10px 0px 0px #e5e5e5;
	}
	#nav > ul > li.active > a:before,
			#nav > ul > li:hover > a:before {
				color: #F0A8D0;
			}
			.dropotron {
				background: #F0A8D0;
			}
			.dropotron.level-0:after {
				border-bottom: solid 0.75em #F0A8D0;
			}
			#features {
				background: #F0A8D0;
			}
			
	#banner {
		background: #F0A8D0;
		color: #F0A8D0;
	}
	
	#main {
		background: #F0A8D0;
	}
	#content > section,
	#content > article {
		box-shadow: inset 0px 8px 0px 0px #F0A8D0, inset 0px 10px 0px 0px #e5e5e5;
	}
	#sidebar > section,
	#sidebar > article {
		box-shadow: inset 0px 8px 0px 0px #F0A8D0, inset 0px 10px 0px 0px #e5e5e5;
	}

	#footer form input[type="text"]:focus,
	#footer form input[type="email"]:focus,
	#footer form input[type="password"]:focus,
	#footer form select:focus,
	#footer form textarea:focus {
		background: #F0A8D0;
	}
	#navPanel .link.depth-0 {
		color: #F0A8D0;
	}
	
	#navPanel .depth-0 {
		color: #F0A8D0;
	}
	
	#navPanel .link
	{
		color: #fff;
	}
	#content section
	{
		background : #fff;
	}
	#content{
		background : #fff;
	}
	body{
		color:#A02334;
	}
	h1, h2, h3{
		color:white;
	}
	#header h1{
		color:#921A40;
	}"""
}
}
def get_css(template, style):
    return  default_styles[template]["default"]+default_styles[template][style.lower()]