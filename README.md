# `Users`
The user management for the wooze application. The api endpoints are defined below

## Endpoints
<table>
<tr>
<th>endpoint</th>
<th>method</th>
<th>parameters</th>
</tr>
<tr>
<td><code>/register</code></td>
<td><code>POST</code></td>
<td>

<code>email</code> Email of the user

<code>Password</code> The account password
</td>
</tr>
<tr>
<td><code>/login</code></td>
<td><code>POST</code></td>
<td>
<code>username</code> The username

<code>email</code> Email of the user

<code>Password</code> The account password

<code>token</code> The secret token
</td>
</tr>
</table>