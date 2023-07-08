<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import '../styles/app.css';

	onMount(() => {
		const SHOW_SCROLL_NAVBAR_HEIGHT = 20;

		let showNavbar: boolean = true;

		// window.onscroll = () => {
		//     if (window.scrollY > SHOW_SCROLL_NAVBAR_HEIGHT) {
		//         console.log("there!");
		//         showNavbar = true;
		//     } else {
		//         console.log("not there!");
		//         showNavbar = false;
		//     }
		// }
	});
</script>

<main>
	<!-- TODO add background little images -->
	<!-- TODO make everything sort of float, it would be cool if it interacts with with the cursor as well -->
	<div id="landing-screen">
		<div class="logo-container">
			<p class="logo">
				<span class="commsa-blue-text">Com</span><span class="comssa-black-text">puter</span> <br />
				<span class="commsa-blue-text">S</span><span class="comssa-black-text">cience</span> <br />
				<span class="commsa-blue-text">S</span><span class="comssa-black-text">tudents</span> <br />
				<span class="commsa-blue-text">A</span><span class="comssa-black-text">ssociation</span>
			</p>
			<img src="/assets/temp-photo.png" class="landing-image landing-image-1"/>
			<img src="/assets/temp-photo.png" class="landing-image landing-image-2"/>
			<img src="/assets/temp-photo.png" class="landing-image landing-image-3"/>
			<p class="tagline">
				Curtin University's and Western Australia's <span
					class="comssa-orange-text comssa-bold-text">largest</span
				> computing student association!
			</p>
		</div>

		<a class="join-button" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">Join Now!</a>

		<div class="comssa-poster">
			<p>Latest News!</p>
			<img src="/assets/poster.png" />
			<!-- TODO put a cool little line burst around this, like this https://www.youtube.com/watch?v=hODmxWZ4H_U -->
		</div>
	</div>

	<div class="content">
		<div>
			<div class="paragraph-float-right">
				<h1>Who are we?</h1>
				<p>
					Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi non tristique lacus. Interdum
					et malesuada fames ac ante ipsum primis in faucibus. Quisque in blandit purus. Nulla odio
					ante, volutpat id aliquam quis, pharetra eget urna. Proin sollicitudin ipsum sapien, aliquam
					porttitor dui maximus eget. Vivamus bibendum tristique libero sit amet porttitor.
					Pellentesque eu facilisis nibh. Maecenas ac sapien a justo rhoncus pretium vitae vel est.
					Suspendisse ornare sodales est, quis mattis orci dignissim vitae. Orci varius natoque
					penatibus et magnis dis parturient montes, nascetur ridiculus mus. Mauris sit amet arcu eu
					enim hendrerit bibendum id nec magna. Donec in augue vel erat dapibus suscipit. Ut eu
					bibendum lacus. Pellentesque ultrices ipsum id nunc venenatis, ac condimentum erat
					tincidunt. Nam sagittis blandit ipsum vel molestie. Morbi ultricies non nunc et molestie.
					Morbi volutpat pulvinar odio ut tincidunt. Fusce pharetra vehicula rhoncus. Nullam nibh
					dolor, efficitur sit amet leo eu, volutpat faucibus velit.
				</p>
			</div>

			<img src="/assets/temp-photo.png" style="float: left; width: 40%; margin: auto;"/>
		</div>
	</div>
	<div id="navbar" class="navbar">
        <div class="navbar-items">
            <div>bean1</div>
            <div>bean2</div>
            <div>bean3</div>
        </div>
    </div>
</main>

<style>
	:root {
		--comssa-blue: #4459a5;
		--comssa-secondary-blue: #7ea3cc;
		--comssa-orange: #f5831f;
		--comssa-black: #404040;
	}

	.logo-container {
		position: absolute;
		top: 100px;
		left: 100px;
		width: 400px;
	}

	.logo {
		letter-spacing: 0.15rem;
		line-height: 1;
		font-family: 'Wavehaus Bold';
		font-size: 75px;
		margin-top: 0;
		margin-bottom: 0;
		text-shadow: -5px -4px 3px rgba(128, 128, 128, 0.5);
	}

	.tagline {
		font-family: 'Wavehaus Semibold';
		font-size: 20px;
	}

	.join-button {
		font-family: 'Wavehaus Bold';
		letter-spacing: 0.15rem;

		background-color: var(--comssa-blue); /* Green */
		border: none;
		color: white;
		padding: 20px;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 16px;
		margin: 4px 2px;
		cursor: pointer;
        box-shadow: -10px -8px 6px rgba(128, 128, 128, 0.5);

		border-radius: 15px;

		position: absolute;
		top: 500px;
		left: 100px;
	}

	.comssa-poster {
		position: absolute;
		top: 25px;
		left: 1000px;
		display: block;
		text-align: center;
	}

	.comssa-poster img {
		border-radius: 2%;
		height: 65vh;
        box-shadow: -10px -8px 6px rgba(128, 128, 128, 0.5);
	}

	.comssa-poster p {
		font-size: 30px;
		margin-bottom: 0;
		font-family: "Wavehaus Bold";
		color: var(--comssa-orange);
		transform: rotate(-1deg);
	}

	/* TODO adjust these positions to make it look nicer */
	.landing-image {
		position: absolute;
		border-radius: 3%;
		width: 20vw;
        box-shadow: -10px -8px 6px rgba(128, 128, 128, 0.5);
	}

	.landing-image-1 {
		top: 0vh;
		left: 25vw;
	}

	.landing-image-2 {
		top: 20vh;
		left: 35vw;
	}

	.landing-image-3 {
		top: 40vh;
		left: 30vw;
	}

	.commsa-blue-text {
		color: var(--comssa-blue);
	}

	.comssa-black-text {
		color: var(--comssa-black);
	}

	.comssa-orange-text {
		color: var(--comssa-orange);
	}

	.comssa-bold-text {
		font-family: 'Wavehaus bold';
	}

	.paragraph-float-right {
		text-align: right;
		width: 50%;
		float:right;
	}

	.paragraph-float-right p {
		text-align: justify;
	}

	#landing-screen {
		height: 100vh;
		/* TODO replace this gross gradient with a pretty background*/
		/* background-image: linear-gradient(to bottom, white, var(--comssa-secondary-blue)); */
		/* background-color: var(--comssa-secondary-blue); */
		position: relative;
	}

	.content {
		max-width: 60em;
		margin: auto;
	}

	h1 {
		font-family: 'Wavehaus SemiBold';
		letter-spacing: 0.15rem;
	}
</style>
