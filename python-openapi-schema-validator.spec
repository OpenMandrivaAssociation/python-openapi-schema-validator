%define module openapi-schema-validator
%define oname openapi_schema_validator

# NOTE Check also openapi-spec-validator and openapi-core for updates when updating this package

Name:		python-openapi-schema-validator
Version:	0.9.0
Release:	1
Summary:	OpenAPI schema validation for Python
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/openapi-schema-validator/
Source0:	https://files.pythonhosted.org/packages/source/o/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
OpenAPI schema validation for Python

%files
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
