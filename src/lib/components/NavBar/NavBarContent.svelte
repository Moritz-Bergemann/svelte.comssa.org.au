<script lang="ts">
	export let showC: boolean = false;
</script>

<div class="navbar-items">
	<a href="contact" class="navbar-item underlined">Socials</a>
	<a href="events" class="navbar-item underlined">Events</a>
	<a href="committee" class="navbar-item underlined">Committee</a>
	<div class="navbar-item">
		{#if showC}
			<a href="/"><img class="comssa-c" alt="ComSSA" src="/assets/comssa-c-black.png" /></a>
		{:else}
			<div class="comssa-c"/>
		{/if}
	</div>
	<a
		href="https://drive.google.com/drive/folders/1HC9XAeFVHCOfjcJeRfK9hbmzNI1Ux2JX"
		class="navbar-item underlined">Meeting Minutes</a
	>
	<a href="sponsors" class="navbar-item underlined">Sponsors</a>
	<a href="join" class="navbar-item underlined button">Join Now!</a>
</div>

<style>
	.navbar-items {
		padding-left: 10%;
		padding-right: 10%;
		height: 100%;
		display: flex;
		text-decoration: none;
		flex-direction: row;
		align-items: center;
	}

	.navbar-item {
		max-width: 10rem;
		font-family: 'WaveHaus SemiBold';
		display: block;
		flex: auto;
		margin-left: auto;
		margin-right: auto;
		text-align: center;
		color: black;
		text-decoration: none;
	}

	.comssa-c {
		width: 3rem;
	}
	
	.navbar-items a img {
		filter: invert(36%) sepia(12%) saturate(2552%) hue-rotate(190deg) brightness(95%) contrast(96%);
	}

	.navbar-items a:hover img {
		filter: invert(51%) sepia(40%) saturate(1121%) hue-rotate(347deg) brightness(107%) contrast(92%);
		transition: 1s;
	}

	.navbar-items a:hover {
		color: var(--comssa-orange);
		transition: 0.3s;
	}

	.button {
		font-family: 'Wavehaus Bold';
		letter-spacing: 0.15rem;

		background-color: var(--comssa-blue);
		border: none;
		color: white;
		padding: 0.75rem;
		text-align: center;
		text-decoration: none;
		cursor: pointer;


		box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
		border-radius: 45px;
	}

	.navbar-items .button:hover {
		color: white;
	}

	.button:hover {
		background-color: var(--comssa-orange);
		box-shadow: 0px 8px 15px rgba(245, 131, 31, 0.5);
		transition: all 0.3s ease 0s;
	}
</style>
