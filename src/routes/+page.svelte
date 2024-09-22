<script lang="ts">
	import NavBar from '$lib/components/NavBar/NavBar.svelte';
	import ComssaTyper from '$lib/components/ComssaTyper.svelte';
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
				<a class="landing-button" href="#join-comssa">Join ComSSA!</a>
				<a class="landing-button" href="#current-events">Latest News</a>
			</div>
		</div>
	</div>

	<div class="content-wide">
		<!-- Welcomes -->
		<div style="display: flex; flex-direction: row; justify-content: space-evenly; flex-wrap: wrap; flex-direction: row;">
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

		<div>
			<h2>Current Events</h2>
			<div id="current-events" class="anchor" />
			<div class="poster-container">
				<img
					src="https://res.cloudinary.com/dec6mijn3/image/upload/v1692112101/ComSSA-Website/posters/hackathon-23_byfxzm.png"
				/>
			</div>
		</div>

		<div class="divider" />

		<h2>Who are we?</h2>
		<div class="horizontal-items">
			<div class="montserrat-normal" style="min-width: 25rem;">
				<p>
					ComSSA is the club that supports computing, computer engineering, and networking students
					at Curtin University. We also support non-computing students by providing events and
					services that give like minded individuals (anyone interested in programming or computing)
					a space to find support, socialise and communicate.
				</p>
				<p>
					You do not need to be a computing student. Membership is open to everyone, even if you're
					not a student!
				</p>
				<p>
					Committee members can be found throughout the level 2 labs in building 314 or in the
					ComSSA common room (314.345). <strong
						><a href="/committee">Not sure who we are?</a></strong
					>
				</p>
				<p>
					ComSSA provides a wide range of events and services for its members, such as academic
					assistance, social events and industry orientated events.
				</p>
				<p>
					ComSSA is affiliated with Curtin Student Guild which means if you are a Curtin student and
					have a voucher from the guild diary then membership is free.
				</p>
			</div>
			<div style="min-width: 20rem; max-width: 40rem; margin: auto;">
				<img src="/assets/temp-photo.png" style="width: 100%;" />
			</div>
		</div>

		<div class="divider" />

		<div class="full-section">
			<div class="anchor" id="join-comssa" />
			<h2 id="join-comssa">Join ComSSA!</h2>

			<img src="/assets/temp-photo.png" style="max-width: 30rem; margin: auto; display: block;" />

			<br />

			<p class="centered">
				If you'd like to join ComSSA online, you can do so easily through TidyHQ. Just click the
				link below:
			</p>

			<br />
			<a
				class="landing-button"
				style="margin: auto; max-width: 8rem; display: block;"
				href="https://comssa.tidyhq.com/public/membership_levels/9b41b2d0d56e">Join Online</a
			>
			<br />

			<p class="centered">
				You can also join in-person - just talk to any of our committee members, either at one of
				our events or in the ComSSA Common Room! This is also the way to join if you would like to
				use a Curtin Student Guild voucher. If you have any more questions, please 
				<a href="/"><strong>contact us!</strong></a>
			</p>
		</div>
	</div>
</body>

<style>
	.divider {
		height: 4rem;
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

	.horizontal-items {
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: space-between;
		align-items: center;
		gap: 5rem;
	}

	.horizontal-items div {
		flex: 1;
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
