Name:		python-annotated-doc
Version:	0.0.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/annotated_doc/annotated_doc-%{version}.tar.gz
Summary:	Document parameters, class attributes, return types, and variables inline, with Annotated.
URL:		https://pypi.org/project/annotated_doc/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Document parameters, class attributes, return types, and variables inline, with Annotated.

%files
%{py_sitedir}/annotated_doc
%{py_sitedir}/annotated_doc-*.*-info
