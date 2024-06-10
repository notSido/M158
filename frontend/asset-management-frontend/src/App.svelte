<script>
  import { Router, Link, Route } from 'svelte-routing';
  import DepartmentList from './components/DepartmentList.svelte';
  import UserList from './components/UserList.svelte';
  import AssetList from './components/AssetList.svelte';
  import CreateDepartment from './components/CreateDepartment.svelte';
  import CreateUser from './components/CreateUser.svelte';
  import CreateAsset from './components/CreateAsset.svelte';
</script>

<Router>
  <nav>
    <ul>
      <li><Link to="/departments">Departments</Link></li>
      <li><Link to="/users">Users</Link></li>
      <li><Link to="/assets">Assets</Link></li>
      <li><Link to="/create-department">Create Department</Link></li>
      <li><Link to="/create-user">Create User</Link></li>
      <li><Link to="/create-asset">Create Asset</Link></li>
    </ul>
  </nav>

  <Route path="/departments" component={DepartmentList} />
  <Route path="/users" component={UserList} />
  <Route path="/assets" component={AssetList} />
  <Route path="/create-department" component={CreateDepartment} />
  <Route path="/create-user" component={CreateUser} />
  <Route path="/create-asset" component={CreateAsset} />
</Router>

<style>
  nav ul {
    list-style-type: none;
    padding: 0;
  }

  nav ul li {
    display: inline;
    margin-right: 10px;
  }
</style>
