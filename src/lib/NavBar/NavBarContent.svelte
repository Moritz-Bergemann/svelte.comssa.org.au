<script lang="ts">
export let showC = false;
</script>

<div class="navbar-items">
	<a href="contact" class="navbar-item underlined"><span class="underline">Socials</span></a>
	<a href="events" class="navbar-item underlined"><span class="underline">Events</span></a>
	<a href="committee" class="navbar-item underlined"><span class="underline">Committee</span></a>
	<div class="navbar-item">
		{#if showC}
			<a href="/"><img alt="ComSSA" src="/assets/comssa-c.svg" /></a>
		{/if}
	</div>
	<a
		href="https://drive.google.com/drive/folders/1HC9XAeFVHCOfjcJeRfK9hbmzNI1Ux2JX"
		class="navbar-item underlined"><span class="underline">Meeting Minutes</span></a
	>
	<a href="sponsors" class="navbar-item underlined"><span class="underline">Sponsors</span></a>
	<a href="join" class="navbar-item underlined"><span class="underline">Join Now!</span></a>
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
		max-width: 150px;
		font-family: 'WaveHaus SemiBold';
		display: block;
		flex: auto;
		margin-left: auto;
		margin-right: auto;
		text-align: center;
		color: black;
		text-decoration: none;
	}

	.navbar-items a img {
		height: 50px;
	}

	.navbar-items a :hover {
		color: var(--comssa-orange);
		transition: 0.3s;
	}

	.underlined:hover:after {
		background: var(--comssa-orange);
		transition: 0.3s;
	}
</style>
