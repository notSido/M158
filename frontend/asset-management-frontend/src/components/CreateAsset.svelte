<script>
  import { onMount } from 'svelte';
  import axios from 'axios';

  let name = '';
  let type = '';
  let serial_nr = '';
  let users = [];
  let user_id = '';

  onMount(async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/users/');
      users = response.data;
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  });

  const createAsset = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/assets/', { name, type, serial_nr, user_id });
      alert('Asset created successfully');
      name = '';
      type = '';
      serial_nr = '';
      user_id = '';
    } catch (error) {
      console.error('Error creating asset:', error);
    }
  };
</script>

<h2>Create Asset</h2>
<form on:submit|preventDefault={createAsset}>
  <input bind:value={name} type="text" placeholder="Asset Name" />
  <input bind:value={type} type="text" placeholder="Asset Type" />
  <input bind:value={serial_nr} type="text" placeholder="Serial Number" />
  <select bind:value={user_id}>
    <option value="" disabled selected>Select User</option>
    {#each users as user}
      <option value={user.id}>{user.name}</option>
    {/each}
  </select>
  <button type="submit">Create</button>
</form>
