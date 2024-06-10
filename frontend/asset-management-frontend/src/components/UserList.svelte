<script>
  import { onMount } from 'svelte';
  import axios from 'axios';

  let users = [];

  onMount(async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/users/');
      users = response.data;
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  });
</script>

<h2>Users</h2>
<ul>
  {#each users as user}
    <li>{user.name} ({user.username})</li>
  {/each}
</ul>
