<script lang="ts">
	import NavBar from '$lib/components/NavBar/NavBar.svelte';
	import ComssaTyper from '$lib/components/ComssaTyper.svelte';
	import { element } from 'svelte/internal';

	function scrollTo(id: string, applyScrollbarOffset = true) {
		let yOffset = 0;
		if (applyScrollbarOffset) {
			const scrollbar = document.getElementsByClassName('navbar')![0];

			yOffset =
				-1 *
					Math.abs(
						scrollbar.getBoundingClientRect().top - scrollbar.getBoundingClientRect().bottom
					) -
				10;
		}

		const element = document.getElementById(id);
		const y = element!.getBoundingClientRect().top + yOffset;

		window.scrollTo({ top: y, behavior: 'smooth' });
	}
</script>

<body>
	<NavBar showCAlways={false} />

	<div id="landing" class="landing">
		<div style="margin: auto;">
			<img src="/assets/comssa-c.svg" style="margin: auto; display: block;" width="250rem" />
			<ComssaTyper />
			<div
				style="margin-top: 1rem; font-family: WaveHaus SemiBold; text-align: center; font-size: 1.5rem;"
			>
				Western Australia's <span class="comssa-orange-text" style="font-family: WaveHaus Bold"
					>largest</span
				> computing student association!
			</div>

			<div
				style="margin-top: 2rem; display: flex; justify-content: center; flex-direction: row; gap: 4rem;"
			>
				<a class="landing-button" href="LINK-TODO">Join Now!</a>
				<button class="landing-button" on:click={() => scrollTo('current-events')}
					>Latest News</button
				>
			</div>
		</div>
	</div>

	<div class="content">
		<!-- Welcomes -->
		<div style="display: flex; flex-direction: row; justify-content: space-evenly;">
			<div class="intro-item">
				<p>Social Events</p>
				<img
					src="https://res.cloudinary.com/dec6mijn3/image/upload/v1692107420/ComSSA-Website/events/grill-the-department-2023/17_hqzttg.jpg"
				/>
			</div>
			<div class="intro-item">
				<p>Industry Networking</p>
				<img
					src="https://res.cloudinary.com/dec6mijn3/image/upload/v1692107445/ComSSA-Website/events/hackathon-2023/11_jslw2e.jpg"
				/>
			</div>
			<div class="intro-item">
				<p>Study Support</p>
				<img
					src="https://res.cloudinary.com/dec6mijn3/image/upload/v1692107362/ComSSA-Website/events/amazing-tech-race-2023/19_ud1cg7.jpg"
				/>
			</div>
		</div>

		<div class="divider" />

		<h2>Current Events</h2>
		<div id="current-events" class="poster-container">
			<img
				src="https://res.cloudinary.com/dec6mijn3/image/upload/v1692112101/ComSSA-Website/posters/hackathon-23_byfxzm.png"
			/>
		</div>

		<div class="divider" />

		<h2>Who are we?</h2>
		<div class="paragraph-float-right">
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

		<img src="/assets/temp-photo.png" style="float: left; width: 40%; margin: auto;" />
	</div>
</body>

<style>
	.logo-container {
		position: absolute;
		top: 100px;
		left: 100px;
		width: 400px;
	}

	.divider {
		height: 4rem;
	}

	.logo {
		letter-spacing: 0.15rem;
		line-height: 1;
		font-family: 'Wavehaus Bold';
		font-size: 75px;
		margin-top: 0;
		margin-bottom: 0;
	}

	.tagline {
		font-family: 'Wavehaus Semibold';
		font-size: 20px;
	}

	.landing {
		position: relative;
		width: 100vw;
		padding-top: 10px;
	}

	.landing-button {
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

		box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
		border-radius: 45px;
	}

	.landing-button:hover {
		background-color: var(--comssa-orange);
		box-shadow: 0px 8px 15px rgba(245, 131, 31, 0.5);
		transition: all 0.3s ease 0s;
	}

	.intro-item {
		padding-left: 2rem;
		padding-right: 2rem;
	}

	.intro-item img {
		width: 20rem;
		background-size: cover;
		border-radius: 2rem;
	}

	.intro-item p {
		font-size: 1.5rem;
		text-align: center;
		font-family: 'WaveHaus SemiBold';
	}

	.paragraph-float-right {
		text-align: right;
		width: 50%;
		float: right;
		margin: 0 !important;
	}

	.paragraph-float-right p {
		text-align: justify;
	}

	.content {
		max-width: 60em;
		margin: auto;
	}

	h1 {
		font-family: 'Wavehaus SemiBold';
		letter-spacing: 0.15rem;
	}

	.poster-container {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: space-evenly;
		height: 85vh;
		max-width: 90vw;
	}

	.poster-container img {
		border-radius: 2rem;
		max-height: 100%;
	}
</style>
