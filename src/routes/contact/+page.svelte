<script lang="ts">
	import NavBar from '$lib/components/NavBar/NavBar.svelte';
	import Socials from '$lib/components/Socials.svelte';

	// import DataModel from '$lib/model/DataModel.ts'; TODO
</script>

<body>
	<NavBar showCAlways={true} />

	<div class="content">
		<h1>Contact Us</h1>

		<div>
			<p>
				The best place to contact the ComSSA committee and keep up with future events is on <b
					><a href="https://discord.gg/SuwfFfjYJB" class="comssa-blue-text">Discord</a></b
				>. Chat with us in the general channels or via direct message! All ComSSA committee members
				are indicated with a special role. Our events also regularly get posted and hosted on the
				<b
					><a href="https://www.facebook.com/ComSSACurtin/" class="comssa-blue-text"
						>ComSSA Facebook Page</a
					></b
				>.
			</p>

			<p>
				For additional or business enquiries, please contact us at <b
					><a class="comssa-blue-text" href="mailto://club@comssa.org.au">club@comssa.org.au</a></b
				>.
			</p>
		</div>

		<div class="divider" />
		<h2>Official Accounts</h2>
		<div>
			<Socials color="original" logoSize="4rem" />
		</div>
	</div>
</body>

<style>
	.divider {
		height: 1rem;
	}
</style>
