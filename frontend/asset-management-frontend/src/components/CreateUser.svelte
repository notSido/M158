<script>
  import { onMount } from 'svelte';
  import axios from 'axios';

  let name = '';
  let username = '';
  let departments = [];
  let department_id = '';

  onMount(async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/departments/');
      departments = response.data;
    } catch (error) {
      console.error('Error fetching departments:', error);
    }
  });

  const createUser = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/users/', { name, username, department_id });
      alert('User created successfully');
      name = '';
      username = '';
      department_id = '';
    } catch (error) {
      console.error('Error creating user:', error);
    }
  };
</script>

<h2>Create User</h2>
<form on:submit|preventDefault={createUser}>
  <input bind:value={name} type="text" placeholder="Name" />
  <input bind:value={username} type="text" placeholder="Username" />
  <select bind:value={department_id}>
    <option value="" disabled selected>Select Department</option>
    {#each departments as department}
      <option value={department.id}>{department.name}</option>
    {/each}
  </select>
  <button type="submit">Create</button>
</form>
