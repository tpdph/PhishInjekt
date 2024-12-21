"use strict";(globalThis.webpackChunk=globalThis.webpackChunk||[]).push([["ui_packages_item-picker_components_RepositoryPicker_tsx"],{15629:(e,l,a)=>{a.d(l,{A:()=>i});let n=function(){var e={defaultValue:!1,kind:"LocalArgument",name:"includeTemplates"},l={defaultValue:null,kind:"LocalArgument",name:"name"},a={defaultValue:null,kind:"LocalArgument",name:"owner"},n=[{kind:"Variable",name:"name",variableName:"name"},{kind:"Variable",name:"owner",variableName:"owner"}],i={alias:null,args:null,kind:"ScalarField",name:"id",storageKey:null},s={alias:null,args:null,kind:"ScalarField",name:"databaseId",storageKey:null},r={alias:null,args:null,kind:"ScalarField",name:"name",storageKey:null},t={alias:null,args:null,kind:"ScalarField",name:"nameWithOwner",storageKey:null},u={alias:null,args:null,kind:"ScalarField",name:"login",storageKey:null},o={alias:null,args:[{kind:"Literal",name:"size",value:64}],kind:"ScalarField",name:"avatarUrl",storageKey:"avatarUrl(size:64)"},d={alias:null,args:null,kind:"ScalarField",name:"isPrivate",storageKey:null},c={alias:null,args:null,kind:"ScalarField",name:"visibility",storageKey:null},g={alias:null,args:null,kind:"ScalarField",name:"isArchived",storageKey:null},m={alias:null,args:null,kind:"ScalarField",name:"isInOrganization",storageKey:null},y={alias:null,args:null,kind:"ScalarField",name:"hasIssuesEnabled",storageKey:null},k={alias:null,args:null,kind:"ScalarField",name:"slashCommandsEnabled",storageKey:null},p={alias:null,args:null,kind:"ScalarField",name:"viewerCanPush",storageKey:null},F={alias:null,args:null,concreteType:"IssueCreationPermissions",kind:"LinkedField",name:"viewerIssueCreationPermissions",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"labelable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"milestoneable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"assignable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"triageable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"typeable",storageKey:null}],storageKey:null},K={alias:null,args:null,kind:"ScalarField",name:"securityPolicyUrl",storageKey:null},S={alias:null,args:null,kind:"ScalarField",name:"contributingFileUrl",storageKey:null},b={alias:null,args:null,kind:"ScalarField",name:"codeOfConductFileUrl",storageKey:null},f={alias:null,args:null,kind:"ScalarField",name:"shortDescriptionHTML",storageKey:null},I={alias:null,args:null,concreteType:"RepositoryPlanFeatures",kind:"LinkedField",name:"planFeatures",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"maximumAssignees",storageKey:null}],storageKey:null},h={alias:null,args:null,kind:"ScalarField",name:"isSecurityPolicyEnabled",storageKey:null},L={alias:null,args:null,kind:"ScalarField",name:"isBlankIssuesEnabled",storageKey:null},T={alias:null,args:null,kind:"ScalarField",name:"templateTreeUrl",storageKey:null},R={alias:null,args:null,kind:"ScalarField",name:"__typename",storageKey:null},v={alias:null,args:null,kind:"ScalarField",name:"about",storageKey:null},P={alias:null,args:null,kind:"ScalarField",name:"filename",storageKey:null},w={alias:null,args:null,kind:"ScalarField",name:"body",storageKey:null},C={alias:null,args:null,kind:"ScalarField",name:"title",storageKey:null},E={kind:"Literal",name:"first",value:20},D=[E,{kind:"Literal",name:"orderBy",value:{direction:"ASC",field:"NAME"}}],A={alias:null,args:null,kind:"ScalarField",name:"color",storageKey:null},V={alias:null,args:null,kind:"ScalarField",name:"description",storageKey:null},x={alias:null,args:null,kind:"ScalarField",name:"url",storageKey:null},U=[i,A,r,{alias:null,args:null,kind:"ScalarField",name:"nameHTML",storageKey:null},V,x],O={alias:null,args:null,kind:"ScalarField",name:"totalCount",storageKey:null},_={alias:null,args:D,concreteType:"LabelConnection",kind:"LinkedField",name:"labels",plural:!1,selections:[{alias:null,args:null,concreteType:"LabelEdge",kind:"LinkedField",name:"edges",plural:!0,selections:[{alias:null,args:null,concreteType:"Label",kind:"LinkedField",name:"node",plural:!1,selections:[{kind:"InlineDataFragmentSpread",name:"LabelPickerLabel",selections:U,args:null,argumentDefinitions:[]}],storageKey:null}],storageKey:null},O],storageKey:'labels(first:20,orderBy:{"direction":"ASC","field":"NAME"})'},N=[{kind:"Literal",name:"first",value:10}],j=[i,u,r,o],Q={alias:null,args:N,concreteType:"UserConnection",kind:"LinkedField",name:"assignees",plural:!1,selections:[{alias:null,args:null,concreteType:"UserEdge",kind:"LinkedField",name:"edges",plural:!0,selections:[{alias:null,args:null,concreteType:"User",kind:"LinkedField",name:"node",plural:!1,selections:[{kind:"InlineDataFragmentSpread",name:"AssigneePickerAssignee",selections:j,args:null,argumentDefinitions:[]}],storageKey:null}],storageKey:null},O],storageKey:"assignees(first:10)"},M=[i,r,{alias:null,args:null,kind:"ScalarField",name:"isEnabled",storageKey:null},V,A],z={alias:null,args:null,concreteType:"IssueType",kind:"LinkedField",name:"type",plural:!1,selections:[{kind:"InlineDataFragmentSpread",name:"IssueTypePickerIssueType",selections:M,args:null,argumentDefinitions:[]}],storageKey:null},W={kind:"ClientExtension",selections:[{alias:null,args:null,kind:"ScalarField",name:"__id",storageKey:null}]},q=[E],H=[i,C,{alias:null,args:null,kind:"ScalarField",name:"closed",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"number",storageKey:null},x,{alias:null,args:null,kind:"ScalarField",name:"viewerCanUpdate",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"hasReachedItemsLimit",storageKey:null},R],B={alias:null,args:null,concreteType:"RepositoryContactLink",kind:"LinkedField",name:"contactLinks",plural:!0,selections:[r,v,x,R,W],storageKey:null},$={alias:null,args:D,concreteType:"LabelConnection",kind:"LinkedField",name:"labels",plural:!1,selections:[{alias:null,args:null,concreteType:"LabelEdge",kind:"LinkedField",name:"edges",plural:!0,selections:[{alias:null,args:null,concreteType:"Label",kind:"LinkedField",name:"node",plural:!1,selections:U,storageKey:null}],storageKey:null},O],storageKey:'labels(first:20,orderBy:{"direction":"ASC","field":"NAME"})'},X={alias:null,args:N,concreteType:"UserConnection",kind:"LinkedField",name:"assignees",plural:!1,selections:[{alias:null,args:null,concreteType:"UserEdge",kind:"LinkedField",name:"edges",plural:!0,selections:[{alias:null,args:null,concreteType:"User",kind:"LinkedField",name:"node",plural:!1,selections:j,storageKey:null}],storageKey:null},O],storageKey:"assignees(first:10)"},Y={alias:null,args:null,concreteType:"IssueType",kind:"LinkedField",name:"type",plural:!1,selections:M,storageKey:null},J={alias:"itemId",args:null,kind:"ScalarField",name:"id",storageKey:null},G={alias:null,args:null,kind:"ScalarField",name:"label",storageKey:null},Z={alias:null,args:null,kind:"ScalarField",name:"descriptionHTML",storageKey:null},ee={alias:null,args:null,kind:"ScalarField",name:"placeholder",storageKey:null},el={alias:null,args:null,kind:"ScalarField",name:"value",storageKey:null},ea={alias:null,args:null,kind:"ScalarField",name:"required",storageKey:null};return{fragment:{argumentDefinitions:[e,l,a],kind:"Fragment",metadata:null,name:"RepositoryPickerCurrentRepoQuery",selections:[{alias:null,args:n,concreteType:"Repository",kind:"LinkedField",name:"repository",plural:!1,selections:[{kind:"InlineDataFragmentSpread",name:"RepositoryPickerRepository",selections:[i,s,r,t,{alias:null,args:null,concreteType:null,kind:"LinkedField",name:"owner",plural:!1,selections:[s,u,o],storageKey:null},d,c,g,m,y,k,p,F,K,S,b,f,I],args:null,argumentDefinitions:[]},{condition:"includeTemplates",kind:"Condition",passingValue:!0,selections:[{kind:"InlineDataFragmentSpread",name:"RepositoryPickerRepositoryIssueTemplates",selections:[h,K,L,T,{alias:null,args:null,concreteType:"IssueTemplate",kind:"LinkedField",name:"issueTemplates",plural:!0,selections:[R,v,r,P,w,C,_,Q,z,W],storageKey:null},{alias:null,args:null,concreteType:"IssueForm",kind:"LinkedField",name:"issueForms",plural:!0,selections:[R,r,V,P,C,{kind:"InlineDataFragmentSpread",name:"IssueFormElements_templateElements",selections:[{alias:null,args:null,concreteType:null,kind:"LinkedField",name:"elements",plural:!0,selections:[R,{kind:"InlineFragment",selections:[{args:null,kind:"FragmentSpread",name:"TextInputElement_input"}],type:"IssueFormElementInput",abstractKey:null},{kind:"InlineFragment",selections:[{args:null,kind:"FragmentSpread",name:"TextAreaElement_input"}],type:"IssueFormElementTextarea",abstractKey:null},{kind:"InlineFragment",selections:[{args:null,kind:"FragmentSpread",name:"MarkdownElement_input"}],type:"IssueFormElementMarkdown",abstractKey:null},{kind:"InlineFragment",selections:[{args:null,kind:"FragmentSpread",name:"DropdownElement_input"}],type:"IssueFormElementDropdown",abstractKey:null},{kind:"InlineFragment",selections:[{args:null,kind:"FragmentSpread",name:"CheckboxesElement_input"}],type:"IssueFormElementCheckboxes",abstractKey:null}],storageKey:null}],args:null,argumentDefinitions:[]},_,Q,{alias:null,args:q,concreteType:"ProjectV2Connection",kind:"LinkedField",name:"projects",plural:!1,selections:[{alias:null,args:null,concreteType:"ProjectV2Edge",kind:"LinkedField",name:"edges",plural:!0,selections:[{alias:null,args:null,concreteType:"ProjectV2",kind:"LinkedField",name:"node",plural:!1,selections:[{kind:"InlineDataFragmentSpread",name:"ProjectPickerProject",selections:H,args:null,argumentDefinitions:[]}],storageKey:null}],storageKey:null}],storageKey:"projects(first:20)"},z,W],storageKey:null},B],args:null,argumentDefinitions:[]}]}],storageKey:null}],type:"Query",abstractKey:null},kind:"Request",operation:{argumentDefinitions:[a,l,e],kind:"Operation",name:"RepositoryPickerCurrentRepoQuery",selections:[{alias:null,args:n,concreteType:"Repository",kind:"LinkedField",name:"repository",plural:!1,selections:[i,s,r,t,{alias:null,args:null,concreteType:null,kind:"LinkedField",name:"owner",plural:!1,selections:[R,s,u,o,i],storageKey:null},d,c,g,m,y,k,p,F,K,S,b,f,I,{condition:"includeTemplates",kind:"Condition",passingValue:!0,selections:[h,L,T,{alias:null,args:null,concreteType:"IssueTemplate",kind:"LinkedField",name:"issueTemplates",plural:!0,selections:[R,v,r,P,w,C,$,X,Y,W],storageKey:null},{alias:null,args:null,concreteType:"IssueForm",kind:"LinkedField",name:"issueForms",plural:!0,selections:[R,r,V,P,C,{alias:null,args:null,concreteType:null,kind:"LinkedField",name:"elements",plural:!0,selections:[R,{kind:"InlineFragment",selections:[J,G,Z,ee,el,ea,W],type:"IssueFormElementInput",abstractKey:null},{kind:"InlineFragment",selections:[J,G,Z,ee,el,ea,{alias:null,args:null,kind:"ScalarField",name:"render",storageKey:null},W],type:"IssueFormElementTextarea",abstractKey:null},{kind:"InlineFragment",selections:[{alias:null,args:null,kind:"ScalarField",name:"contentHTML",storageKey:null}],type:"IssueFormElementMarkdown",abstractKey:null},{kind:"InlineFragment",selections:[G,Z,{alias:null,args:null,kind:"ScalarField",name:"options",storageKey:null},ea,{alias:null,args:null,kind:"ScalarField",name:"multiple",storageKey:null},{alias:"defaultOptionIndex",args:null,kind:"ScalarField",name:"default",storageKey:null},W],type:"IssueFormElementDropdown",abstractKey:null},{kind:"InlineFragment",selections:[G,Z,{alias:"checkboxOptions",args:null,concreteType:"IssueFormElementCheckboxOption",kind:"LinkedField",name:"options",plural:!0,selections:[G,{alias:null,args:null,kind:"ScalarField",name:"labelHTML",storageKey:null},ea],storageKey:null},W],type:"IssueFormElementCheckboxes",abstractKey:null}],storageKey:null},$,X,{alias:null,args:q,concreteType:"ProjectV2Connection",kind:"LinkedField",name:"projects",plural:!1,selections:[{alias:null,args:null,concreteType:"ProjectV2Edge",kind:"LinkedField",name:"edges",plural:!0,selections:[{alias:null,args:null,concreteType:"ProjectV2",kind:"LinkedField",name:"node",plural:!1,selections:H,storageKey:null}],storageKey:null}],storageKey:"projects(first:20)"},Y,W],storageKey:null},B]}],storageKey:null}]},params:{id:"d19da59a0e07ebcc782d35400810282b",metadata:{},name:"RepositoryPickerCurrentRepoQuery",operationKind:"query",text:null}}}();n.hash="a86960f12fe252ddbacabc1d0618c27a";let i=n},62191:(e,l,a)=>{a.d(l,{SR:()=>I,R6:()=>P,DM:()=>w,f0:()=>E,ow:()=>D,i_:()=>C,XD:()=>v,m:()=>L,Sy:()=>T,DW:()=>h,Xl:()=>R});var n=a(74848),i=a(15629);let s=function(){var e={defaultValue:null,kind:"LocalArgument",name:"hasIssuesEnabled"},l={defaultValue:null,kind:"LocalArgument",name:"owner"},a={defaultValue:10,kind:"LocalArgument",name:"topRepositoriesFirst"},n={kind:"Variable",name:"hasIssuesEnabled",variableName:"hasIssuesEnabled"},i={kind:"Variable",name:"owner",variableName:"owner"},s={alias:null,args:null,kind:"ScalarField",name:"id",storageKey:null},r={alias:null,args:null,kind:"ScalarField",name:"databaseId",storageKey:null};return{fragment:{argumentDefinitions:[e,l,a],kind:"Fragment",metadata:null,name:"RepositoryPickerTopRepositoriesQuery",selections:[{alias:null,args:null,concreteType:"User",kind:"LinkedField",name:"viewer",plural:!1,selections:[{args:[n,i,{kind:"Variable",name:"topRepositoriesFirst",variableName:"topRepositoriesFirst"}],kind:"FragmentSpread",name:"RepositoryPickerTopRepositories"}],storageKey:null}],type:"Query",abstractKey:null},kind:"Request",operation:{argumentDefinitions:[a,e,l],kind:"Operation",name:"RepositoryPickerTopRepositoriesQuery",selections:[{alias:null,args:null,concreteType:"User",kind:"LinkedField",name:"viewer",plural:!1,selections:[{alias:null,args:[{kind:"Variable",name:"first",variableName:"topRepositoriesFirst"},n,{kind:"Literal",name:"orderBy",value:{direction:"DESC",field:"UPDATED_AT"}},i],concreteType:"RepositoryConnection",kind:"LinkedField",name:"topRepositories",plural:!1,selections:[{alias:null,args:null,concreteType:"RepositoryEdge",kind:"LinkedField",name:"edges",plural:!0,selections:[{alias:null,args:null,concreteType:"Repository",kind:"LinkedField",name:"node",plural:!1,selections:[s,r,{alias:null,args:null,kind:"ScalarField",name:"name",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"nameWithOwner",storageKey:null},{alias:null,args:null,concreteType:null,kind:"LinkedField",name:"owner",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"__typename",storageKey:null},r,{alias:null,args:null,kind:"ScalarField",name:"login",storageKey:null},{alias:null,args:[{kind:"Literal",name:"size",value:64}],kind:"ScalarField",name:"avatarUrl",storageKey:"avatarUrl(size:64)"},s],storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"isPrivate",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"visibility",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"isArchived",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"isInOrganization",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"hasIssuesEnabled",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"slashCommandsEnabled",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"viewerCanPush",storageKey:null},{alias:null,args:null,concreteType:"IssueCreationPermissions",kind:"LinkedField",name:"viewerIssueCreationPermissions",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"labelable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"milestoneable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"assignable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"triageable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"typeable",storageKey:null}],storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"securityPolicyUrl",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"contributingFileUrl",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"codeOfConductFileUrl",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"shortDescriptionHTML",storageKey:null},{alias:null,args:null,concreteType:"RepositoryPlanFeatures",kind:"LinkedField",name:"planFeatures",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"maximumAssignees",storageKey:null}],storageKey:null}],storageKey:null}],storageKey:null}],storageKey:null},s],storageKey:null}]},params:{id:"261dd4bf8cd2ba06d5bf2c454463f784",metadata:{},name:"RepositoryPickerTopRepositoriesQuery",operationKind:"query",text:null}}}();s.hash="73e96d7c429663ba233d926c532b97e4";let r=function(){var e={alias:null,args:null,kind:"ScalarField",name:"databaseId",storageKey:null};return{argumentDefinitions:[{defaultValue:!0,kind:"LocalArgument",name:"hasIssuesEnabled"},{defaultValue:null,kind:"LocalArgument",name:"owner"},{defaultValue:10,kind:"LocalArgument",name:"topRepositoriesFirst"}],kind:"Fragment",metadata:null,name:"RepositoryPickerTopRepositories",selections:[{alias:null,args:[{kind:"Variable",name:"first",variableName:"topRepositoriesFirst"},{kind:"Variable",name:"hasIssuesEnabled",variableName:"hasIssuesEnabled"},{kind:"Literal",name:"orderBy",value:{direction:"DESC",field:"UPDATED_AT"}},{kind:"Variable",name:"owner",variableName:"owner"}],concreteType:"RepositoryConnection",kind:"LinkedField",name:"topRepositories",plural:!1,selections:[{alias:null,args:null,concreteType:"RepositoryEdge",kind:"LinkedField",name:"edges",plural:!0,selections:[{alias:null,args:null,concreteType:"Repository",kind:"LinkedField",name:"node",plural:!1,selections:[{kind:"InlineDataFragmentSpread",name:"RepositoryPickerRepository",selections:[{alias:null,args:null,kind:"ScalarField",name:"id",storageKey:null},e,{alias:null,args:null,kind:"ScalarField",name:"name",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"nameWithOwner",storageKey:null},{alias:null,args:null,concreteType:null,kind:"LinkedField",name:"owner",plural:!1,selections:[e,{alias:null,args:null,kind:"ScalarField",name:"login",storageKey:null},{alias:null,args:[{kind:"Literal",name:"size",value:64}],kind:"ScalarField",name:"avatarUrl",storageKey:"avatarUrl(size:64)"}],storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"isPrivate",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"visibility",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"isArchived",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"isInOrganization",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"hasIssuesEnabled",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"slashCommandsEnabled",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"viewerCanPush",storageKey:null},{alias:null,args:null,concreteType:"IssueCreationPermissions",kind:"LinkedField",name:"viewerIssueCreationPermissions",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"labelable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"milestoneable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"assignable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"triageable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"typeable",storageKey:null}],storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"securityPolicyUrl",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"contributingFileUrl",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"codeOfConductFileUrl",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"shortDescriptionHTML",storageKey:null},{alias:null,args:null,concreteType:"RepositoryPlanFeatures",kind:"LinkedField",name:"planFeatures",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"maximumAssignees",storageKey:null}],storageKey:null}],args:null,argumentDefinitions:[]}],storageKey:null}],storageKey:null}],storageKey:null}],type:"User",abstractKey:null}}();r.hash="d57ff072515ddc886c611e82b42e0bde";let t=function(){var e={defaultValue:null,kind:"LocalArgument",name:"after"},l={defaultValue:null,kind:"LocalArgument",name:"searchQuery"},a=[{kind:"Variable",name:"after",variableName:"after"},{kind:"Literal",name:"first",value:10},{kind:"Variable",name:"query",variableName:"searchQuery"},{kind:"Literal",name:"type",value:"REPOSITORY"}],n={alias:null,args:null,kind:"ScalarField",name:"repositoryCount",storageKey:null},i={alias:null,args:null,concreteType:"PageInfo",kind:"LinkedField",name:"pageInfo",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"hasNextPage",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"endCursor",storageKey:null}],storageKey:null},s={alias:null,args:null,kind:"ScalarField",name:"id",storageKey:null},r={alias:null,args:null,kind:"ScalarField",name:"databaseId",storageKey:null},t={alias:null,args:null,kind:"ScalarField",name:"name",storageKey:null},u={alias:null,args:null,kind:"ScalarField",name:"nameWithOwner",storageKey:null},o={alias:null,args:null,kind:"ScalarField",name:"login",storageKey:null},d={alias:null,args:[{kind:"Literal",name:"size",value:64}],kind:"ScalarField",name:"avatarUrl",storageKey:"avatarUrl(size:64)"},c={alias:null,args:null,kind:"ScalarField",name:"isPrivate",storageKey:null},g={alias:null,args:null,kind:"ScalarField",name:"visibility",storageKey:null},m={alias:null,args:null,kind:"ScalarField",name:"isArchived",storageKey:null},y={alias:null,args:null,kind:"ScalarField",name:"isInOrganization",storageKey:null},k={alias:null,args:null,kind:"ScalarField",name:"hasIssuesEnabled",storageKey:null},p={alias:null,args:null,kind:"ScalarField",name:"slashCommandsEnabled",storageKey:null},F={alias:null,args:null,kind:"ScalarField",name:"viewerCanPush",storageKey:null},K={alias:null,args:null,concreteType:"IssueCreationPermissions",kind:"LinkedField",name:"viewerIssueCreationPermissions",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"labelable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"milestoneable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"assignable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"triageable",storageKey:null},{alias:null,args:null,kind:"ScalarField",name:"typeable",storageKey:null}],storageKey:null},S={alias:null,args:null,kind:"ScalarField",name:"securityPolicyUrl",storageKey:null},b={alias:null,args:null,kind:"ScalarField",name:"contributingFileUrl",storageKey:null},f={alias:null,args:null,kind:"ScalarField",name:"codeOfConductFileUrl",storageKey:null},I={alias:null,args:null,kind:"ScalarField",name:"shortDescriptionHTML",storageKey:null},h={alias:null,args:null,concreteType:"RepositoryPlanFeatures",kind:"LinkedField",name:"planFeatures",plural:!1,selections:[{alias:null,args:null,kind:"ScalarField",name:"maximumAssignees",storageKey:null}],storageKey:null},L={alias:null,args:null,kind:"ScalarField",name:"__typename",storageKey:null};return{fragment:{argumentDefinitions:[e,l],kind:"Fragment",metadata:null,name:"RepositoryPickerSearchRepositoriesQuery",selections:[{alias:null,args:a,concreteType:"SearchResultItemConnection",kind:"LinkedField",name:"search",plural:!1,selections:[n,i,{alias:null,args:null,concreteType:null,kind:"LinkedField",name:"nodes",plural:!0,selections:[{kind:"InlineFragment",selections:[{kind:"InlineDataFragmentSpread",name:"RepositoryPickerRepository",selections:[s,r,t,u,{alias:null,args:null,concreteType:null,kind:"LinkedField",name:"owner",plural:!1,selections:[r,o,d],storageKey:null},c,g,m,y,k,p,F,K,S,b,f,I,h],args:null,argumentDefinitions:[]}],type:"Repository",abstractKey:null}],storageKey:null}],storageKey:null}],type:"Query",abstractKey:null},kind:"Request",operation:{argumentDefinitions:[l,e],kind:"Operation",name:"RepositoryPickerSearchRepositoriesQuery",selections:[{alias:null,args:a,concreteType:"SearchResultItemConnection",kind:"LinkedField",name:"search",plural:!1,selections:[n,i,{alias:null,args:null,concreteType:null,kind:"LinkedField",name:"nodes",plural:!0,selections:[L,{kind:"InlineFragment",selections:[s,r,t,u,{alias:null,args:null,concreteType:null,kind:"LinkedField",name:"owner",plural:!1,selections:[L,r,o,d,s],storageKey:null},c,g,m,y,k,p,F,K,S,b,f,I,h],type:"Repository",abstractKey:null},{kind:"InlineFragment",selections:[s],type:"Node",abstractKey:"__isNode"}],storageKey:null}],storageKey:null}]},params:{id:"d2ef0c47b5c4e3854e97a0db0982c254",metadata:{},name:"RepositoryPickerSearchRepositoriesQuery",operationKind:"query",text:null}}}();t.hash="725e16a49931497bfc9fa961f3c8721a";let u={kind:"InlineDataFragment",name:"RepositoryPickerRepository"};u.hash="a402a6117a996f3e3724be24cc6b84f5";let o={kind:"InlineDataFragment",name:"RepositoryPickerRepositoryIssueTemplates"};o.hash="e80fbaec2adb2595ece108ec7e011688";var d=a(88360),c=a(54156),g=a(38621),m=a(55847),y=a(75177),k=a(96540),p=a(18312),F=a(72035),K=a(40415),S=a(35625),b=a(47555),f=a(39126);let I=i.A,h=(e,l="",a="",n=!1)=>(0,p.fetchQuery)(e,I,{owner:l,name:a,includeTemplates:n},{fetchPolicy:"store-or-network"}),L=s,T=r,R=(e,l=10,a)=>(0,p.fetchQuery)(e,L,{topRepositoriesFirst:l,hasIssuesEnabled:a},{fetchPolicy:"store-or-network"}),v=t,P=u,w=o,C=()=>(0,n.jsx)(m.Q,{leadingVisual:g.RepoIcon,trailingVisual:g.TriangleDownIcon,disabled:!0,children:K.k.selectRepository});function E({topReposQueryRef:e,...l}){let a=(0,p.usePreloadedQuery)(L,e);return a.viewer?(0,n.jsx)(D,{...l,topRepositoriesData:a.viewer}):null}function D({initialRepository:e,onSelect:l,preventDefault:a,organization:i,topRepositoriesData:s,focusRepositoryPicker:r,enforceAtleastOneSelected:t,options:{hasIssuesEnabled:u,readonly:o,includeForks:I}={hasIssuesEnabled:void 0,readonly:!1,includeForks:!1},renderTrailingVisual:h,exclude:L,"aria-labelledby":R,"aria-describedby":w,anchorElement:C,title:E,subtitle:D,preventClose:A,triggerOpen:V,onOpen:x,onClose:U,ignoredRepositories:O,repositoryFilter:_,customNoResultsItem:N,repoNameOnly:j,pickerId:Q,currentRepoVisibility:M}){let{addToast:z}=(0,c.Y6)(),[W,q]=(0,k.useState)(""),[H,B]=(0,k.useState)(void 0),[$,X]=(0,k.useState)(null==s);(0,k.useEffect)(()=>{null!=s&&X(!1)},[s]);let Y=(0,p.useRelayEnvironment)(),J=(0,k.useCallback)((e,l)=>{X(!0),(0,p.fetchQuery)(Y,v,{searchQuery:(0,b.J4)(e,i,L,I,M)}).subscribe({next:e=>{if(null!==e){let a=(e.search.nodes||[]).flatMap(e=>e?[(0,p.readInlineData)(P,e)]:[]);u&&(a=a.filter(e=>e.hasIssuesEnabled===u));let n=a.sort((e,a)=>l.includes(e.owner.login)&&!l.includes(a.owner.login)?-1:!l.includes(e.owner.login)&&l.includes(a.owner.login)?1:e.owner.login.localeCompare(a.owner.login));if(O){let e=new Set(O);n=n.filter(l=>!e.has(l.nameWithOwner))}_&&(n=n.filter(_)),B(n),X(!1)}},error:()=>{X(!1),z({type:"error",message:F.S.couldNotSearchRepositories})}})},[Y,i,L,I,u,O,_,z,M]),G=(0,d.d)(e=>J(e,es),f.t.pickerDebounceTime);(0,k.useEffect)(()=>{if(0===W.length){B(void 0);return}G(W)},[G,W]);let Z=(0,k.useCallback)(e=>e.id,[]),ee=(0,k.useRef)(null);(0,k.useEffect)(()=>{r&&ee.current?.focus()},[ee,r]);let el=(0,k.useCallback)(({...l})=>C?C(l):(0,n.jsx)(m.Q,{leadingVisual:g.RepoIcon,trailingVisual:g.TriangleDownIcon,"aria-label":R?void 0:K.k.selectRepository,"aria-labelledby":R,"aria-describedby":w,...l,disabled:o,ref:ee,children:e?(0,n.jsx)("span",{children:j?e.name:`${e.owner.login}/${e.name}`}):K.k.selectRepository}),[C,w,R,e,o,j]),ea=(0,k.useCallback)(e=>({id:`${e.id}_${e.databaseId}_${e.slashCommandsEnabled}`,children:(0,n.jsx)("span",{children:j?e.name:`${e.owner.login}/${e.name}`}),source:e,leadingVisual:()=>e.isPrivate?(0,n.jsx)(g.LockIcon,{size:12}):(0,n.jsx)(g.RepoIcon,{size:12}),trailingVisual:h?.(e.id),sx:{wordBreak:"break-word"}}),[h,j]),en=(0,p.useFragment)(T,s),ei=(0,k.useMemo)(()=>{let l=(en?.topRepositories.edges||[]).flatMap(e=>e?.node?[(0,p.readInlineData)(P,e.node)]:[]);if(e&&!l.find(l=>l.id===e.id)&&(l=[e,...l]),i&&(l=l.filter(e=>e.owner.login===i)),L&&(l=l.filter(e=>e.nameWithOwner!==L)),O){let e=new Set(O);l=l.filter(l=>!e.has(l.nameWithOwner))}return l.slice(0,10)},[L,e,i,O,en]),es=(0,k.useMemo)(()=>[...new Set(ei.map(e=>e.owner.login))],[ei]),er=(0,k.useMemo)(()=>{if(H)return H;let e=ei.filter(e=>!e.isArchived);return _?e.filter(_):e},[ei,_,H]);(0,k.useEffect)(()=>{e||!(er.length>0)||a||l(er[0])},[]);let et=(0,k.useCallback)(e=>{o||q(e)},[o]);return(0,n.jsx)(y.A,{sx:{display:"flex",flexDirection:"row",flexWrap:"wrap",gap:1},children:(0,n.jsx)(S.O,{items:er,initialSelectedItems:e?[e]:[],filterItems:et,getItemKey:Z,convertToItemProps:ea,placeholderText:K.k.selectRepository,selectionVariant:"single",onSelectionChange:([e])=>l(e),loading:$,renderAnchor:el,selectPanelRef:ee,enforceAtleastOneSelected:t,resultListAriaLabel:"Repository results",height:"large",width:"medium",title:E,subtitle:D,preventClose:A,triggerOpen:V,onOpen:x,onClose:U,customNoResultsItem:N?{children:N}:void 0,pickerId:Q})})}try{C.displayName||(C.displayName="RepositoryPickerPlaceholder")}catch{}try{E.displayName||(E.displayName="RepositoryPicker")}catch{}try{D.displayName||(D.displayName="RepositoryPickerInternal")}catch{}}}]);
//# sourceMappingURL=ui_packages_item-picker_components_RepositoryPicker_tsx-5f2fa6bd87fe.js.map