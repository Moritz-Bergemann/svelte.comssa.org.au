<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import NavBar from '$lib/NavBar.svelte';
	import ComssaTyper from '$lib/ComssaTyper.svelte';

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

<body>
	<!-- TODO add background little images -->
	<!-- TODO make everything sort of float, it would be cool if it interacts with with the cursor as well -->
	<NavBar dynamic={true}/>

	<div id="landing" class="landing">
		<div style="margin: auto;">
			<img src="/assets/comssa-c.png" style="margin: auto; display: block;" width="250rem" />
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
				<a class="landing-button" href="LINK-TODO">Latest News</a>
			</div>
		</div>
	</div>

	<div class="content">
		<!-- Welcomes -->
		<div style="display: flex; flex-direction: row; justify-content: space-evenly;">
			<div class="intro-item">
				<p>Social Events</p>
				<img src="/assets/temp-photo.png"/>
			</div>
			<div class="intro-item">
				<p>Industry Networking</p>
				<img src="/assets/temp-photo.png"/>
			</div>
			<div class="intro-item">
				<p>Study Support</p>
				<img src="/assets/temp-photo.png"/>
			</div>
		</div>

		<div class="divider" />

		<div>
			<h1>Who are we?</h1>
			<div class="paragraph-float-right">
				<p>
					Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi non tristique lacus.
					Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque in blandit purus.
					Nulla odio ante, volutpat id aliquam quis, pharetra eget urna. Proin sollicitudin ipsum
					sapien, aliquam porttitor dui maximus eget. Vivamus bibendum tristique libero sit amet
					porttitor. Pellentesque eu facilisis nibh. Maecenas ac sapien a justo rhoncus pretium
					vitae vel est. Suspendisse ornare sodales est, quis mattis orci dignissim vitae. Orci
					varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Mauris
					sit amet arcu eu enim hendrerit bibendum id nec magna. Donec in augue vel erat dapibus
					suscipit. Ut eu bibendum lacus. Pellentesque ultrices ipsum id nunc venenatis, ac
					condimentum erat tincidunt. Nam sagittis blandit ipsum vel molestie. Morbi ultricies non
					nunc et molestie. Morbi volutpat pulvinar odio ut tincidunt. Fusce pharetra vehicula
					rhoncus. Nullam nibh dolor, efficitur sit amet leo eu, volutpat faucibus velit.
				</p>
			</div>

			<img src="/assets/temp-photo.png" style="float: left; width: 40%; margin: auto;" />
		</div>
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
		height: 100px;
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
		background-color: var(--comssa-orange); /* Green */
		box-shadow: 0px 8px 15px rgba(245, 131, 31, 0.5);
		transition: all 0.3s ease 0s;
	}

	.intro-item {
		padding-left: 20px;
		padding-right: 20px;
	}

	.intro-item img {
		max-width: 100%;
	}

	.intro-item p {
		font-size: 1.5rem;
		text-align: center;
		font-family: "WaveHaus SemiBold";
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
</style>
