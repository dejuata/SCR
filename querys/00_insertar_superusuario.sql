INSERT INTO public.auth_user(
            id, password, last_login, is_superuser, username, first_name,
            last_name, email, is_staff, is_active, date_joined)
    VALUES ('0', 'pbkdf2_sha256$30000$JKtHlgC7pG1m$mKXVnUL5POfqaxkdFFDOTbNkbRyTZzAoQZEMO0n5TLA=', '2017-04-14', True, 'admin', 'admin',
            'admin', 'admin@scr.com', True, True, '2017-04-14');
