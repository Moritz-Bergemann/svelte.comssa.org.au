<script lang="ts">
	import MemberProfile from '$lib/components/MemberProfile.svelte';
	import NavBar from '$lib/components/NavBar/NavBar.svelte';
</script>

<NavBar showCAlways={true} />

<div class="content">
	<h1>Our Committee</h1>

	<p>
		Something something committee. If you are keen on joining the committee or sub-committee,
		contact a comssa member at one of our official channels!
	</p>
</div>

<!-- TODO Andrew, Tui and Lauren need to be downsampled - their images are ~10x larger than all others -->
<div class="content-wide">
	<h2>Executive Committee</h2>

	<div class="profile-row">
		<MemberProfile
			name={'Warittha Rayabsri'}
			title={'President'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1679318914/ComSSA-Website/Profile/Warittha%20Rayabsri.jpg'}
		/>
		<MemberProfile
			name={'Samuel Suhardiman'}
			title={'Vice President'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1679318918/ComSSA-Website/Profile/Samuel%20Suhardiman.jpg'}
		/>
		<MemberProfile
			name={'Andrew Owens'}
			title={'Treasurer'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1679318918/ComSSA-Website/Profile/Andrew%20Owens.png'}
		/>
		<MemberProfile
			name={'Tui Warihana'}
			title={'Secretary'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1679318916/ComSSA-Website/Profile/Tui%20Warihana.png'}
		/>
	</div>
	<h2>Ordinary Committee</h2>
	<div class="profile-row">
		<MemberProfile
			name={'Nicholas Lim'}
			title={'Events Coordinator'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1691929077/ComSSA-Website/Profile/Nicholas%20Lim.jpg'}
		/>
		<MemberProfile
			name={'Lauren Rothnie'}
			title={'Marketing Coordinator'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1679318920/ComSSA-Website/Profile/Lauren%20Rothnie.png'}
		/>
		<MemberProfile
			name={'Sean McGinty'}
			title={'Technical Coordinator'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1679318917/ComSSA-Website/Profile/Sean%20McGinty.jpg'}
		/>
		<MemberProfile
			name={'Nicholas Wright'}
			title={'Revision Session Coordinator'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1679318916/ComSSA-Website/Profile/Nicholas%20Wright.jpg'}
		/>
		<MemberProfile
			name={'Ethan Olson'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1679318914/ComSSA-Website/Profile/Ethan%20Olson.jpg'}
		/>
		<MemberProfile
			name={'Franco Forgione Velazco'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1679318917/ComSSA-Website/Profile/Franco%20Forgione%20Velazco.png'}
		/>
		<MemberProfile
			name={'Haylee Jackson'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1691929076/ComSSA-Website/Profile/Haylee%20Jackson.jpg'}
		/>
		<MemberProfile
			name={'Justin Pan'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1691929076/ComSSA-Website/Profile/Justin%20Pan.jpg'}
		/>
		<MemberProfile
			name={'Sean Phay'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1691929077/ComSSA-Website/Profile/Sean%20Phay.jpg'}
		/>
		<MemberProfile
			name={'Mori Anderson'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1691929076/ComSSA-Website/Profile/Mori%20Arvidson.jpg'}
		/>
		<MemberProfile
			name={'Kai Chen Chai'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1691929076/ComSSA-Website/Profile/Kai%20Chen%20Chai.jpg'}
		/>
		<MemberProfile
			name={'Daniela Degasperi'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1691929076/ComSSA-Website/Profile/Daniela%20Degasperi.jpg'}
		/>
		<MemberProfile
			name={'Clarissa Sutandi'}
			imageSource={'https://res.cloudinary.com/dec6mijn3/image/upload/v1691929076/ComSSA-Website/Profile/Clarissa%20Sutandi.jpg'}
		/>
		
	</div>
</div>

<div class="content">
	<h2>Subcommittee</h2>

	<p>Subcommittee members somethign something easy to join, contact us on discord! TODO</p>
</div>

<style>
	.profile-row {
		display: flex;
		align-items: center;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: space-evenly;
		width: 100%;
	}

	.content-wide {
		max-width: 70em;
		margin: auto;
	}
</style>
