Name:		python-openapi-schema-validator
Version:	0.8.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/openapi_schema_validator/openapi_schema_validator-%{version}.tar.gz
Summary:	OpenAPI schema validation for Python
URL:		https://pypi.org/project/openapi-schema-validator/
License:	BSD-3-Clause
Group:		Development/Python
BuildRequires:	python%{pyver}dist(poetry-core)
BuildSystem:	python
BuildArch:	noarch

%description
OpenAPI schema validation for Python

%files
%{py_sitedir}/openapi_schema_validator
%{py_sitedir}/openapi_schema_validator-*.*-info
