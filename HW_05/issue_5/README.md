python -m pytest test_what_is_year_now.py

по идее, далее нужно делать: python -m pytest test_what_is_year_now.py --cov . --cov-report html > result.txt
но у меня выбрасывает ошибку:

python -m pytest test_what_is_year_now.py --cov . --cov-report html > result.txt
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/Users/administrator/venv/lib/python3.8/site-packages/pytest/__main__.py", line 5, in <module>
    raise SystemExit(pytest.console_main())
  File "/Users/administrator/venv/lib/python3.8/site-packages/_pytest/config/__init__.py", line 185, in console_main
    code = main()
  File "/Users/administrator/venv/lib/python3.8/site-packages/_pytest/config/__init__.py", line 143, in main
    config = _prepareconfig(args, plugins)
  File "/Users/administrator/venv/lib/python3.8/site-packages/_pytest/config/__init__.py", line 318, in _prepareconfig
    config = pluginmanager.hook.pytest_cmdline_parse(
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/hooks.py", line 286, in __call__
    return self._hookexec(self, self.get_hookimpls(), kwargs)
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/manager.py", line 93, in _hookexec
    return self._inner_hookexec(hook, methods, kwargs)
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/manager.py", line 84, in <lambda>
    self._inner_hookexec = lambda hook, methods, kwargs: hook.multicall(
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/callers.py", line 203, in _multicall
    gen.send(outcome)
  File "/Users/administrator/venv/lib/python3.8/site-packages/_pytest/helpconfig.py", line 100, in pytest_cmdline_parse
    config: Config = outcome.get_result()
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/callers.py", line 80, in get_result
    raise ex[1].with_traceback(ex[2])
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/callers.py", line 187, in _multicall
    res = hook_impl.function(*args)
  File "/Users/administrator/venv/lib/python3.8/site-packages/_pytest/config/__init__.py", line 1003, in pytest_cmdline_parse
    self.parse(args)
  File "/Users/administrator/venv/lib/python3.8/site-packages/_pytest/config/__init__.py", line 1283, in parse
    self._preparse(args, addopts=addopts)
  File "/Users/administrator/venv/lib/python3.8/site-packages/_pytest/config/__init__.py", line 1191, in _preparse
    self.hook.pytest_load_initial_conftests(
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/hooks.py", line 286, in __call__
    return self._hookexec(self, self.get_hookimpls(), kwargs)
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/manager.py", line 93, in _hookexec
    return self._inner_hookexec(hook, methods, kwargs)
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/manager.py", line 84, in <lambda>
    self._inner_hookexec = lambda hook, methods, kwargs: hook.multicall(
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/callers.py", line 208, in _multicall
    return outcome.get_result()
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/callers.py", line 80, in get_result
    raise ex[1].with_traceback(ex[2])
  File "/Users/administrator/venv/lib/python3.8/site-packages/pluggy/callers.py", line 187, in _multicall
    res = hook_impl.function(*args)
  File "/Users/administrator/venv/lib/python3.8/site-packages/pytest_cov/plugin.py", line 126, in pytest_load_initial_conftests
    plugin = CovPlugin(options, early_config.pluginmanager)
  File "/Users/administrator/venv/lib/python3.8/site-packages/pytest_cov/plugin.py", line 172, in __init__
    from . import engine
  File "/Users/administrator/venv/lib/python3.8/site-packages/_pytest/assertion/rewrite.py", line 170, in exec_module
    exec(co, module.__dict__)
  File "/Users/administrator/venv/lib/python3.8/site-packages/pytest_cov/engine.py", line 11, in <module>
    from coverage.data import CoverageData
ModuleNotFoundError: No module named 'coverage.data'; 'coverage' is not a package

Посмотрел решения на stackoverflow, скорее всего, проблема в том, что на компьютере установлено несколько версий python, однако из решений с сайта пока ничего не подошло. ¯\_(ツ)_/¯
